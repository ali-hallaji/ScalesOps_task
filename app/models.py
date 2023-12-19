from sqlalchemy import Column, Integer, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

# create a declarative base instance
Base = declarative_base()


# define a class for the image model that inherits from Base
class ImageModel(Base):
    # specify the name of the table in the database
    __tablename__ = 'images'
    # define the primary key column for the table
    id = Column(Integer, primary_key=True)
    # define the column for storing the image data
    image_data = Column(LargeBinary)
