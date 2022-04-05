import sqlalchemy
import LibraryModulesSQL

from sqlalchemy import create_engine
from sqlalchemy import text
engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)

# search all book titles and their genre
# with engine.connect() as conn:
#     result = conn.execute(text(f"SELECT * FROM books"))
#     for row in result:
#         print(row.book_title)
#         print(row.genre)

# keyword search
# with engine.connect() as conn:
#     user_search = input('Enter a keyword to search for within the library: ')
#     result = conn.execute(text(f"SELECT * FROM books"))
#     print(f"Here are your return searches for {user_search}")
#     for row in result:
#         if user_search in row.book_title:
#             print(row)

# with engine.connect() as conn:
#     user_search = input('Enter a keyword to search for within the library: ')
#     result = conn.execute(text(f"SELECT * FROM books"))
#     print(f"Here are your return searches for {user_search}")
#     for row in result:
#         if user_search in row.book_title:
#             print(row)

# USER SEARCH AND BORROW
LibraryModulesSQL.welcome_to_library()
start = input("Would you like to use the library search engine? Enter y for Yes or q to quit: ")
while start.lower() == "y":
    search_outcome = LibraryModulesSQL.get_user_search_results()
    if len(search_outcome) == 0:
        print("Sorry your search found no results.")
    else:
        LibraryModulesSQL.request_borrow_book()
    start = input("Would you like to search again? Enter y for yes or q to quit: ")

