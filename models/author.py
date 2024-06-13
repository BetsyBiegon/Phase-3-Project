from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base, session

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship('Book', back_populates='author')

    @staticmethod
    def create(name):
        existing_author = session.query(Author).filter_by(name=name).first()
        if existing_author:
            return existing_author
        else:
            new_author = Author(name=name)
            session.add(new_author)
            session.commit()
            return new_author

    @staticmethod
    def get_all():
        return session.query(Author).all()

    @staticmethod
    def find_by_id(author_id):
        return session.query(Author).filter_by(id=author_id).first()
