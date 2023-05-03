from fastapi import APIRouter, Depends
from dataBase import get_db
from sqlalchemy.orm import Session
from schemas.address import detail_address
from models import AddressDetail

router = APIRouter(tags=["Address"])

@router.post('/address')
def add_address(request: detail_address, db: Session = Depends(get_db)):
    
    data = dict(request)
    row = AddressDetail(**data)
    db.add(row)
    db.commit()

    return {"message": "Address has been saved sucessfully"}

@router.get('/address')
def add_address(db: Session = Depends(get_db)):
    
    data = db.query(AddressDetail).all()

    return data