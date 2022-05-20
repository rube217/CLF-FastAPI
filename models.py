from email.policy import default
import sqlalchemy as sql
import sqlalchemy.orm as orm
import database as db




class User(db.Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    first_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    email = sql.Column(sql.String, unique = True, index = True)
    hashed_password = sql.Column(sql.String)
    is_active = sql.Column(sql.Boolean, default = True)
    type_id_document = sql.Column(sql.String)
    weight = sql.Column(sql.Float)
    is_teacher = sql.Column(sql.Boolean, default = False)
    level = sql.Column(sql.Integer)
    contact_number = sql.Column(sql.String)
    contact_person = sql.Column(sql.String)
    school = sql.Column(sql.Integer, sql.ForeignKey("schools.id"))
    age = sql.Column(sql.Integer)

    posts = orm.relationship("Post", back_populates = "owner")
    
    
# class Post(db.Base):
#     __tablename__ = "posts"
#     id = sql.Column(sql.Integer,primary_key = True, index = True)
#     title = sql.Column(sql.String, index = True)
#     content = sql.Column(sql.String, index = True)
#     owner_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
#     date_created = sql.Column(sql.DateTime, default = dt.datetime.utcnow)
#     date_last_updated = sql.Column(sql.DateTime, default = dt.datetime.utcnow)

#     owner = orm.relationship("User", back_populates = "posts")

class School(db.Base):
    __tablename__ = "schools"
    id = sql.Column(sql.Integer, primary_key = True, index = True)
    school_name = sql.Column(sql.String)
    email = sql.Column(sql.String, unique = True, index = True)
    teacher_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    address = sql.Column(sql.String)
    contact_number_school = sql.Column(sql.String)