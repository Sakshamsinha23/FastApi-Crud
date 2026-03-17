from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Employee(Base):
    __tablename__ = "emp"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String, index=True)
    email=Column(String, index=True, unique=True)