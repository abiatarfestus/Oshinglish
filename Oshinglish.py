from tkinter import*
import sqlite3

mainWindow = Tk()
mainWindow.title("Oshinglish Dictionary First Edition")
mainWindow.configure(background = "#0970d2")
mainWindow.geometry("700x700+300+0")
variable = StringVar(mainWindow)
variable.set("one") # default value


nameWithLogo = Label(mainWindow, text = "Oshinglish Dictionary First Edition", font = "Times 28", background = "#982901")
nameWithLogo.grid()

#options = OptionMenu(mainWindow, variable = 3)
#options.grid(columnspan = 3, row = 5, sticky = W)
options = OptionMenu(mainWindow, variable, "one", "two", "three")
options.grid()

infoMenu = Menubutton(mainWindow)
infoMenu.grid(column = 3, row = 5)

searchBox = Entry(mainWindow)
searchBox.grid(columnspan = 11, row = 6, sticky = W)

findButton = Button(mainWindow, text = "Find")
findButton.grid(column = 9, row = 6)

listLabel = Label(mainWindow, text = "List of words appears here", background = "white", height = 40)
listLabel.grid()


#definitionSpace = Label(mainWindow, text = "Definitions appear here")
#definitionSpace.grid(columnspan = 15, rowspan = 15)


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
            english_definition TEXT NOT NULL,
            english_example TEXT NOT NULL,
            oshindonga_definition TEXT NOT NULL,
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
            english_definition TEXT NOT NULL,
            english_example TEXT NOT NULL,
            oshindonga_definition TEXT NOT NULL,
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

#Functions
#Add an English word
def add_english_word(word):
    #Remember to LOWERCASE word
    with conn:
        c.execute("INSERT INTO english (word) VALUES (?)", (word,))

#Add Oshindonga word
def add_oshindonga_word(word, engId):
    with conn:
        c.execute("INSERT INTO oshindonga (word, english_id) VALUES (?,?)", (word, engId))

#Add a noun definiton
def add_noun_definition(engId, oshId, engdef, engEx, oshDef, oshEx):
    with conn:
        c.execute("""INSERT INTO nouns (english_id, oshindonga_id, english_definition,
                    english_example, oshindonga_definition, oshindonga_example) 
                    VALUES (?,?,?,?,?,?)""", (engId, oshId, engdef, engEx, oshDef, oshEx))

#Add a verb definition
def add_verb_definition(engId, oshId, engDef, engEx, oshDef, oshEx):
    with conn:
        c.execute("""INSERT INTO verbs (english_id, oshindonga_id, english_definition,
                    english_example, oshindonga_definition, oshindonga_example) 
                    VALUES (?,?,?,?,?,?)""", (engId, oshId, engDef, engEx, oshDef, oshEx))

#Get a definition
def find_english_word(word): #Returns input value/argument for find_definition if word found
    c.execute("SELECT id FROM english WHERE word=(?)", (word,))
    result = c.fetchone()
    if result == None:
        return "Word not found"
    else:
        return result[0] #Retuns id (english_id)

def find_oshindonga_word(word): #Returns input value/argument for find_definition if word found
    c.execute("SELECT english_id FROM oshindonga WHERE word=(?)", (word,))
    result = c.fetchone()
    if result == None:
        return "Oshitya inashi monika"
    else:
        return result[0]    #Returns english_id, which should be passed to find definition

#Search part of speech tables for definitions
def find_definition(wordID):
    definitions = []
    tables = ["noun", "verb"]
    definition = []
    squery = ""
    for table in tables:
        squery ="SELECT * FROM {} WHERE english_id=(?)".format(table + "s") #Assign select statement to squery (for dynamic table selectio)
        c.execute(squery, (wordID,))
        definition = c.fetchall()
        if definition != []:
            definitions.extend([table.capitalize()+":"]) #Adds Part of speech before definitons
            #definitions.extend([table.capitalize()+":", definition])
            for i in definition[0]: #Takes tuple elements and add them to definitions
                definitions.append(i)
    if definitions == []:
        return "No definition found"
    return definitions

def remove_oshindonga_word(id):
    with conn:
        c.execute("DELETE FROM oshindonga WHERE id = (?)", (id,))

def remove_english_word(id):
    with conn:
        c.execute("DELETE FROM english WHERE id = (?)", (id,))

def remove_definition(table, id):
    with conn:
        squery ="SELECT * FROM {} WHERE english_id = (?)".format(table)
        c.execute(squery, (id,))

#Update/modify words and definitions
def update_english_word(word, id):
    with conn:
        c.execute("UPDATE english SET word = (?) WHERE id = (?)", (word, id))

def update_oshindonga_word(word, id):
    with conn:
        c.execute("UPDATE oshindonga SET word = (?) WHERE id = (?)", (word, id))

def update_definition(table, engId, oshId, engDef, engEx, oshDef, oshEx, id):
    with conn:
        uquery = """UPDATE {} SET english_id = (?), oshindonga_id = (?), english_definition = (?), 
        english_example = (?), oshindonga_definition = (?), oshindonga_example = (?) WHERE id = (?)""".format(table)
        c.execute(uquery, (engId, oshId, engDef, engEx, oshDef, oshEx, id))

words = ["lightining", "scar", "ball", "person", "play", "phone", "car", "speak", "cup", "rain"]
iitya = ["olwaadhi", "oshiyadhi", "etanga", "omuntu", "dhana", "ongodhi", "ohauto", "popya", "ekopi", "omvula"]

#Testing adding words to database
'''
#adding words to English table
for word in words:
    add_english_word(word)

#Adding words to Oshindonga table
engId = 1
for word in iitya:
    add_oshindonga_word(word, engId)
    engId += 1'''
#add_oshindonga_word("oshinyandwa", 5)

#remove_oshindonga_word(1)
'''
english = c.execute("SELECT * FROM english")
print(c.fetchall())
oshindonga = c.execute("SELECT * FROM oshindonga")
print(c.fetchall())'''

#add_noun_definition(5, 5, "A drama played by actors", "They performed a play by Shakespeare", 
                    #"Oshinyandwa tshi li kombinga yokahokololo", "Oya dhana oshinyandwa oshiwanawa")

#add_verb_definition(5, 5, "To perform a drama or sport", "They played a good game", 
                    #"Oku dhana uudhano nenge oshinyandwa", "Oya dhana uudhano uuwanawa")

#Testing search word in English table
#print(get_definition_by_english_word("played"))

#Testing search definitions in parts of speech tables
#print(find_definition(5))
#print(find_oshindonga_word("oshinyandua"))
#remove_definition("nouns", 7)
#update_english_word("lightning", 1)
#update_definition("verbs", 5, 5, "To take part in a game action", "They played a good game", 
                    #"Oku dhana uudhano nenge oshinyandwa", "Oya dhana uudhano uuwanawa", 1)

conn.close()

mainWindow.mainloop()
