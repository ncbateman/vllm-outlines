from vllm.engine.arg_utils import AsyncEngineArgs
from vllm import AsyncLLMEngine, SamplingParams
from transformers import AutoTokenizer
import logging

logging.basicConfig(level=logging.DEBUG)

MODEL_NAME_OR_PATH = "./models/model"
engine_args = AsyncEngineArgs(model=MODEL_NAME_OR_PATH, tensor_parallel_size=2, dtype='half')

try:
    engine = AsyncLLMEngine.from_engine_args(engine_args)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME_OR_PATH)
    logging.info("Async LLM Engine initialized successfully")
except Exception as e:
    logging.error(f"An error occurred during model initialization: {e}")