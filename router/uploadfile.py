from fastapi import APIRouter, Depends, UploadFile, File
import os, pathlib, shutil
from datetime import datetime
from sqlalchemy.orm import Session
from dataBase import get_db
from utils.send_email import sendInvoice

router = APIRouter(tags=["Upload file"])

def uploadFile(uploaded_file: UploadFile, folder: str):

    os.makedirs(f"files/{folder}", mode=0o777, exist_ok=True)
    name, exten = os.path.splitext(uploaded_file.filename)
    time_stamp = int(datetime.timestamp(datetime.now()))
    file_name = f"{name}_{time_stamp}" + exten
    if exten == '':
        exten = ".png"
    dest = f"files/{folder}/{file_name}"
    with open(pathlib.Path(dest), "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    
    return dest

@router.post('/uploadfile')
def upload_file(
    uploaded_file: UploadFile = File(...), 
    db: Session = Depends(get_db)):

    file_path = uploadFile(uploaded_file, "productImage")

    return {"message": "Product images uploaded sucessfully", "file_path": file_path}

@router.post('/share_invoice_on_mail')
async def share_invoice_on_mail(
    email: str,
    uploaded_file: UploadFile = File(...), 
    db: Session = Depends(get_db)):

    file_path = uploadFile(uploaded_file, "productPDF")

    await sendInvoice("INV-71", email, file_path)

    return {"message": "Product images uploaded sucessfully", "file_path": file_path}