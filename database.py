from anyio import connect_tcp
import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

SQLALCHEMY_DATABE_URL = "sqlite:///./database.db"

engine = sql.create_engine(SQLALCHEMY_DATABE_URL, connect_args = {"check_same_thread":False})