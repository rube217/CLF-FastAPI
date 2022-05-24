from __future__ import unicode_literals
from email.policy import default
from operator import index
import sqlalchemy as sql
import datetime as dt
import database as db
from typing import Optional
import pydantic




class User(db.Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    identification_number: sql.Column(sql.String, unique = True, index = True)
    first_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    email = sql.Column(sql.String, unique = True, index = True)
    hashed_password = sql.Column(sql.String)
    is_active = sql.Column(sql.Boolean, default = True)
    type_id = sql.Column(sql.String)
    weight = sql.Column(sql.Float)
    is_teacher = sql.Column(sql.Boolean, default = False)
    level = sql.Column(sql.Integer)
    contact_number = sql.Column(sql.String)
    contact_person = sql.Column(sql.String)
    school = sql.Column(sql.Integer, sql.ForeignKey("schools.id"))
    birth_date = sql.Column(sql.Date, default = dt.date.today())

    #events = sql.orm.relationship("Event", back_populates = "competitors")

class School(db.Base):
    __tablename__ = "schools"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    school_name = sql.Column(sql.String)
    email = sql.Column(sql.String, unique = True, index = True)
    teacher_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    address = sql.Column(sql.String)
    contact_number_school = sql.Column(sql.String)


class Event(db.Base):
    __tablename__ = "events"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    date_event = sql.Column(sql.Date, default = dt.date.today())
    cost = sql.Column(sql.Integer)

    #category = sql.Column(sql.Integer)
    competitors = sql.orm.relationship("User", back_populates = "events")

class Items(db.Base):
    __tablename__ = "items"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    item_name = sql.Column(sql.String)
    item_description = sql.Column(sql.String)
    item_cost = sql.Column(sql.Integer)

class Categories(db.Base):
    __tablename__ = "categories"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    events = sql.Column(sql.Integer, sql.ForeignKey("events.id"))
    is_group = sql.Column(sql.Boolean, default = False)
    min_level = sql.Column(sql.Integer)
    max_level = sql.Column(sql.Integer)
    min_weight = sql.Column(sql.Integer)
    max_weight = sql.Column(sql.Integer)
    form_category = sql.Column(sql.Boolean, default = True)

class Boughts(db.Base):
    __tablename__ = "boughts"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    item = sql.Column(sql.Integer, sql.ForeignKey("items.id"))
    buyer = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    date = sql.Column(sql.Date)

class Competitors(db.Base):
    __tablename__ = "competitors"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    id_event = sql.Column(sql.Integer, sql.ForeignKey("events.id"))
    id_competitor = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    id_category = sql.Column(sql.Integer, sql.ForeignKey("categories.id"))