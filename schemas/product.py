from pydantic import BaseModel

class detail_product(BaseModel):
    productName: str = None
    description: str = None
    inStock: bool = None
    productCode: str = None
    # gender: str = None
    category: str = None
    price: int = None
    # taxes: bool = None