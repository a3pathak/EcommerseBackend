from fastapi import APIRouter, Depends, HTTPException, status
from schemas.order import Order_Details
from sqlalchemy.orm import Session
from dataBase import get_db
from models import OrderDetails

router = APIRouter(tags= ["orders"])

@router.post('/order')
def create_order(request:Order_Details, db: Session = Depends(get_db)):

    data = OrderDetails(
        product_id = request.product_id,
        payment_stat = request.payment_stat,
        productName = request.productName,
        amount = request.amount,
    )
    db.add(data)
    db.commit()

    return {'message': "Order has been saved sucessfully"}

@router.get('/orderAll')
def getAll_order(db: Session= Depends(get_db)):

    orderData = db.query(OrderDetails).all()

    return orderData

@router.get('/order/{ID}')
def get_order(
    ID: int,
    db: Session = Depends(get_db)
):
    orderData = db.query(OrderDetails).filter(OrderDetails.id == ID).first()

    return orderData

@router.put('/order/{ID}')
def update_order(ID: int, request: Order_Details , db: Session = Depends(get_db)):

    check = db.query(OrderDetails).filter(OrderDetails.id == ID)

    if not check.first():
        raise HTTPException(status_code = status.HTTP400, details="There is not order avilable with this id")
    else:
        check.update(**request)
        db.commit()

    return {"message": "Order has been updated sucecssfully"}

@router.delete('/order/{ID}')
def delete_order(ID: int, db: Session = Depends(get_db)):
    check = db.query(OrderDetails).filter(OrderDetails.id == ID)

    if not check.first():
        raise HTTPException(status_code = status.HTTP400, details="There is not order avilable with this id")

    else:
        check.delete()
        db.commit()
    return { "message": "Order has been deleted sucessfully"}