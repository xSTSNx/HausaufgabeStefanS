from ast import Delete
from rich.console import Console
from rich.table import Table

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker


# # # ###########################################
# # Do not touch!
# # Database Connection stuff!
# Erzeugen einer neuen Datenbank Engine
database = create_engine("sqlite:///friendbook.db")
# Basisklasse für Klassen
Base = declarative_base()

# Öffne Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()

# Rich Initialization
console = Console()
# # # ###########################################


class Language(Base): 
    __tablename__ = "languages"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Friend(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

    # Foreignkeys
    language_id = Column(Integer, ForeignKey("languages.id"))

    def __repr__(self) -> str:
        return f"<{self.last_name}, {self.first_name}>"


def initialize_database():
    """
    Initializes the database and creates all tables.

    See more here: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """
    Base.metadata.create_all(database)


def show_menu():
    """
    Displays a menu.
    """

    MENU_TEXT = """
    Menu: 
    - (A)dd new Friend
    - (L)ist all Friends
    - (E)xit
    - (D)elete
    - (U)pdate
    """
    print(MENU_TEXT)


def get_users_menu_input():
    menu_choice = input("Choose menue option: ")

    if menu_choice == "A":
        add_new_friend()
    elif menu_choice == "E":
        exit(0)
    elif menu_choice == "L":
        list_all_friends()
    elif menu_choice == "D":
        delete_friend()
    elif menu_choice == "U":
        update_friend()
        
    

def add_new_friend():
    """
    Asks the user for the information about the new friend. 
    Adds the friend to the database.
    """
    print("Einen neuen Freund hinzufügen")
    first_name = input("First name\t:")
    last_name = input("Last name\t:")
    new_friend = Friend(first_name=first_name, last_name=last_name)
    database_add_friend(new_friend)

def delete_friend(): 
    to_delete_id = int(input("id to delete?"))
    session.query(Friend).filter_by(id = to_delete_id).delete() 
    session.commit()
    
def update_friend():
    # zu updatende ID Benutzer
    # first und last name Abfrage
    # updaten in der Datenbank
    # committen
     user_to_update = int(input("id to update?"))
     first_name = input("First name\t:")
     last_name = input("Last name\t:")
     session.query(Friend).filter_by(id = user_to_update).update({Friend.last_name: last_name, Friend.first_name: first_name})
     session.commit()
     
  


def list_all_friends():
    friends = database_get_all_friends()
    table = Table(show_header=True, header_style="bold green")
    table.add_column("ID", style="dim")
    table.add_column("First Name")
    table.add_column("Last Name")
    
    for friend in friends:
        table.add_row(str(friend.id), friend.first_name, friend.last_name)

    console.print(table)


def database_add_friend(friend: Friend):
    """
    Database command to add a new friend.

    ORM = Object Relational Mapper
    """
    session.add(friend)
    session.commit()


def database_get_all_friends():
    """
    Database command to get all friends.

    `all_friends = session.query(Friend).all()` is a query call made with the sqlalchemy ORM. 
    The SQL query that is made is: `SELECT * FROM friends;`

    Alternative to this with raw sql:
    `all_friends_raw = session.execute("SELECT * FROM friends;").fetchall()`
    """
    return session.query(Friend).all()


# # # ###########################################
# # # Main
# # # ###########################################
if __name__ == "__main__":
    initialize_database()

    while True:
        show_menu()
        get_users_menu_input()


