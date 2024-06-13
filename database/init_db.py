from database import engine, Base, session
from models.books import Book
from models.author import Author
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text

# Add the author_id column if it doesn't exist
def add_author_id_column():
    with engine.connect() as conn:
        try:
            conn.execute(text("ALTER TABLE books ADD COLUMN author_id INTEGER REFERENCES authors(id)"))
            print("Added author_id column to books table.")
        except OperationalError as e:
            if "duplicate column name" in str(e):
                print("author_id column already exists.")
            else:
                raise

# Create the database tables
Base.metadata.create_all(engine)

# Add the new column to the existing table
add_author_id_column()

# Adding sample authors and books
authors_books = {
    "Harper Lee": ["To Kill a Mockingbird"],
    "George Orwell": ["1984"],
    "F. Scott Fitzgerald": ["The Great Gatsby"],
    "J.D. Salinger": ["The Catcher in the Rye"],
    "J.R.R. Tolkien": ["The Hobbit", "The Lord of the Rings"],
    "Ray Bradbury": ["Fahrenheit 451"],
    "Herman Melville": ["Moby Dick"],
    "Jane Austen": ["Pride and Prejudice"],
    "Leo Tolstoy": ["War and Peace"],
    "Fyodor Dostoevsky": ["Crime and Punishment", "The Brothers Karamazov"],
    "Aldous Huxley": ["Brave New World"],
    "Homer": ["The Odyssey"],
    "Dante Alighieri": ["The Divine Comedy"],
    "Miguel de Cervantes": ["Don Quixote"],
    "George R.R. Martin": ["A Song of Ice and Fire"],
    "Mark Twain": ["The Adventures of Huckleberry Finn"],
    "J.K. Rowling": ["Harry Potter series"],
    "E.L. James": ["Fifty Shades of Grey", "Fifty Shades Darker", "Fifty Shades Freed"],
    "Dan Brown": ["The Da Vinci Code"],
    "Paulo Coelho": ["The Alchemist"],
}

for author_name, books in authors_books.items():
    author = Author.create(author_name)
    for book_title in books:
        Book.create(book_title, author.id)

print("Database initialized with sample authors and books!")
