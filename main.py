#Python
from datetime import date, datetime
from optparse import Option, OptionConflictError
from typing import Optional
from enum import Enum
#Pydantic
from pydantic import BaseModel,  Field
#FastAPI
import fastapi, sqlalchemy.orm as orm #, Query, Body, Path

from services import get_user_by_email

import services, schemas
#from fastapi import Body
#from fastapi import Query


app = fastapi.FastAPI()

services.create_database()

@app.get("/")
def home():
    return "Aqui va el FrontEnd!!!"

@app.post("/users/new",response_model=schemas.User)

def create_user(user: schemas.UserCreate, db: orm.Session = fastapi.Depends(services.get_db)):
    db_user = services.get_user_by_email(db = db, email=user.email)
    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="woops the email is in use")
    return services.create_user(db=db, user=user)


@app.post("/schools/new",response_model=schemas.School)

def create_school(school: schemas.School, db: orm.Session = fastapi.Depends(services.get_db)):
    db_school = services.get_school_by_email(db = db, email=school.email)
    if db_school:
        raise fastapi.HTTPException(status_code=400, detail="woops the email is in use")
    return services.create_school(db=db, school=school)



#Models




# @app.get("/")

# def home():
#     return {"Hello":"World"} 

# # Request and Response Body

# @app.post("/person/new")
# def create_person(person: Person = Body(...)):
#     return person

# @app.post("/items/new")
# def create_item(item: Items = Body(...)):
#     return item

# @app.post("/events/new")
# def create_event(event: Event = Body(...)):
#     return event

# @app.post("/schools/new")
# def create_school(school: School = Body(...)):
#     return school

# @app.post("/category/new")
# def create_category(category: Categories = Body(...)):
#     return category

# # Validaciones de los Query Parameters

# @app.get("/person/detail")
# def show_person(
#     first_name: Optional[str] = Query(
#         None,
#         min_length=1,
#         max_length=75,
#         title= "Person First Name"
#         ),
#     last_name: Optional[str] = Query(
#         None,
#         min_length=1,
#         max_length=75,
#         title="Person's Last Name"
#         ),
#     age: Optional[int] = Query(
#         None,
#         ge=1,
#         title="Person Age"
#         ),
#     type_id_document: Optional[str] = Query(
#         None,
#         min_length=1,
#         max_length=75,
#         title="Type of Identification document"
#         ),
#     person_id: Optional[int] = Query(
#         None,
#         ge=1,
#         le = 5000000000,
#         title="Person Id"
#         ),
#     #birth_date: Optional[date] = Query(
#     #    None,
#         #min_length=1,
#         #max_length=75,
#     #    title="Person Birth Date"
#     #    )
# ):
#     return{person_id:[first_name,last_name, age,  type_id_document+str(person_id) ]}

# #Validaciones Path Parameters

# @app.get("/person/detail/{person_id}")
# def show_person(
#     person_id: int = Path
#     (...,
#     gt=0,
#     title="Person Id as key for show"
#     )
# ):
#     return {person_id:"It exist!"}

# #Validaciones Request Body

# @app.put("/person/{person_id}")
# def update_person(
#     person_id: int = Path(
#         ...,
#         title="Person Id",
#         description="this is the person Id",
#         gt = 0
#     ),
#     person: Person = Body(...)
# ):
#     return person
    