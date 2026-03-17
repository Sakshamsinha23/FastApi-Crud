from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine,Base
import models, schemas, crud
from typing import List

Base.metadata.create_all(bind=engine)

app=FastAPI()

#dependency with db

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#1.endpoints

@app.post("/employees", response_model=schemas.EmployeeOut)

def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

#2.get all employees

@app.get("/employees", response_model=List[schemas.EmployeeOut])

def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_employee(db=db)

#3.get employee by id
@app.get("/employees/{emp_id}",response_model=schemas.EmployeeOut)

def get_employee_id(emp_id:int, db: Session = Depends(get_db)):
    db_employee=crud.get_employee_by_id(db=db, emp_id=emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#4.update employee
@app.put("/employees/{emp_id}",response_model=schemas.EmployeeOut)

def update_employee(emp_id:int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee=crud.update_employee(db=db, emp_id=emp_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#5 delete employee

@app.delete("/employees/{emp_id}",response_model=schemas.EmployeeOut)

def delete_employee(emp_id:int, db : Session = Depends(get_db)):
    db_employee=crud.delete_employee(db=db, emp_id=emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    # return db_employee
    return {"message": "Employee deleted successfully"}