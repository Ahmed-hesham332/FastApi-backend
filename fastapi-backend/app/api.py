from fastapi import APIRouter, Depends
from app.config import settings
from app.models import AddressResponse
from app.dependencies import get_api_key
from app.logger import logger

# Define API Router (Make sure it's at the top)
router = APIRouter()

@router.get("/address", response_model=AddressResponse, dependencies=[Depends(get_api_key)])
def get_address():
    logger.info("Address endpoint accessed")
    return AddressResponse(postcode=settings.POSTCODE)
