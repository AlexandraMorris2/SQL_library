import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import text


def welcome_to_library():
    print("""Welcome to ... library we specialise in magical books!
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


def request_borrow_book():
    book_number = input(f"Would you like to borrow a book? If so enter the book_id or press q to quit: ")
    engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT book_id, book_title, on_loan, reserved FROM books"))
        for row in result:
            if book_number == str(row.book_id) and row.on_loan == "no":
                borrow_book(book_number)
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

def borrow_book(book_id):
    engine = create_engine("mysql+pymysql://root:password@localhost/library", echo=False, future=True)
    with engine.connect() as conn:
        result = conn.execute(
            text("""SELECT book_id, book_title, author, branch_number, on_loan, reserved, branch_address FROM books INNER JOIN branch
            ON books.branch_id = branch.branch_id""")
        )
        for row in result:
            if book_id in str(row.book_id):
                print(f"The book {row.book_title} by {row.author} is located at the {row.branch_address} branch.")
                if row.on_loan == "no" and row.reserved =="no":
                    user_input = input('Would you like to borrow it?')
                    if user_input == "y":
                        user_card_number = input("Please enter your library card: ")
                        with engine.connect() as conn:
                            result = conn.execute(
                                text(f"UPDATE books SET on_loan = 'yes' WHERE book_id = {row.book_id}")
                            )
                            #update isn't working and need to also update loan and user_id tables too, do you have to run a seperate join?
                            print('All done. Happy Reading')
                    else: print('Ok, goodbye')

                else: print(f"Book is either on loan already or reserved, check back in one week")

                    #     "INSERT INTO books (book_id, dewy_decimal_number, isbn, book_title, author, genre, year_published, branch_id, copy_number, on_loan, reserved) VALUES (:book_id, :dewy_decimal_number, :isbn, :book_title, :author, :genre, :year_published, :branch_id, :copy_number, :on_loan, :reserved)"),
                    #     [{'book_id': 4, 'dewy_decimal_number': 393.333, 'isbn': 'st7689899',
                    #       'book_title': 'The Standard Book of Spells Grade 1', 'author'





