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

def get_user_by_email(db: orm.Session, email:str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: orm.Session, user: schemas.UserCreate):
    hashed_password = user.password + "this_is_not_secure"
    db_user = models.User(email= user.email, hashed_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_school_by_email(db: orm.Session, email:str):
    return db.query(models.School).filter(models.School.email == email).first()

def create_school(db: orm.Session, school: schemas.School):
    #hashed_password = user.password + "this_is_not_secure"
    db_school = models.User(email= school.email, school_name = school.school_name)#hashed_password = hashed_password)
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school