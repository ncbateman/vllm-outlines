import logging
import uuid
import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from vllm import AsyncLLMEngine, SamplingParams
from outlines.serve.vllm import JSONLogitsProcessor
from src.model.config import engine, tokenizer
from types import SimpleNamespace

router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.websocket("/ws/inference/guided")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            if 'prompt' in data and 'schema' in data:
                await generate_and_stream(data, websocket)
            else:
                await websocket.send_json({"error": "Missing 'prompt' or 'schema' key in request."})

    except WebSocketDisconnect as e:
        logging.info(f"WebSocket disconnected with code: {e.code}")
    except Exception as e:
        logging.error(f"Error during WebSocket communication: {e}")
        await websocket.close(code=1011)

async def generate_and_stream(json_data, websocket):
    prompt = json_data['prompt']
    schema_dict = json_data['schema']
    schema = json.dumps(schema_dict)
    max_tokens = json_data.get('max_tokens', 50)
    temperature = json_data.get('temperature', 0.0)
    top_p = json_data.get('top_p', 1)
    number_of_logprobs = json_data.get('number_of_logprobs', 0)

    # Tokenize the prompt and convert to token IDs
    prompt_token_ids = tokenizer.encode(prompt, add_special_tokens=True)

    dummy_llm = SimpleNamespace(
        tokenizer=SimpleNamespace(
            tokenizer=tokenizer,
        )
    )
    
    logits_processor = JSONLogitsProcessor(schema=schema, llm=dummy_llm)
    
    sampling_params = SamplingParams(
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        logprobs=number_of_logprobs,
        top_k=5,
        logits_processors=[logits_processor]
    )

    request_id = uuid.uuid4().hex
    async for request_output in engine.generate(
        prompt=None,  # We are using token IDs now
        prompt_token_ids=prompt_token_ids,
        sampling_params=sampling_params,
        request_id=request_id
    ):
        text = request_output.outputs[0].text
        await websocket.send_json({"stream_response": [{"text": text, "sender": "ai", "request": request_id}]})


