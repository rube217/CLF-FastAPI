#Python
from datetime import date, datetime
from optparse import Option, OptionConflictError
from typing import Optional
from enum import Enum
#Pydantic
from pydantic import BaseModel,  Field
#FastAPI
from fastapi import FastAPI, Query, Body, Path

#from fastapi import Body
#from fastapi import Query


app = FastAPI()

#Models

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,           ## Se valida los atributos del modelo
        max_length=75
    )
    last_name: str
    age: int = Field(
        gt = 0
    )   
    type_id_document: str
    person_id: int
    #birth_date: date
    weight: Optional[float] = None
    contact_person: Optional[str] = None
    contact_number: str
    level: int
    is_teacher: Optional[bool] = False
    school: int
    email: str
    
    class Config:
        schema_extra = {
            "Eduardo Polania": {
                "first_name":"Eduardo",
                "last_name":"Polania",
                "age":40,
                "type_id_document":"Cedula",
                "person_id":123456789,
                "weight": 75.9,
                "concact_person":"Javier",
                "level": 12,
                "is_teacher":True,
                "school":1,
                "email":"eduardo@gmail.com",
            }
        }


class School(BaseModel):
    teacher_id: int
    school_id: int
    school_name: str
    address: str
    contact_number_school: str

class Event(BaseModel):
    event_id: int
    category : int
    date_event: date
    cost: Optional[int]=0

#class boughts(BaseModel):
#    date_bought:date
#    bought_id:int
#    item:int

class Items(BaseModel):
    item_id:int
    item_name:str
    item_description: Optional[str]=None
    item_cost: int

class Categories(BaseModel):
    category_id:int
    is_group: Optional[bool] = False
    allowed_levels: Optional[list] = []
    allowed_weight: Optional[list] = [] 
    form_category: Optional[str] = None




@app.get("/")

def home():
    return {"Hello":"World"} 

# Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

@app.post("/items/new")
def create_item(item: Items = Body(...)):
    return item

@app.post("/events/new")
def create_event(event: Event = Body(...)):
    return event

@app.post("/schools/new")
def create_school(school: School = Body(...)):
    return school

@app.post("/category/new")
def create_category(category: Categories = Body(...)):
    return category

# Validaciones de los Query Parameters

@app.get("/person/detail")
def show_person(
    first_name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=75,
        title= "Person First Name"
        ),
    last_name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=75,
        title="Person's Last Name"
        ),
    age: Optional[int] = Query(
        None,
        ge=1,
        title="Person Age"
        ),
    type_id_document: Optional[str] = Query(
        None,
        min_length=1,
        max_length=75,
        title="Type of Identification document"
        ),
    person_id: Optional[int] = Query(
        None,
        ge=1,
        le = 5000000000,
        title="Person Id"
        ),
    #birth_date: Optional[date] = Query(
    #    None,
        #min_length=1,
        #max_length=75,
    #    title="Person Birth Date"
    #    )
):
    return{person_id:[first_name,last_name, age,  type_id_document+str(person_id) ]}

#Validaciones Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path
    (...,
    gt=0,
    title="Person Id as key for show"
    )
):
    return {person_id:"It exist!"}

#Validaciones Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person Id",
        description="this is the person Id",
        gt = 0
    ),
    person: Person = Body(...)
):
    return person
    