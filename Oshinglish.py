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

c.executescript("""PRAGMA foreign_keys = ON;
            CREATE TABLE IF NOT EXISTS english (
            id INTEGER PRIMARY KEY,
            word TEXT NOT NULL UNIQUE);

            CREATE TABLE IF NOT EXISTS oshindonga (
            id INTEGER PRIMARY KEY,            
            word TEXT NOT NULL,
            english_id INTEGER NOT NULL,
            FOREIGN KEY (english_id)
            REFERENCES english (id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT);

            CREATE TABLE IF NOT EXISTS nouns (
            id INTEGER PRIMARY KEY,
            english_id TEXT NOT NULL,
            oshindonga_id INTEGER NOT NULL,
            english_definion TEXT NOT NULL,
            english_example TEXT NOT NULL,
            oshindonga_definion TEXT NOT NULL,
            oshindonga_example TEXT NOT NULL,
            FOREIGN KEY (english_id)
            REFERENCES english (id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            FOREIGN KEY (oshindonga_id)
            REFERENCES oshindonga (id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT);

            CREATE TABLE IF NOT EXISTS verbs (
            id INTEGER PRIMARY KEY,
            english_id TEXT NOT NULL,
            oshindonga_id INTEGER NOT NULL,
            english_definion TEXT NOT NULL,
            english_example TEXT NOT NULL,
            oshindonga_definion TEXT NOT NULL,
            oshindonga_example TEXT NOT NULL,
            FOREIGN KEY (english_id)
            REFERENCES english (id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT,
            FOREIGN KEY (oshindonga_id)
            REFERENCES oshindonga (id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT)
            """)

def insert_english_word(word):
    #Remember to LOWERCASE word
    with conn:
        c.execute("INSERT INTO english (word) VALUES (?)", (word,))

def insert_oshindonga_word(word, engId):
    with conn:
        c.execute("INSERT INTO oshindonga (word, english_id) VALUES (?,?)", (word, engId))

def insert_noun_definition(engId, oshId, engdef, engEx, oshDef, oshEx):
    with conn:
        c.execute("""INSERT INTO nouns (english_id, oshindonga_id, english_definition,
                    english_example, oshindonga_definition, oshindonga_example) 
                    VALUES (?,?,?,?,?,?)""", (engId, oshId, engdef, engEx, oshDef, oshEx))

def insert_verb_definition(engId, oshId, engdef, engEx, oshDef, oshEx):
    with conn:
        c.execute("""INSERT INTO nouns (english_id, oshindonga_id, english_definition,
                    english_example, oshindonga_definition, oshindonga_example) 
                    VALUES (?,?,?,?,?,?)""", (engId, oshId, engdef, engEx, oshDef, oshEx))

def get_definition_by_english_word(word):
    c.execute("SELECT * FROM nouns WHERE english_id=:english_id", {'english_id': word})
    return c.fetchall()

def remove_oshindonga_word(ref):
    with conn:
        c.execute("DELETE FROM oshindonga WHERE english_id = (?)", (ref,))

words = ["lightining", "scar", "ball", "person", "play", "phone", "car", "speak", "cup", "rain"]
iitya = ["olwaadhi", "oshiyadhi", "etanga", "omuntu", "dhana", "ongodhi", "ohauto", "popya", "ekopi", "omvula"]

'''engId = 1
for word in iitya:
    print(engId)
    insert_oshindonga_word(word, engId)
    engId += 1
    print("after")'''
#insert_oshindonga_word("oshinyandwa", 5)

#remove_oshindonga_word(1)

#english = c.execute("SELECT * FROM english")
#print(c.fetchall())
oshindonga = c.execute("SELECT * FROM oshindonga")
print(c.fetchall())

conn.close()


'''
def update_pay(emp, pay):

    with conn:

        c.execute("""UPDATE employees SET pay = :pay

                    WHERE first = :first AND last = :last""",

                  {'first': emp.first, 'last': emp.last, 'pay': pay})





def remove_emp(emp):

    with conn:

        c.execute("DELETE from employees WHERE first = :first AND last = :last",

                  {'first': emp.first, 'last': emp.last})

'''

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

'''
def insert_english_word(word):
    #Remember to LOWERCASE word
    with conn:
        c.execute("INSERT INTO english VALUES (:word)", {'word': word})

def insert_oshindonga_word(word, engId):
    with conn:
        c.execute("INSERT INTO oshindonga VALUES (:word, :english_id)", {'word': word, 'english_id': engId})

def insert_noun_definition(engId, oshId, engdef, engEx, oshDef, oshEx):
    with conn:
        c.execute("""INSERT INTO nouns VALUES (:english_id, :oshindonga_id, :english_definition,
                    :english_example, :oshindonga_definition, :oshindonga_example)""", 
                    {'english_id': engId, 'oshindonga_id': oshId, 'english_definition': engdef,
                    'english_example': engEx, 'oshindonga_definition': oshDef, 'oshindonga_example': oshEx})

def insert_verb_definition(engId, oshId, engdef, engEx, oshDef, oshEx):
    with conn:
        c.execute("""INSERT INTO verbs VALUES (:english_id, :oshindonga_id, :english_definition,
                    :english_example, :oshindonga_definition, :oshindonga_example)""", 
                    {'english_id': engId, 'oshindonga_id': oshId, 'english_definition': engdef,
                    'english_example': engEx, 'oshindonga_definition': oshDef, 'oshindonga_example': oshEx})
'''