from sqlalchemy import Column, Date, Integer, ForeignKey, SmallInteger, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.users.models import User

class Person(Base):
    __tablename__ = 'people_person'
    id = Column(Integer, primary_key=True)
    created_by_user_id = Column(Integer, ForeignKey('users_user.id'))
    created_by_user = relationship("User", primaryjoin=created_by_user_id == User.id)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    birthdate = Column(Date)
    address = Column(String)
    city = Column(String)
    postalcode = Column(Integer)
    state = Column(String)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.address = address
        self.city = city
        self.postalcode = postalcode
        self.state = state
        self.created_by_user = created_by_user
