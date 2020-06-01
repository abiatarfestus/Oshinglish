import tkinter as tk
from tkinter import ttk
#import ttkthemes
from ttkthemes import ThemedTk
import sqlite3

mainWindow =  ThemedTk(theme="arc") #tk.Tk()
mainWindow.title("Oshinglish Dictionary First Edition")
#mainWindow.configure(background = "#0970d2")
#mainWindow.geometry("900x600+300+0")
engWindow = tk.Toplevel(mainWindow)
engWindow.title("Add/Update English word")
engWindow.resizable(tk.FALSE,tk.FALSE)

#THEMES & STYLE
#theme = ttk.Style()
#print(theme.theme_names()) #Prints theme names
#print(theme.theme_use()) #Prints theme in use
#theme.theme_use('winnative') #Changes theme in use

#Configuring column and row resizability
mainWindow.columnconfigure(0, weight=1)
mainWindow.rowconfigure(0, weight=1)

#VARIABLES
#Main window variables
inputLang = tk.StringVar() #variable for input language radiobuttons
#inputLang.set("English")
logo = tk.PhotoImage(file='Logo.gif')

#New English window variables
newEng = tk.StringVar()

#FRAMES
#Main window frames
mainFrame = ttk.Frame(mainWindow, relief='raised', borderwidth=3)
mainFrame.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')
#Configuring column and row resizability
mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure((0,1), weight=1)
mainFrame.rowconfigure(2, weight=100)

topFrame = ttk.Frame(mainFrame, borderwidth=2)
topFrame.grid(column=0, row=0, sticky='nesw')
#Configuring column and row resizability
topFrame.columnconfigure(1, weight=1)
#topFrame.rowconfigure(0, weight=1)

midFrame = ttk.Frame(mainFrame, borderwidth=2)
midFrame.grid(column=0, row=1, sticky='nesw')
#Configuring column and row resizability
midFrame.columnconfigure((0,1), weight=1)
midFrame.rowconfigure(0, weight=1)

leftFrame = ttk.Frame(midFrame, borderwidth=2)
leftFrame.grid(column=0, row=0, sticky='nesw')
#Configuring column and row resizability
leftFrame.columnconfigure(0, weight=1, minsize=80)
leftFrame.rowconfigure((0,1,2), weight=1)

rightFrame = ttk.Frame(midFrame, borderwidth=2)
rightFrame.grid(column=1, row=0, sticky='nesw')
#Configuring column and row resizability
rightFrame.columnconfigure((0,1,2,3), weight=1, minsize=80)
#rightFrame.rowconfigure((0,1), weight=1)

bottomFrame = ttk.Frame(mainFrame, borderwidth=2)
bottomFrame.grid(column=0, row=2, sticky='nesw')
#Configuring column and row resizability
bottomFrame.columnconfigure(0, weight=1)
bottomFrame.rowconfigure((1), weight=1)

#Engish word frames
engMainFrame = ttk.Frame(engWindow, borderwidth=3)
engMainFrame.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')

#LABELS
#Main window labels
logoLbl = ttk.Label(topFrame, image = logo)
logoLbl.grid(column=0, row=0, sticky="w")
#mainWindow.rowconfigure(1, weight=0, minsize=25) #Inserts an empty row btwn the 2 labels (NB: minsize is in pixels)
titleLbl = ttk.Label(topFrame, text = "Oshinglish Dictionary First Edition", background="white")
titleLbl.grid(column=1, row=0, padx=5, sticky="nsew")
searchLbl = ttk.Label(leftFrame, text = "Search word definition", background="white")
searchLbl.grid(column=0, row=0, sticky="nsew", pady=2)
contributeLbl = ttk.Label(rightFrame, text = "Contribute to the dictionary", background="white")
contributeLbl.grid(column=0, columnspan=3, row=0, sticky="nsew", pady=2)
inputLangLbl = ttk.Label(leftFrame, text = "Choose input language", background="white")
inputLangLbl.grid(column=0, row=1, sticky="nsew", pady=2)
wordLbl = ttk.Label(bottomFrame, text = "Word/Oshitya", background="white")
wordLbl.grid(column=0, row=0, sticky="w")
definitionLbl = ttk.Label(bottomFrame, text = "The definition wil appear here", background="white", relief='sunken')
definitionLbl.grid(column=0, row=1, sticky="nsew")

