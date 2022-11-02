from rich.console import Console
from rich.table import Table

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# Datenbank erzeugen
database = create_engine("sqlite:///ToDoList.db")
# Basisklasse für Klassen
Base = declarative_base()

# Verbindung zur Datenbank
Session = sessionmaker(bind=database)
# Offene Verbindung zur Datenbank
session = Session()

# Rich Konsole Initialisieren
console = Console()


class erledigte_Aufgaben(Base):
    __tablename__ = "erledigteAufgaben"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Aufgaben(Base):  
    __tablename__ = "Aufgaben"
    id = Column(Integer, primary_key=True)
    neue_Aufgabe = Column(String)

    # ForeignKeys
    erledigte_Aufgaben_id = Column(Integer, ForeignKey("erledigteAufgaben.id"))

    def __repr__(self) -> str:
        return f"{self.neue_Aufgabe}"


def initialisiere_Datenbank():
    Base.metadata.create_all(database)


def menue_anzeigen():
    MENU_TEXT = """
    Menu:
    - (A)dd a new Task
    - (D)elete a Task
    - (L)ist all Tasks
    - (E)xit
    """
    print(MENU_TEXT)


def menue_eingabe_input():
    menu_choice = input("Suche eine Option aus:")

    if menu_choice == "A":
        add_new_Tasks()
    elif menu_choice == "D":
        delete_a_Task()
    elif menu_choice == "L":
        list_all_Tasks()
    # elif menu_choice == "U":
    #     update_new_Task
    elif menu_choice == "E":
        exit(1)


def add_new_Tasks():
    print("Add a new Task:")
    neue_Aufgabe = input("Neue Aufgabe\t:")
    neue_Aufgabe = Aufgaben(neue_Aufgabe=neue_Aufgabe)

    database_add_Aufgaben(neue_Aufgabe)


def database_add_Aufgaben(neue_Aufgabe: Aufgaben):
    session.add(neue_Aufgabe)
    session.commit()


def list_all_Tasks():
    aufgaben = database_list_all_Tasks() 
    table = Table(show_header=True,  header_style="bold green")
    table.add_column("ID", style="dim")
    table.add_column("neue_Aufgabe")

    
    for aufgabe in aufgaben:  
        
        table.add_row(str(aufgabe.id), str(aufgabe.neue_Aufgabe))

    console.print(table)


def database_list_all_Tasks():
    return session.query(Aufgaben).all()


def delete_a_Task():
    task_id = int(input("Bitte gebe eine ID an:"))
    aufgabe = database_get_one_Task(task_id)
    console.print(f"Delete Task {aufgabe.neue_Aufgabe}", style="red")
    database_delete_a_Task(aufgabe)


def database_get_one_Task(task_id: int):
    return session.query(Aufgaben).get(task_id)


def database_delete_a_Task(aufgabe: Aufgaben):
    session.delete(aufgabe)
    session.commit()


if __name__ == "__main__":
    initialisiere_Datenbank()

    while True:
        menue_anzeigen()
        menue_eingabe_input()
