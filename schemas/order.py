from pydantic import BaseModel

class Order_Details(BaseModel):
    product_id: int
    payment_stat: bool
    productName: str = None
    amount: str=None