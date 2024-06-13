## Phase-3-Project
   # Librart Application

## Description

This is a simple library management system implemented in Python. It allows users to manage books through a command-line interface (CLI). 

## Functionalities

### Manage Books
- **Add a Book:** Allows the user to add a new book by entering its title and author
- **Delete a Book:** Enables the user to delete a book by its ID.
- **List All Books:** Displays all books in the library.
- **Find a Book by ID:** Allows the user to find a book by its ID.

## Commands

- `list-books`: List all books
- `add-book`: Add a new book
- `delete-book`: Delete a book by ID
- `find-book`: Find a book by ID

## Usage
Clone the repository

cd to the project folder

Install the dependencies by running;
`pipenv install`

Activate the project's virtualenv by running;
`pipenv shell`

Initialize the database by running;  
`python database/init_db.py`

Run the application by running;
`python cli/main.py`

To list all the books in the library;
`python cli/main.py list-books`

To add a new book;
`python cli/main.py add-book`

To delete a book by ID;
`python cli/main.py delete-book`

To find a book by ID;
`python cli/main.py find-book`


   ##### ~by Betsy Biegon~

