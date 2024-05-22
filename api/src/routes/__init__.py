from fastapi import APIRouter

# health checks
from src.routes.health import router as health_router

# inference routes
# from src.routes.inference.rest import router as inference_rest_router
# from src.routes.inference.sockets.guided import router as guided_inference_sockets_router
from src.routes.inference.sockets.character import router as character_inference_sockets_router
from src.routes.inference.sockets.unguided import router as unguided_inference_sockets_router
# from src.routes.sockets.sse import router as inference_sse_router

router = APIRouter()

# Utilities
router.include_router(health_router)
# router.include_router(guided_inference_sockets_router)
router.include_router(unguided_inference_sockets_router)
# router.include_router(character_inference_sockets_router)