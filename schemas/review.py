from pydantic import BaseModel

class detail_review(BaseModel):
    review: str = None
    # name: str = None
    email: str = None
    rating: str = None
    product_id: int = None
    