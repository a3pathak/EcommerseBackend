from pydantic import BaseModel

class Detail_Cart(BaseModel):
    productName: str = None
    price: int = None
    quantity: int = None
    totalPrice: int = None