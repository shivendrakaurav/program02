from sqlalchemy import create_engine, Column,Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , relationship
import pymysql


Base = declarative_base()

#delete function
class User(Base):
    __tablename__ = "person"

    id = Column("id",Integer,primary_key = True )
    username = Column("username", String, unique = True) 

engine = create_engine('mysql://root:shivendrasingh@localhost/football', echo = True)
Base.metadata.create_all(bind = engine )

Session = sessionmaker(bind = engine)

session = Session()

obj = session.query(User).get(2)
session.delete(obj)
session.commit()
session.close()



 #read operation
 
class User(Base):
    __tablename__ = "person"

    id = Column("id",Integer,primary_key = True )
    username = Column("username", String, unique = True) 

engine = create_engine('sqlite:///users.db', echo = True)
Base.metadata.create_all(bind = engine )

Session = sessionmaker(bind = engine)

session = Session()

users = session.query(User).all()
for user in users:
    print(f"id : {user.id} name : {user.username}")

session.close()





# create table operation and inserting value operation
class User(Base):
    __tablename__ = "person"

    id = Column("id",Integer,primary_key = True )
    username = Column("username", String, unique = True) 

engine = create_engine("username", String, unique = True)
Base.metadata.create_all(bind = engine )


# inserting value function

class User(Base):
    __tablename__ = "person"

    id = Column("id",Integer,primary_key = True )
    username = Column("username", String, unique = True) 

engine = create_engine("username", String, unique = True)
Base.metadata.create_all(bind = engine )

Session = sessionmaker(bind = engine)

session = Session()

user = User()
user.id = 0 
user


session.close()