from pydantic import BaseModel

class detail_address(BaseModel):
    address1: str = None
    address2: str = None
    state: str = None
    country: str = None
    pincode: int = None
    city: str = None