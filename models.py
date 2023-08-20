from email.policy import default
from sqlalchemy import Column, Integer, String, BigInteger, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from typing import Any
from dataBase import Base as Basex
from sqlalchemy.orm import relationship

class Base(Basex):
    __abstract__ = True

    #to generate tablename from classname
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class Admin(Base):
    id = Column(Integer, index= True, primary_key = True)
    userName = Column(String(500), default = None)
    password = Column(String(500), default = None)
    email = Column(String(500), unique=True, default = None)
    mobile = Column(BigInteger, unique=True, default = None)    

class User(Base):
    id = Column(Integer, index= True, primary_key = True)
    userName = Column(String(500), default = None)
    email = Column(String(500), default = None)
    phoneNumber = Column(BigInteger, default = False)
    password = Column(String(100), default=None)
    products = relationship("Product", back_populates="owner")
    orders = relationship("OrderDetails", back_populates="owner")

class password_reset(Base):
    id = Column(Integer, index= True, primary_key = True)
    user_email_id = Column(String(500), nullable=False, unique=True)
    otp = Column(Integer, default = None)
    othersPassReset = Column(String(500), default="")

class Product(Base):
    id = Column(Integer, index= True, primary_key = True)
    productName = Column(String(500), default = None)
    description = Column(String(10000), default = None)
    inStock = Column(Boolean, default = False)
    productCode = Column(String(500), default = None)    
    gender = Column(String(500), default = None)    
    category = Column(String(500), default = None)    
    price = Column(Integer, default = None)    
    taxes = Column(Boolean, default = False)   
    user_id = Column(Integer, ForeignKey("user.id"))
    branchID = Column(Integer, default=None)
    owner = relationship("User", back_populates="products")
    
class Branch(Base):
    id = Column(Integer, index= True, primary_key = True)
    branchName = Column(String(500), default = None)
    branchAddress1 = Column(String(500), default = None)
    branchAddress2 = Column(String(500), default = None)
    branchCity = Column(String(500), default = None)    
    branchState = Column(Integer, default = None)    
    branchCountry = Column(Integer, default = None)    
    branchPincode = Column(Integer, default = None)
    user_id = Column(Integer, default=None)

class AddressDetail(Base):
    id = Column(Integer, index= True, primary_key = True)
    address1 = Column(String(500), default = None)    
    address2 = Column(String(500), default = None)    
    state = Column(String(500), default = None)    
    country = Column(String(500), default = None)    
    city = Column(String(500), default = None)  
    pincode = Column(Integer, default = False)
    user_id = Column(Integer, default=None)
    branchID = Column(Integer, default=None)

class CartDetail(Base):
    id = Column(Integer, index=True, primary_key= True)
    productName = Column(String(500), default = None)
    price = Column(Integer, default = None)   
    quantity = Column(Integer, default = None)
    totalPrice = Column(Integer, default = None)
    user_id = Column(Integer, default=None)
    branchID = Column(Integer, default=None)

class Review(Base):
    id = Column(Integer, index=True, primary_key= True)
    review = Column(String(1000), default = None)   
    name = Column(String(500), default = None)
    email = Column(String(500), default = None)
    rating = Column(String(500), default = None)
    product_id = Column(Integer, default = None)
    user_id = Column(Integer, default=None)
    branchID = Column(Integer, default=None)

class OrderDetails(Base):
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, default=None)
    payment_stat = Column(Boolean, default=False)
    productName = Column(String(100), default=None)
    amount = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey("user.id"))
    branchID = Column(Integer, default=None)
    owner = relationship("User", back_populates="orders")
