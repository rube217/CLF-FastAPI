from difflib import IS_CHARACTER_JUNK
import email
import fastapi
import sqlalchemy.orm as orm
import database, models, schemas

def create_database():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_by_email(db: orm.Session, email:str =""):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: orm.Session, user: schemas.User):
    hashed_password = user.password + "this_is_not_secure"
    db_user = models.User(
        email= user.email,
        hashed_password = hashed_password,
        first_name = user.first_name,
        birth_date = user.birth_date,
        identification = user.identification_number,
        level = user.level,
        type_id = user.type_id,
        weight = user.weight,
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def update_user(db: orm.Session, user: schemas.User):
#     db_user = models.User(
#         identification_number = user.identification_number,
#         type_id = user.type_id,
#         weight = user.weight,
#         is_active = user.is_active,

#         is_teacher = user.is_teacher,
#         level = user.level,
#         contact_number = user.contact_number,
#         contact_person = user.contact_person,
#         school = user.school)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def get_school_by_email(db: orm.Session, email:str):
    return db.query(models.School).filter(models.School.email == email).first()

def create_school(db: orm.Session, school: schemas.School):

    db_school = models.User(
        email = school.email,
        school_name = school.school_name,
        address = school.address,
        contact_school = school.contact_number_school,
        teacher = school.teacher_id)
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school