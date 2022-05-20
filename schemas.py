import datetime as dt
from optparse import Option
from turtle import title
import pydantic
from typing import List, Optional


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

class User(UserBase):
    id: int
    type_id_document: str
    weight: Optional[float] = 0.0
    is_active: bool
    is_teacher: Optional[bool] = False
    level = int
    contact_number: Optional[str] = ''
    contact_person: Optional[str] = ''
    school: int
    age: int

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



# class Person(BaseModel):
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


# class School(BaseModel):
#     teacher_id: int
#     school_id: int
#     school_name: str
#     address: str
#     contact_number_school: str

# class Event(BaseModel):
#     event_id: int
#     category : int
#     date_event: date
#     cost: Optional[int]=0

# #class boughts(BaseModel):
# #    date_bought:date
# #    bought_id:int
# #    item:int

# class Items(BaseModel):
#     item_id:int
#     item_name:str
#     item_description: Optional[str]=None
#     item_cost: int

# class Categories(BaseModel):
#     category_id:int
#     is_group: Optional[bool] = False
#     allowed_levels: Optional[list] = []
#     allowed_weight: Optional[list] = [] 
#     form_category: Optional[str] = None