#English window labels
newEngTitleLbl = ttk.Label(engMainFrame, text = "Add or update an English word", anchor=tk.CENTER, background="white")
newEngTitleLbl.grid(column=0, columnspan=3, row=0, padx=5, sticky="nsew")
newEngLbl = ttk.Label(engMainFrame, text = "Enter new word:", background="white")
newEngLbl.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
newUpdateEngLbl = ttk.Label(engMainFrame, text = "Select New/Update:", background="white")
newUpdateEngLbl.grid(column=0, row=2, padx=5, pady=5, sticky="nsew")
newEngIdLbl = ttk.Label(engMainFrame, text = "ID of word to be update:", background="white")
newEngIdLbl.grid(column=0, row=3, padx=5, pady=5, sticky="nsew")
newEngDisplayLbl = ttk.Label(engMainFrame, text = "ID of word to be update:", background="white")
newEngDisplayLbl.grid(column=0, columnspan=3, row=4, padx=5, pady=5, sticky="nsew")

#BUTTONS
#Main window buttons
deleteDefBtn = ttk.Button(rightFrame, text = "Delete definition from database")
deleteDefBtn.grid(column=3, row=0, sticky="nsew")
searchBtn = ttk.Button(leftFrame, text = "Search")
searchBtn.grid(column=1, row=2)
addEngBtn = ttk.Button(rightFrame, text = "Add/update English word")
addEngBtn.grid(column=0, row=1, sticky="nsew")
addOshBtn = ttk.Button(rightFrame, text = "Add/Update Oshindonga word")
addOshBtn.grid(column=1, row=1, sticky="nsew")
addDefBtn = ttk.Button(rightFrame, text = "Add/Update definition")
addDefBtn.grid(column=2, row=1, sticky="nsew")
deleteWordBtn = ttk.Button(rightFrame, text = "Delete word from database")
deleteWordBtn.grid(column=3, row=1, sticky="nsew")

#English window buttons
newEngSaveBtn = ttk.Button(engMainFrame, text = "Save")
newEngSaveBtn.grid(column=0, row=5, padx=5, sticky="nsew")
newEngCancelBtn = ttk.Button(engMainFrame, text = "Cancel")
newEngCancelBtn.grid(column=1, row=5, padx=5, sticky="nsew")

#RADIOBUTTONS
#Main window radiobuttons
englishRbtn = ttk.Radiobutton(leftFrame, text="English", variable=inputLang, value="English")
englishRbtn.grid(column=1, row=1, sticky="nsew")
oshindongaRbtn = ttk.Radiobutton(leftFrame, text="Oshindonga", variable=inputLang, value="Oshindonga")
oshindongaRbtn.grid(column=2, row=1, sticky="nsew")

#English window radiobuttons
newEngRbtn = ttk.Radiobutton(engMainFrame, text="New", variable=newEng, value="New")
newEngRbtn.grid(column=1, row=2, sticky="nsew")
updateEngRbtn = ttk.Radiobutton(engMainFrame, text="Update", variable=newEng, value="Update")
updateEngRbtn.grid(column=2, row=2, sticky="nsew")

#ENTRY WIDGETS
#Main window entry widgets
searchEbx = ttk.Entry(leftFrame)
searchEbx.grid(column=0, row=2, sticky="nsew", pady=2)

#English window entry widgets
newEngEbx = ttk.Entry(engMainFrame)
newEngEbx.grid(column=1, row=1, sticky="nsew", pady=2)
updateEngEbx = ttk.Entry(engMainFrame)
updateEngEbx.grid(column=1, row=3, sticky="nsew", pady=2)

#TEXT WIDGETS
#OPTION MENUES
#Main window option menues
#SIZEGRIPs
ttk.Sizegrip(mainWindow).grid(column=999, row=999, sticky='se')

#SCROLLBARS
""" defScrb = ttk.Scrollbar(bottomFrame, orient=VERTICAL, command=definitionLbl.yview)
defScrb.grid(bottomFrame, column=1, row=1)
definitionLbl.configure(yscrollcommand=defScrb.set)
 """ #Labels are not scrollable

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
