from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import select

# s = select([puppy])
# result = conn.execute(s)

puppies = session.query(Puppy).join(Shelter).order_by(Shelter.name)
for puppy in puppies:
    print(puppy.name, puppy.shelter.name)

# Exercise 2 - Queries
# 1. Query all of the puppies and return results in ascending alphabetical order

alpha = session.query(Puppy).order_by(Puppy.name).all()
for alpha in alpha:
    print alpha.name


# 2. Query all of the puppies that are less than 6 months old organized by youngest first

import datetime
six_mos_before = datetime.date.today()-datetime.timedelta(days=182)
youngones = session.query(Puppy).filter(Puppy.dateOfBirth > six_mos_before).\
            order_by(Puppy.dateOfBirth.desc()).all()
for i in youngones:
    print i.name, i.dateOfBirth

# 3. Query all puppies grouped by shelter in which they are staying

weight = session.query(Puppy).order_by(Puppy.weight).all()
for weight in weight:
    print weight.name, weight.weight

# 4. Query all puppies grouped by shelter in which they are staying

pbs = session.query(Puppy).order_by(Puppy.shelter_id).all()
for pbs in pbs:
    print pbs.name, pbs.shelter_id

# Exercise 4: create DB columns for maximum_capacity and current_occupancy
# Was unable to import sqlalchemy migrate.changeset, so instead reran the puppies.py and
# puppies_populate.py scripts.
# Determined puppy occupancy with a SQL query
# `select shelter_id, count(shelter_id) from puppy group by shelter_id;`
# then used SQLAlchemy at python command line to add totals to the database


# 5. Define function/query to calculate current_occupancy of shelters


def CheckIn (puppy.name, shelter.name):
    shelter = session.query(Shelter).filter_by(name = shelter.name).one():
    if shelter.current_occupancy >= shelter.maximum_capacity:
        print "Please enroll your puppy at another shelter."
# update puppy (entire record), update shelter.current_occupancy
    else:
        new_puppy = Puppy(name=puppy.name, gender="F",
                          shelter_id=puppy.shelter.name)
        session.add(Puppy)
        session.commit()
