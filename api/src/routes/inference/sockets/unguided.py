import logging
import uuid
from fastapi import FastAPI, APIRouter, WebSocket, status
from fastapi.responses import JSONResponse
from starlette.websockets import WebSocketDisconnect
from vllm import AsyncLLMEngine, SamplingParams
from src.model.config import engine

router = APIRouter()

logging.basicConfig(level=logging.DEBUG)

@router.websocket("/ws/inference/unguided")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            if 'prompt' in data:
                await generate_and_stream(data, websocket)
            else:
                await websocket.send_json({"error": "No prompt found."})
    except WebSocketDisconnect as e:
        print(f"WebSocket disconnected with code: {e.code}")
    except Exception as e:
        print(f"Error during WebSocket communication: {e}")
        await websocket.close(code=1011)  # Use an appropriate WebSocket close code

async def generate_and_stream(json_data, websocket):
    prompt = json_data['prompt']
    real_prompt = f'''Below is an instruction that describes a task. Write a very short descriptive response that appropriately completes the request. Do not expand beyond the users specific instructions.

        ### Instruction:
        {prompt}

        Be very concise with your answer. Never impersonate the user. Never reply more than once as the AI.

        ### Response:
    '''
    max_tokens = 2048
    temperature = json_data['temperature']
    top_p = json_data['top_p']
    number_of_logprobs = json_data['number_of_logprobs']

    sampling_params = SamplingParams(
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p if top_p != 0 else 1,
        logprobs=number_of_logprobs,
        top_k=5
    )

    # Generating outputs for the request
    request_id = uuid.uuid4().hex
    async for request_output in engine.generate(
        prompt=real_prompt,
        sampling_params=sampling_params,
        request_id=request_id
    ):
        text = request_output.outputs[0].text
        await websocket.send_json({"stream_response": [{"text": text, "sender": "ai", "request": request_id}]})