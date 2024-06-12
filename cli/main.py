import click
from models import Book

@click.group()
def cli():
    pass

@click.command()
def list_books():
    """Displays a list of all books in the library."""
    books = Book.get_all()
    for book in books:
        print(f"{book.id}: {book.title} by {book.author}")

@click.command()
@click.option('--title', prompt='Title', help='The title of the book')
@click.option('--author', prompt='Author', help='The author of the book')
def add_book(title, author):
    """Allows the user to add a new book to the library."""
    Book.create(title, author)
    print(f"Book '{title}' by {author} added.")

@click.command()
@click.option('--id', prompt='Book ID', help='The ID of the book to delete')
def delete_book(id):
    """Enables the user to delete a book from the library by its ID."""
    if Book.delete(id):
        print(f"Book with ID {id} deleted.")
    else:
        print(f"Book with ID {id} not found.")

@click.command()
@click.option('--id', prompt='Book ID', help='The ID of the book to find')
def find_book(id):
    """Allows the user to find a book by its ID."""
    book = Book.find_by_id(id)
    if book:
        print(f"Book found: {book.id}: {book.title} by {book.author}")
    else:
        print(f"Book with ID {id} not found.")

# Add commands to the cli group
cli.add_command(list_books)
cli.add_command(add_book)
cli.add_command(delete_book)
cli.add_command(find_book)

if __name__ == '__main__':
    cli()
