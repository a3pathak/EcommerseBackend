from fastapi import APIRouter, Depends, HTTPException, status
from dataBase import get_db
from sqlalchemy.orm import Session
from models import Review
from schemas.review import detail_review

router = APIRouter(tags=["Review"])

@router.post('/review')
def createReview(request: detail_review, db: Session = Depends(get_db)):
     
     data = dict(request)
     data = Review(**data)
     db.add(data)
     db.flush()
     db.commit()

     return {"message": "Review has been created sucessfully"}

@router.get('/review')
def getAllReview(db: Session = Depends(get_db)):
    
    data = db.query(Review).all()

    return data
 