import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite:///todo.db'

engine  = _sql.create_engine(DATABASE_URL)

Base = declarative_base()