from sqlalchemy import create_engine

engine = create_engine('sqlite:///library.db')
with engine.connect() as conn:
    conn.execute("ALTER TABLE books ADD COLUMN author_id INTEGER REFERENCES authors(id)")

print("Table 'books' altered successfully to add 'author_id' column.")
