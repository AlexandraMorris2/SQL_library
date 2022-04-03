#import sqlalchemy
#print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+pymysql://root:password@localhost/Library", echo= False, future= True)
with engine.connect() as conn:
    print("hello")


#with engine.connect() as conn:
    #conn.execute(text("CREATE TABLE some_table(x int, y int)"))
    #conn.execute(
       # text("INSERT INTO some_table (x,y) VALUES(:x, :y)"),
       # [{"x":1, "y":1}, {"x":4, "y":4}]
   # )
    #conn.commit()

#with engine.connect() as conn:
    #conn.execute(
       # text("INSERT INTO author(author_id,first_name, last_name) VALUES(:author_id, :first_name, :last_name)"),
       # [{"author_id":4, "first_name": "Stephen", "last_name": "King"}, {"author_id":5, "first_name": "Enid", "last_name": "Blyton"}]
    #)
   # conn.commit()

with engine.connect() as conn:
    conn.execute(
         text("INSERT INTO users(user_id, library_card, user_name, user_age, fine_date, fine_date2, fine_cost, fine_cost2, fine_outstanding, blocked) VALUES(:user_id, :library_card, :user_name, :user_age, :fine_date, :fine_date2, :fine_cost, :fine_cost2, :fine_outstanding, :blocked)"),
         [{"user_id": 4, "library_card": 485156, "user_name": "Harry Potter", "user_age": 16, "fine_date": "2022-01-10", "fine_date2": "2022-01-15", "fine_cost": 5, "fine_cost2": 2, "fine_outstanding": "no", "blocked": "no"},
          {"user_id": 5, "library_card": 489587, "user_name": "Ron Weasley", "user_age": 16, "fine_date": "2022-01-11", "fine_date2": "2022-02-17", "fine_cost": 6, "fine_cost2": 2, "fine_outstanding": "yes", "blocked": "yes"},
          {"user_id": 6, "library_card": 845712, "user_name": "Hermione Grainger", "user_age": 16, "fine_date": "2022-02-18", "fine_date2": "2022-03-02", "fine_cost": 2, "fine_cost2": 3, "fine_outstanding": "no", "blocked": "no"},
          {"user_id": 7, "library_card": 982365, "user_name": "Lord Voldermot", "user_age": 43, "fine_date": "2022-03-12", "fine_date2": "2022-04-01", "fine_cost": 5, "fine_cost2": 5, "fine_outstanding": "yes", "blocked": "yes"},
          {"user_id": 8, "library_card": 741258, "user_name": "Severus Snape", "user_age": 57, "fine_date": "2022-03-01", "fine_date2": "2022-04-01", "fine_cost": 4, "fine_cost2": 2, "fine_outstanding": "no", "blocked": "no"},
          {"user_id": 9, "library_card": 968235, "user_name": "Draco Malfoy", "user_age": 17, "fine_date": "2022-02-19", "fine_date2": "2022-03-04", "fine_cost": 7, "fine_cost2": 2, "fine_outstanding": "yes", "blocked": "yes"},
          {"user_id": 10, "library_card": 985632, "user_name": "Neville Longbottom", "user_age": 16, "fine_date": "2022-01-25", "fine_date2": "2022-02-28", "fine_cost": 4, "fine_cost2": 5, "fine_outstanding": "no", "blocked": "no"},
          {"user_id": 11, "library_card": 120452, "user_name": "Rubeus Hagrid", "user_age": 62, "fine_date": "2022-01-18", "fine_date2": "2022-03-28", "fine_cost": 5, "fine_cost2": 3, "fine_outstanding": "no", "blocked": "no"},
          {"user_id": 12, "library_card": 851472, "user_name": "Sirius Black", "user_age": 58, "fine_date": "2022-03-15", "fine_date2": "2022-03-30", "fine_cost": 10, "fine_cost2": 10, "fine_outstanding": "no", "blocked": "no"},]
    )
    conn.commit()
