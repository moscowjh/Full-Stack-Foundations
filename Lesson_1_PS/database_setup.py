import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)
    city = Column(String(80), nullable=False)
    state = Column(String(20), nullable=False)
    zipCode = Column(String(10))
    website = Column(String, nullable=True)
    maximum_capacity = Column(Integer, nullable=True)
    current_occupancy = Column(Integer, nullable=True)


class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable=False)
    dateOfBirth = Column(Date)
    picture = Column(String, nullable=True)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))


engine = create_engine('sqlite:///puppyshelter.db')


Base.metadata.create_all(engine)
