import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import text


def welcome_to_library():
    print("""Welcome to Hogwarts library we specialise in magical books!
    """)

def get_user_search_results():
    search_results = []
    engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM books"))
        user_search = input('Enter a keyword relating to author, book title or genre: ')
        print(f"Here are the results that match your search: {user_search}")
        for row in result:
            if user_search in row.book_title or user_search in row.author or user_search in row.genre:
                search_results.append(row.book_id)
                print(f"Book ID {row.book_id} titled: {row.book_title} by {row.author} published in {row.year_published} categorised in genre {row.genre}")
                print(f"Is the book on loan? {row.on_loan}")
                print(f"Is the book reserved? {row.reserved}")
            else:
                pass
    return search_results


def check_if_book_available_to_borrow():
    book_number = input(f"Would you like to borrow a book? If so enter the book_id or press q to quit: ")
    engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT book_id, book_title, on_loan, reserved FROM books"))
        for row in result:
            if book_number in str(row.book_id):
                request_to_borrow_book(book_number)
                break
            elif book_number == str(row.book_id) and row.on_loan == "yes":
                print(f"Sorry, {row.book_title} is on loan already, maybe you could reserve it.")
                break
            elif book_number == str(row.book_id) and row.on_loan == "no" and row.reserved == "yes":
                print(f"Sorry, {row.book_title} is reserved for somebody else and will be held for them for 7 days.")
                break
            elif book_number != str(row.book_id):
                print(f"Book ID {book_number} does not exist")
                break

def request_to_borrow_book(book_id):
    engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)
    with engine.connect() as conn:
        result = conn.execute(
            text("""SELECT book_id, book_title, author, branch_number, on_loan, reserved, branch_address FROM books INNER JOIN branch
            ON books.branch_id = branch.branch_id""")
        )
        for row in result:
            if book_id == str(row.book_id):
                print(f"The book {row.book_title} by {row.author} is located at the {row.branch_address} branch.")
                if row.on_loan == "no" and row.reserved =="no":
                    library_card = input('Would you like to borrow it? press y for yes or press q to quit')
                    if library_card == "y":
                        make_book_on_loan_in_db(book_id)
                        print('All done. Happy Reading')
                    else:
                        print('Thank you for using the library, goodbye')
                else: print(f"Book is either on loan already or reserved, check back in one week")

def make_book_on_loan_in_db(book_number):
    engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)
    with engine.connect() as conn:
        result = conn.execute(
            text("""SELECT book_id, book_title, author, branch_number, on_loan, reserved, branch_address FROM books INNER JOIN branch
            ON books.branch_id = branch.branch_id"""))
        for row in result:
            if book_number == row.book_id:
                text(f"UPDATE books SET on_loan = 'yes' WHERE book_id = {row.book_id}")
                conn.commit()
                print("Mischief managed")
                print(row.book_id, row.on_loan)

# once got the matching ids working add the additional updates in make_book_on_loan_in_db (loan table, user history etc).
# add reserve function to work the same way

