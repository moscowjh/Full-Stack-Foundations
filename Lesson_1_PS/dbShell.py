from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import association_table, Base, Puppy, Shelter, PuppyData, Adoptions

engine = create_engine('sqlite:///puppyshelter.db', echo = True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

print('Your SQLAlchemy session is ready to go! Access it with `session`')
