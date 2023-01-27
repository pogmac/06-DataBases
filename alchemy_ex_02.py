# sqlalchemy_ex_02.py
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

#engine = create_engine('sqlite:///database.db')
engine = create_engine('sqlite:///database.db', echo = True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('id', Integer, primary_key=True),
   Column('firstname', String),
   Column('lastname', String),
)

meta.create_all(engine)
#print(engine.table_names())


