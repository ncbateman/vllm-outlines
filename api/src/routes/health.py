from fastapi import APIRouter, status
from starlette.responses import JSONResponse

router = APIRouter()

@router.post("/health")
def health_check_post():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "healthy"})

@router.get("/health")
def health_check_get():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "healthy"})
