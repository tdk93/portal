from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = 'mysql+mysqlconnector://akarora:akshay123@localhost:3306/portaldb'
engine = create_engine(db_url, echo=True)


# Define the SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    name = Column(String(255))

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert data
new_user = User(username='john_doe', name='John Doe')
session.add(new_user)
session.commit()

# Close the session
session.close()