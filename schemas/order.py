from pydantic import BaseModel

class Order_Details(BaseModel):
    product_id: int = None
    payment_stat: bool = False
    productName: str = None
    amount: str=None