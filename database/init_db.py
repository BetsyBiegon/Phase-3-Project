from database import engine, Base
from models.book import Book
from sqlalchemy.orm import sessionmaker

# Create the database tables
Base.metadata.create_all(engine)

# Initialize the session
Session = sessionmaker(bind=engine)
session = Session()

# Adding sample books
books = [
    Book(title="To Kill a Mockingbird", author="Harper Lee"),
    Book(title="1984", author="George Orwell"),
    Book(title="The Great Gatsby", author="F. Scott Fitzgerald"),
    Book(title="The Catcher in the Rye", author="J.D. Salinger"),
    Book(title="The Hobbit", author="J.R.R. Tolkien"),
    Book(title="Fahrenheit 451", author="Ray Bradbury"),
    Book(title="Moby Dick", author="Herman Melville"),
    Book(title="Pride and Prejudice", author="Jane Austen"),
    Book(title="War and Peace", author="Leo Tolstoy"),
    Book(title="Crime and Punishment", author="Fyodor Dostoevsky"),
    Book(title="The Brothers Karamazov", author="Fyodor Dostoevsky"),
    Book(title="Brave New World", author="Aldous Huxley"),
    Book(title="The Odyssey", author="Homer"),
    Book(title="The Divine Comedy", author="Dante Alighieri"),
    Book(title="Don Quixote", author="Miguel de Cervantes")
]

# Add the books to the session and commit
session.add_all(books)
session.commit()

print("Database initialized with sample books!")
