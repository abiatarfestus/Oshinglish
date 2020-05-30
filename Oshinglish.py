import tkinter as tk
#from tkinter import ttk
import sqlite3

mainWindow = tk.Tk()
mainWindow.title("Oshinglish Dictionary First Edition")
#mainWindow.configure(background = "#0970d2")
mainWindow.geometry("900x600+300+0")
#variable = StringVar(mainWindow)
#variable.set("one") # default value


#VARIABLES
#Main window variables??
inputLang = tk.StringVar() #variable for input language radiobuttons
#inputLang.set("English")
#FRAMES
mainFrame = tk.Frame(mainWindow, relief=tk.RAISED, borderwidth=3)
#mainFrame['padding'] = 5
#mainFrame['borderwidth'] = 2
mainFrame.grid(column=0, row=0, padx=5, pady=5)

topFrame = tk.Frame(mainFrame, relief=tk.RAISED, borderwidth=2)
#mainFrame["padding"] = 5
#topFrame['borderwidth'] = 2
topFrame.grid(column=0, row=0)

leftFrame = tk.Frame(mainFrame, relief=tk.RAISED, borderwidth=2)
#mainFrame["padding"] = 5
#leftFrame['borderwidth'] = 2
leftFrame.grid(column=0, row=1, padx=20, pady=20)

rightFrame = tk.Frame(mainFrame, relief=tk.RAISED, borderwidth=2)
#mainFrame["padding"] = 5
#rightFrame['borderwidth'] = 2
rightFrame.grid(column=1, row=1)

bottomFrame = tk.Frame(mainFrame, relief=tk.RAISED, borderwidth=2)
#mainFrame["padding"] = 5
#bottomFrame['borderwidth'] = 2
bottomFrame.grid(column=0, row=2)

#LABELS
#Main window labels
logoLbl = tk.Label(topFrame, text = "Logo placeholder", background="blue", height=5)
logoLbl.grid(column=0, row=0, sticky="w")
#mainWindow.rowconfigure(1, weight=0, minsize=25) #Inserts an empty row btwn the 2 labels (NB: minsize is in pixels)
titleLbl = tk.Label(topFrame, text = "Oshinglish Dictionary First Edition", background="white")
titleLbl.grid(column=1, row=0, sticky="nsew")
searchLbl = tk.Label(leftFrame, text = "Search word definition", background="white", height=2)
searchLbl.grid(column=0, row=0, sticky="nsew", pady=2)
contributeLbl = tk.Label(rightFrame, text = "Contribute to the dictionary", background="white", height=2)
contributeLbl.grid(column=0, row=0, sticky="nsew", pady=2)
inputLangLbl = tk.Label(leftFrame, text = "Choose input language", background="white", height=2)
inputLangLbl.grid(column=0, row=1, sticky="nsew", pady=2)
wordLbl = tk.Label(leftFrame, text = "Word/Oshitya", background="white")
wordLbl.grid(column=0, row=3, sticky="nsew")
definitionLbl = tk.Label(bottomFrame, text = "The definition wil appear here", background="white", width=100)
definitionLbl.grid(column=0, row=0, sticky="nsew")

#BUTTONS
#Main window buttons
#deleteDefBtn = tk.Button(rightFrame, text = "Delete definition from database")
#deleteDefBtn.grid(column=9, row=2)
searchBtn = tk.Button(leftFrame, text = "Search")
searchBtn.grid(column=1, row=2)
addEngBtn = tk.Button(rightFrame, text = "Add/update English word", height=5)
addEngBtn.grid(column=0, row=1, sticky="nsew")
addOshBtn = tk.Button(rightFrame, text = "Add/Update Oshindonga word")
addOshBtn.grid(column=1, row=1, sticky="nsew")
addDefBtn = tk.Button(rightFrame, text = "Add/Update definition")
addDefBtn.grid(column=2, row=1, sticky="nsew")
deleteWordBtn = tk.Button(rightFrame, text = "Delete word from database")
deleteWordBtn.grid(column=3, row=1)

#RADIOBUTTONS
#Main window radiobuttons
englishRbtn = tk.Radiobutton(leftFrame, text="English", variable=inputLang, value="English")
englishRbtn.grid(column=1, row=1, sticky="nsew")
oshindongaRbtn = tk.Radiobutton(leftFrame, text="Oshindonga", variable=inputLang, value="Oshindonga")
oshindongaRbtn.grid(column=2, row=1, sticky="nsew")

#ENTRY WIDGETS
#Main window entry widgets
searchEbx = tk.Entry(leftFrame)
searchEbx.grid(column=0, row=2, sticky="nsew", pady=2)

#TEXT WIDGETS
#OPTION MENUES
#Main window option menues



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
