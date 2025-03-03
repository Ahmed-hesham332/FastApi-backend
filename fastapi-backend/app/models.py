from pydantic import BaseModel

class AddressResponse(BaseModel):
    street: str = "123 Main Street"
    city: str = "Abu Dhabi"
    country: str = "UAE"
    postcode: str
