from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from app.logger import logger
import os

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="FastAPI Secure API", version="1.0")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# CORS Middleware - Restrict origins for better security
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["X-API-KEY"],
)

app.include_router(router)

@app.get("/")
def hello_world():
    """Example Hello World route."""
    name = os.getenv("NAME", "World")
    return {"message": f"Hello {name}!"}

