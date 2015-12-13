from sqlalchemy import Table, Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('puppy_id', Integer, ForeignKey('puppy.id')),
    Column('adoptions_id', Integer, ForeignKey('adoptions.id'))
)


class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)
    maximum_capacity = Column(Integer, nullable=True)
    current_occupancy = Column(Integer, nullable=True)


class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable=False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    puppydata = relationship("PuppyData", uselist=False, backref="puppy")
    adoptions = relationship("Adoptions", backref="puppy", secondary=association_table)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))


class PuppyData(Base):
    __tablename__ = 'puppydata'
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)
    picture = Column(String)
    special_needs = Column(String(250))
    puppy_id = Column(Integer, ForeignKey('puppy.id'))


class Adoptions(Base):
    __tablename__ = 'adoptions'
    id = Column(Integer, primary_key=True)
    adopter_name = Column(String(250), nullable=False)


engine = create_engine('sqlite:///puppyshelter.db')


Base.metadata.create_all(engine)
