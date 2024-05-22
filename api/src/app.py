from fastapi import FastAPI
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from src.routes import router

# Create the FastAPI app instance
app = FastAPI(title="Home GPT API", version="1.0")

# Configure CORS
origins = [
    "*",
    # Add other origins as needed, or use "*" to allow all origins (not recommended for production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# # Include the routers from the routes package
app.include_router(router)
