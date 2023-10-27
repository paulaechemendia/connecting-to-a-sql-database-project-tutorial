import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import sqlite3 as sq 

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
con = sq.connect("SOS.db")

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
# con.execute("""CREATE TABLE publishers(
#     publisher_id INT NOT NULL,
#     name VARCHAR(255) NOT NULL,
#     PRIMARY KEY(publisher_id)
# )""")
#con.commit()
# con.execute("""CREATE TABLE authors(
#     author_id INT NOT NULL,
#     first_name VARCHAR(100) NOT NULL,
#     middle_name VARCHAR(50) NULL,
#     last_name VARCHAR(100) NULL,
#     PRIMARY KEY(author_id)
# )""")
# con.commit()

# con.execute("""CREATE TABLE books(
#     book_id INT NOT NULL,
#     title VARCHAR(255) NOT NULL,
#     total_pages INT NULL,
#     rating DECIMAL(4, 2) NULL,
#     isbn VARCHAR(13) NULL,
#     published_date DATE,
#     publisher_id INT NULL,
#     PRIMARY KEY(book_id),
#     CONSTRAINT fk_publisher FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
# )""")

# con.execute("""CREATE TABLE book_authors (
#     book_id INT NOT NULL,
#     author_id INT NOT NULL,
#     PRIMARY KEY(book_id, author_id),
#     CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES books(book_id) ON DELETE CASCADE,
#     CONSTRAINT fk_author FOREIGN KEY(author_id) REFERENCES authors(author_id) ON DELETE CASCADE
# )""")
# con.commit()

# con.execute("""INSERT INTO publishers(publisher_id, name) VALUES (1, 'O Reilly Media')""")
# con.commit()
# con.execute("""INSERT INTO publishers(publisher_id, name) VALUES (2, 'A Book Apart')""")
# con.execute("""INSERT INTO publishers(publisher_id, name) VALUES (3, 'A K PETERS')""")
# con.commit()
con.execute("""DROP TABLE publishers""")
con.commit()
# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function
