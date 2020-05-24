#from tkinter import*
import sqlite3

conn = sqlite3.connect('dictionary.db')

c = conn.cursor()

"""The syntax to create a foreign key using a CREATE TABLE statement in SQLite is:
CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY,
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER,
    FOREIGN KEY (group_id)
    REFERENCES supplier_groups (group_id) 
       ON UPDATE CASCADE
       ON DELETE CASCADE
);"""

c.execute("""PRAGMA foreign_keys = ON;
            CREATE TABLE IF NOT EXISTS english (
            id INTEGER UNIQUE AUTOINCREMENT,
            word TEXT PRIMARY KEY);

            CREATE TABLE IF NOT EXISTS oshindonga (
            id INTEGER PRIMARY KEY AUTOINCREMENT,            
            word TEXT NOT NULL,
            english_word TEXT NOT NULL,
            FOREIGN KEY (english_word)
            REFERENCES english (word)
                ON UPDATE CASCADE
                ON DELETE RESTRICT);

            CREATE TABLE IF NOT EXISTS nouns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            english_id TEXT NOT NULL,
            oshindonga_id INTEGER NOT NULL,
            english_definion TEXT NOT NULL,
            english_example TEXT NOT NULL,
            oshindonga_definion TEXT NOT NULL,
            oshindonga_example TEXT NOT NULL,
            FOREIGN KEY (english_id)
            REFERENCES english (word)
                ON UPDATE CASCADE
                ON DELETE RESTRICT),
            FOREIGN KEY (oshindonga_id)
            REFERENCES oshindonga (id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT));

            CREATE TABLE IF NOT EXISTS verbs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            english_id TEXT NOT NULL,
            oshindonga_id INTEGER NOT NULL,
            english_definion TEXT NOT NULL,
            english_example TEXT NOT NULL,
            oshindonga_definion TEXT NOT NULL,
            oshindonga_example TEXT NOT NULL,
            FOREIGN KEY (english_id)
            REFERENCES english (word)
                ON UPDATE CASCADE
                ON DELETE RESTRICT),
            FOREIGN KEY (oshindonga_id)
            REFERENCES oshindonga (id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT))
            """)



def insert_engWord(word):

    with conn:

        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})





def get_emps_by_name(lastname):

    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})

    return c.fetchall()





def update_pay(emp, pay):

    with conn:

        c.execute("""UPDATE employees SET pay = :pay

                    WHERE first = :first AND last = :last""",

                  {'first': emp.first, 'last': emp.last, 'pay': pay})





def remove_emp(emp):

    with conn:

        c.execute("DELETE from employees WHERE first = :first AND last = :last",

                  {'first': emp.first, 'last': emp.last})


conn.close()





""" root = Tk()
root.title("Oshinglish Dictionary First Edition")
root.configure(background = "#0970d2")
root.geometry("700x700+300+0")
variable = StringVar(root)
variable.set("one") # default value


nameWithLogo = Label(root, text = "Oshinglish Dictionary First Edition", font = "Times 28", background = "#982901")
nameWithLogo.grid()

#options = OptionMenu(root, variable = 3)
#options.grid(columnspan = 3, row = 5, sticky = W)
options = OptionMenu(root, variable, "one", "two", "three")
options.grid()

infoMenu = Menubutton(root)
infoMenu.grid(column = 3, row = 5)

searchBox = Entry(root)
searchBox.grid(columnspan = 11, row = 6, sticky = W)

findButton = Button(root, text = "Find")
findButton.grid(column = 9, row = 6)

listLabel = Label(root, text = "List of words appears here", background = "white", height = 40)
listLabel.grid()


#definitionSpace = Label(root, text = "Definitions appear here")
#definitionSpace.grid(columnspan = 15, rowspan = 15)



root.mainloop() """

'''
            CREATE TABLE IF NOT EXISTS parts_of_speech (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            english TEXT NOT NULL,
            oshindonga TEXT NOT NULL);'''