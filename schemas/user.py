from pydantic import BaseModel

class detail_user(BaseModel):
    userName: str = None
    email: str = None
    phoneNumber: int = None
    country: str = None
    state: str = None
    city: str = None
    address: str = None
    zipCode: int = None
    company: str = None
    role: str = None
    isVerified: bool = None