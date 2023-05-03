from pydantic import BaseModel

class detail_register(BaseModel):
    userName: str = None
    password : str = None
    email: str = None
    mobile: int = None

class pass_reset(BaseModel):
    user_email_id: str = None
    password: str = None
    otp : str = None
    othersPassReset: str = None