from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')

    @staticmethod
    def create(title, author_id):
        new_book = Book(title=title, author_id=author_id)
        session.add(new_book)
        session.commit()
        return new_book

    @staticmethod
    def delete(book_id):
        book = session.query(Book).filter_by(id=book_id).first()
        if book:
            session.delete(book)
            session.commit()
            return True
        return False

    @staticmethod
    def get_all():
        return session.query(Book).all()

    @staticmethod
    def find_by_id(book_id):
        return session.query(Book).filter_by(id=book_id).first()
