from sqlalchemy import (create_engine, Column, 
                        Integer, String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create a database
engine = create_engine('sqlite:///books.db',echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# books.db
class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    published_date = Column("Published", Date)
    price = Column("Price", Integer)
    
    def __repr__(self):
        return f"Title: {self.title} | Author: {self.author} | Published: {self.published_date} | Price: {self.price}"
    

# create model
    # title, author, date published, price