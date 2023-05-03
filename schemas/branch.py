from pydantic import BaseModel

class Branch_Detail(BaseModel):
    branchName: str = None
    branchAddress1: str = None
    branchAddress2: str = None
    branchCity: str = None
    branchState: int = None
    branchCountry: int = None
    branchPincode: int = None
