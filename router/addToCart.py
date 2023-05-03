from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dataBase import get_db
from schemas.cart import Detail_Cart
from models import CartDetail

router = APIRouter(tags=["Cart"])

@router.post('/post_cart')
def add_to_cart(
    request: Detail_Cart,
    db: Session = Depends(get_db)):

    data = dict(request)
    data = CartDetail(**data)
    db.add(data)
    db.flush()
    db.commit()

    return {"message": "Product has been add to cart sucessfully"}

@router.get('/get_cart')
def get_cart(db: Session = Depends(get_db)):

    data = db.query(CartDetail).all()

    return data