import datetime as dt
from optparse import Option
from turtle import title
import pydantic
from typing import List, Optional
import datetime as dt


class UserBase(pydantic.BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    first_name: str = pydantic.Field(
        ...,
        min_length=1,
        max_length=75
    )
    last_name: str = pydantic.Field(
        ...,
        min_length=1,
        max_length=75
    )
    birth_date: Optional[dt.date] = dt.date.today()

class User(UserBase):
    id: int
    identification_number: str
    type_id: str
    weight: Optional[float] = 0.0
    is_active: bool
    is_teacher: Optional[bool] = False
    level = int
    contact_number: Optional[str] = ''
    contact_person: Optional[str] = ''
    school: int
    #events: int #List[Event] = []

    class Config:
        orm_mode = True


class School(pydantic.BaseModel):
    teacher_id: int
    id: int
    school_name: str = pydantic.Field(
        ...,
        min_length=1,
        max_length=100
    )
    address: Optional[str] =''
    contact_number_school: Optional[str] = ''
    email: Optional[str] = ''
    
    class Config:
        orm_mode = True


class Items(pydantic.BaseModel):
    id:int
    item_name:str
    item_description: Optional[str]=None
    item_cost: int

    class Config:
        orm_mode = True


class Categories(pydantic.BaseModel):
    id:int
    is_group: Optional[bool] = False
    min_level: Optional[int] = 0
    max_level: Optional[int] = 12
    min_weight: Optional[float] = 0.0 
    max_weight: Optional[float] = 0.0 
    form_category: Optional[str] = None

    class Config:
        orm_mode = True

class Event(pydantic.BaseModel):
    id: int
    category : List[Categories] = []
    date_event: Optional[dt.date] = dt.date.today()
    cost: Optional[int]=0
    #competitor: List[User] = []

    class Config:
        orm_mode = True


class Boughts(pydantic.BaseModel):
   date:dt.date
   id:int
   item:int
   buyer:int

class Competitors(pydantic.BaseModel):
    id: int
    id_event: int
    id_competitor: int
    id_category: int

# class Person(pydantic.BaseModel):
#     first_name: str = Field(
#         ...,
#         min_length=1,           ## Se valida los atributos del modelo
#         max_length=75
#     )
#     last_name: str
#     age: int = Field(
#         gt = 0
#     )   
#     type_id_document: str
#     person_id: int
#     #birth_date: date
#     weight: Optional[float] = None
#     contact_person: Optional[str] = None
#     contact_number: str
#     level: int
#     is_teacher: Optional[bool] = False
#     school: int
#     email: str
    
#     class Config:
#         schema_extra = {
#             "Eduardo Polania": {
#                 "first_name":"Eduardo",
#                 "last_name":"Polania",
#                 "age":40,
#                 "type_id_document":"Cedula",
#                 "person_id":123456789,
#                 "weight": 75.9,
#                 "concact_person":"Javier",
#                 "level": 12,
#                 "is_teacher":True,
#                 "school":1,
#                 "email":"eduardo@gmail.com",
#             }
#         }


# class School(pydantic.BaseModel):
#     teacher_id: int
#     school_id: int
#     school_name: str
#     address: str
#     contact_number_school: str


