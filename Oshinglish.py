import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#import ttkthemes
from ttkthemes import ThemedTk
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
def add_english_word(word=""):
    #print("Entered add english word function")
    word = newEngEbx.get().lower()
    try:
        with conn:
            c.execute("INSERT INTO english (word) VALUES (?)", (word,))
        newEngEbx.delete(0, tk.END)
    except sqlite3.IntegrityError as error:
        messagebox.showerror(title="Duplicate found", message= "Error: " + word + " is already in the dictionary.")
    else:
        messagebox.showinfo(title="Word added", message= "The word '" +word+ "' was successfully added to the dictionary.")
        


#Add Oshindonga word
def add_oshindonga_word(word="", engId=0): #Remove arguments if not necessary
    word = newOshEbx.get().lower()
    engId = find_english_word(engWordEbx.get().lower())
    try:
        with conn:
            c.execute("INSERT INTO oshindonga (word, english_id) VALUES (?,?)", (word, engId))
        newOshEbx.delete(0, tk.END)
        engWordEbx.delete(0, tk.END)
        global displayEngId3
        displayEngId3 = ""      #Resets the the variable of English word ID to avoid inadvertent linking of Oshindonga words to wrong English words
    except sqlite3.IntegrityError as error:
        messagebox.showerror(title="Duplicate found", message= "Error: " + word + " is already in the dictionary.")
    else:
        messagebox.showinfo(title="Word added", message= "The word '" +word+ "' was successfully added to the dictionary.")

#Add a noun definiton
def add_noun_definition(engId, oshId, engdef, engEx, oshDef, oshEx):
    global engIdDef #To allow resetting of these labels and text boxes after successful submittion of definitions
    global oshIdDef
    global engDefTxt
    global engExampleTxt
    global oshDefTxt
    global oshExampleTxt
    try:
        with conn:
            c.execute("""INSERT INTO nouns (english_id, oshindonga_id, english_definition,
                        english_example, oshindonga_definition, oshindonga_example) 
                        VALUES (?,?,?,?,?,?)""", (engId, oshId, engdef, engEx, oshDef, oshEx))
            engIdDef.set("")
            oshIdDef.set("")
            engDefTxt.delete("1.0", tk.END)
            engExampleTxt.delete("1.0", tk.END)
            oshDefTxt.delete("1.0", tk.END)
            oshExampleTxt.delete("1.0", tk.END)
    except Exception as error:
        messagebox.showerror(title="Definition error", message= "An unexpected error occured: {0}\n\n Please check everything is fine and try again.\
             If the error persists, please report it to the developer.".format(error))
    else:
        messagebox.showinfo(title="Definition added", message= "Definition(s) successfully added to the dictionary.")

#Add a verb definition
def add_verb_definition(engId, oshId, engDef, engEx, oshDef, oshEx):
    with conn:
        c.execute("""INSERT INTO verbs (english_id, oshindonga_id, english_definition,
                    english_example, oshindonga_definition, oshindonga_example) 
                    VALUES (?,?,?,?,?,?)""", (engId, oshId, engDef, engEx, oshDef, oshEx))

#Get a definition
def find_english_word(word): #Returns input value/argument for find_definition if word found
    with conn:
        c.execute("SELECT id FROM english WHERE word=(?)", (word,))
        result = c.fetchone()
        if result == None:
            return "Word not found"
        else:
            return result[0] #Retuns id (english_id)

def find_oshindonga_word(word): #Returns input value/argument for find_definition if word found
    with conn:
        c.execute("SELECT english_id FROM oshindonga WHERE word=(?)", (word,))
        result = c.fetchone()
        if result == None:
            return "Oshitya inashi monika"
        else:
            return result[0]    #Returns english_id, which should be passed to find definition

def find_oshindonga_id(id): #Returns input value/argument for find_definition if word found
    with conn:
        c.execute("SELECT word FROM oshindonga WHERE id=(?)", (id,))
        result = c.fetchone()
        if result == None:
            return "Oshitya inashi monika"
        else:
            return result[0]    #Returns Oshidonga word, which should be passed to search_oshindonga_id()

#Search part of speech tables for definitions
def find_definition(wordID):
    with conn:
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
def update_english_word(word="", id=0):
    word = newEngEbx.get().lower()
    try: 
        id = int(updateEngEbx.get()) #Gets the value from the update entrybox, converts it to int (to match id data type)
    except ValueError:
         messagebox.showerror(title="English ID error", message= "No word ID or invalid ID was entered.\nEnter valid ID and try again.")
    else:
        with conn:
            c.execute("SELECT word FROM english WHERE id=(?)", (updateEngEbx.get(), id))
            result = c.fetchone()
            #print("Result: ", result)
            if result == None:
                return messagebox.showerror(title="ID not found", message= "The ID entered was not found in the database.\nEnter a valid ID and try again.")
            else:
                try:
                    with conn:
                        c.execute("UPDATE english SET word = (?) WHERE id = (?)", (word, id))
                    newEngEbx.delete(0, tk.END)
                    updateEngEbx.delete(0, tk.END)
                except sqlite3.IntegrityError as error:
                    messagebox.showerror(title="Duplicate found", message= "Error: " + word + " is already in the dictionary.")
                else:
                    messagebox.showinfo(title="Word updated", message= "The word was successfully updated.")


def update_oshindonga_word(word="", id=0):
    word = newOshEbx.get().lower()
    try: 
        id = int(oshWordIdEbx.get()) #Gets the value from the update entrybox, converts it to int (to match id data type)
    except ValueError:
         messagebox.showerror(title="Oshindonga ID error 1", message= "No word ID or invalid ID was entered. Enter valid ID, click search and try again if the word you wish to modify appears below.")
    else:
        with conn:
            c.execute("SELECT word FROM oshindonga WHERE id=(?)", (id,))
            result = c.fetchone()
            if result == None:      #This checks if the ID exists before trying to update the word
                return messagebox.showerror(title="Oshindonga ID error 2", message= "The ID entered was not found in the database.Enter valid ID, click search. If no word is returned, select New instead of Update.")
            else:
                with conn:
                    c.execute("UPDATE oshindonga SET word = (?) WHERE id = (?)", (word, id))
                newOshEbx.delete(0, tk.END)
                oshWordIdEbx.delete(0, tk.END)
                messagebox.showinfo(title="Word updated", message= "Word was successfully updated.")

def update_definition(table, engId, oshId, engDef, engEx, oshDef, oshEx, id):
    with conn:
        uquery = """UPDATE {} SET english_id = (?), oshindonga_id = (?), english_definition = (?), 
        english_example = (?), oshindonga_definition = (?), oshindonga_example = (?) WHERE id = (?)""".format(table)
        c.execute(uquery, (engId, oshId, engDef, engEx, oshDef, oshEx, id))

#conn.close()


def open_english_window():
    engWindow = tk.Toplevel(mainWindow)
    engWindow.title("Add/Update English word")
    engWindow.resizable(tk.FALSE,tk.FALSE)

    #VARIABLES
    engSelectedRbtn = tk.StringVar()
    #newEngDisplay = tk.StringVar()
    #newEngDisplay.set("ID of word to be update:::")

    #FUNCTIONS
    def select_new_or_update_english():     #Decides which function to run between new and update english based on the selected operation
        newOrUpdateEng = engSelectedRbtn.get()  #Checks option selected on radiobutton (new/update)
        #print(newOrUpdateEng)
        if newOrUpdateEng == "New":
            add_english_word()    #Calls the add_english_word function
        elif newOrUpdateEng == "Update":
            update_english_word() #Calls the update_english_word function
        else:
            return messagebox.showerror(title="Operation unknown", message="Operation not specified.\nSelect New or Update and search again.")
        engSelectedRbtn.set(None)
        return

    def search_if_english_word_exist(word=""):
        word = newEngEbx.get()
        searchResult = find_english_word(word)
        updateEngEbx.delete(0, tk.END) #Clears the textbox before inserting the returned ID/result
        updateEngEbx.insert(tk.INSERT, searchResult)
        #newEngDisplay.set("ID of word to be update: " + searchResult)
        #newEngDisplayLbl.configure(textvariable=newEngDisplay)

    #FRAMES
    engMainFrame = ttk.Frame(engWindow, borderwidth=3)
    engMainFrame.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')

    #LABELS
    newEngTitleLbl = ttk.Label(engMainFrame, text = "Add or update an English word", anchor=tk.CENTER, background="white")
    newEngTitleLbl.grid(column=0, columnspan=3, row=0, padx=5, sticky="nsew")
    newEngLbl = ttk.Label(engMainFrame, text = "Enter new word:", background="white")
    newEngLbl.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
    newUpdateEngLbl = ttk.Label(engMainFrame, text = "Select New/Update:", background="white")
    newUpdateEngLbl.grid(column=0, row=2, padx=5, pady=5, sticky="nsew")
    newEngIdLbl = ttk.Label(engMainFrame, text = "ID of word to be update:", background="white")
    newEngIdLbl.grid(column=0, row=3, padx=5, pady=5, sticky="nsew")
    #newEngDisplayLbl = ttk.Label(engMainFrame, textvariable=newEngDisplay, background="white")
    #newEngDisplayLbl.grid(column=0, columnspan=3, row=4, padx=5, pady=5, sticky="nsew")
    #BUTTONS
    newEngSearchBtn = ttk.Button(engMainFrame, text = "Search", command=search_if_english_word_exist)
    newEngSearchBtn.grid(column=2, row=1, padx=5, sticky="nsew")
    newEngSaveBtn = ttk.Button(engMainFrame, text = "Save", command=select_new_or_update_english)
    newEngSaveBtn.grid(column=0, row=5, padx=5, sticky="nsew")
    newEngCancelBtn = ttk.Button(engMainFrame, text = "Cancel")
    newEngCancelBtn.grid(column=1, row=5, padx=5, sticky="nsew")
    #RADIOBUTTONS
    newEngRbtn = ttk.Radiobutton(engMainFrame, text="New", variable=engSelectedRbtn, value="New")
    newEngRbtn.grid(column=1, row=2, sticky="nsew")
    updateEngRbtn = ttk.Radiobutton(engMainFrame, text="Update", variable=engSelectedRbtn, value="Update")
    updateEngRbtn.grid(column=2, row=2, sticky="nsew")

    #TEXT ENTRY for multi-line texts
    #ENTRY BOXES
    global newEngEbx
    global updateEngEbx
    newEngEbx = ttk.Entry(engMainFrame)
    newEngEbx.grid(column=1, row=1, sticky="nsew", pady=2)
    updateEngEbx = ttk.Entry(engMainFrame)
    updateEngEbx.grid(column=1, row=3, sticky="nsew", pady=2)

def open_oshindonga_window():
    oshWindow = tk.Toplevel(mainWindow)
    oshWindow.title("Add/Update Oshindonga word")
    oshWindow.resizable(tk.FALSE,tk.FALSE)

    #VARIABLES
    oshSelectedRbtn = tk.StringVar()
    displayEngId = tk.StringVar()
    displayOshWord = tk.StringVar()
    displayOshWord.set("No word to display")
    displayEngId1 = "The ID of "
    displayEngId2 = ""
    global displayEngId3
    displayEngId3 = ""
    displayEngId.set(displayEngId1 + '"' + displayEngId2 + '" is: ' + str(displayEngId3))

    def search_english_word(word=""):
        word = engWordEbx.get().lower() # Remember to search for other places to add .lower()
        displayEngId2 = word
        global displayEngId3
        displayEngId3 = find_english_word(word) #Returns the English word ID and assign it to this variable
        displayEngId.set(displayEngId1 + '"' + displayEngId2 + '" is: ' + str(displayEngId3))
        #print("EnglishID:", displayEngId3)

    def search_oshindonga_id(id=0): #Find oshindonga word to be update by ID
        try:
            id = int(oshWordIdEbx.get()) #Gets the value from the update entrybox, converts it to int (to match id data type)
        except ValueError:
            messagebox.showerror(title="Oshindonga ID error 3", message= "No word ID or invalid ID was entered. Enter valid ID, click search and try again if the word you wish to modify appears below.")
        else:
            oshUpdateWord = find_oshindonga_id(id) #Calls the function to find oshindonga word to be updated
            #print(oshUpdateWord)
            displayOshWord.set("The word to be updated is: " + oshUpdateWord)

    def select_new_or_update_oshindonga():     #Decides which function to run between new and update oshindonga based on the selected operation
        newOrUpdateOsh = oshSelectedRbtn.get()  #Gets option selected on radiobutton (new/update)
        global displayEngId3
        #print("EnglishID:", displayEngId3)
        if newOrUpdateOsh == "New":
            #print("EnglishID:", displayEngId3)
            if displayEngId3 == "" or displayEngId3 == "Word not found": #When user tries to save before searhing for the English word
                return messagebox.showerror(title="English ID error", message="English word ID is not provided. Search for the English word and try again. If the corresponding English word is not in the database, add it first.")
            else:
                add_oshindonga_word()    #Calls the add_oshindonga_word function
        elif newOrUpdateOsh == "Update":
            update_oshindonga_word() #Calls the update_oshindonga_word function
        else:
            return messagebox.showerror(title="Operation unknown", message="Operation not specified.\nSelect New or Update and search again.")
        oshSelectedRbtn.set(None)
        return

    #FRAMES
    oshMainFrame = ttk.Frame(oshWindow, borderwidth=3)
    oshMainFrame.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')

    #LABELS
    newOshTitleLbl = ttk.Label(oshMainFrame, text = "Add or update an Oshindonga word", anchor=tk.CENTER, background="white")
    newOshTitleLbl.grid(column=0, columnspan=3, row=0, padx=5, sticky="nsew")
    engWordIdLbl = ttk.Label(oshMainFrame, text = "Enter the corresponding English word:", background="white")
    engWordIdLbl.grid(column=0, row=1, padx=5, pady=5, sticky="nsew")
    engWordDisplayLbl = ttk.Label(oshMainFrame, textvariable = displayEngId, anchor=tk.CENTER, background="white")
    engWordDisplayLbl.grid(column=0, columnspan=3, row=2, padx=5, pady=5, sticky="nsew")
    newOshWordLbl = ttk.Label(oshMainFrame, text = "Enter new Oshindonga word:", background="white")
    newOshWordLbl.grid(column=0, row=3, padx=5, pady=5, sticky="nsew")
    newUpdateOshLbl = ttk.Label(oshMainFrame, text = "Select New/Update:", background="white")
    newUpdateOshLbl.grid(column=0, row=4, padx=5, pady=5, sticky="nsew")
    oshWordIdLbl = ttk.Label(oshMainFrame, text = "ID of word to be updated:", background="white")
    oshWordIdLbl.grid(column=0, row=5, padx=5, pady=5, sticky="nsew")
    oshWordDisplayLbl = ttk.Label(oshMainFrame, textvariable = displayOshWord, anchor=tk.CENTER, background="white")
    oshWordDisplayLbl.grid(column=0, columnspan=3, row=6, padx=5, pady=5, sticky="nsew")
    #BUTTONS
    searchEngIdBtn = ttk.Button(oshMainFrame, text = "Search", command=search_english_word)
    searchEngIdBtn.grid(column=2, row=1, padx=5, sticky="nsew")
    searchOshIdBtn = ttk.Button(oshMainFrame, text = "Search", command=search_oshindonga_id)
    searchOshIdBtn.grid(column=2, row=5, padx=5, sticky="nsew")
    newOshSaveBtn = ttk.Button(oshMainFrame, text = "Save", command=select_new_or_update_oshindonga)
    newOshSaveBtn.grid(column=0, row=7, padx=5, sticky="nsew")
    newOshCancelBtn = ttk.Button(oshMainFrame, text = "Cancel")
    newOshCancelBtn.grid(column=1, row=7, padx=5, sticky="nsew")
    #RADIOBUTTONS
    newOshRbtn = ttk.Radiobutton(oshMainFrame, text="New", variable=oshSelectedRbtn, value="New")
    newOshRbtn.grid(column=1, row=4, sticky="nsew")
    updateOshRbtn = ttk.Radiobutton(oshMainFrame, text="Update", variable=oshSelectedRbtn, value="Update")
    updateOshRbtn.grid(column=2, row=4, sticky="nsew")

    #TEXT ENTRY for multi-line texts
    #ENTRY BOXES
    global newOshEbx
    global engWordEbx
    global oshWordIdEbx
    engWordEbx = ttk.Entry(oshMainFrame)
    engWordEbx.grid(column=1, row=1, sticky="nsew", pady=2)
    newOshEbx = ttk.Entry(oshMainFrame)
    newOshEbx.grid(column=1, row=3, sticky="nsew", pady=2)
    oshWordIdEbx = ttk.Entry(oshMainFrame)
    oshWordIdEbx.grid(column=1, row=5, sticky="nsew", pady=2)

def open_definition_window():
    defWindow = tk.Toplevel(mainWindow)
    defWindow.title("Add/Update a definition")
    #Configuring column and row resizability
    defWindow.columnconfigure(0, weight=1)
    defWindow.rowconfigure(0, weight=1)

    #VARIABLES
    #Variables for English and Oshindonga word IDs and other labels
    global engIdDef
    global oshIdDef
    global engDefTxt
    global engExampleTxt
    global oshDefTxt
    global oshExampleTxt

    engIdDef = tk.StringVar()
    engIdDef.set("")
    oshIdDef = tk.StringVar()
    oshIdDef.set("")
    wordToDefine = tk.StringVar()
    wordToDefine.set("No word is selected fo definition")
    #Variables for the radiobuttons
    newOrUpdateDef = tk.StringVar()
    partsOfSpeech = tk.StringVar()
    

    def search_word_to_define(word=""): #Returns english and oshidonga ids and pass them to the respective labels' textvariables, also displays that the word was found the database, otherewise Word to found.
        word = oshWordDefEbx.get().lower()
        with conn:
            c.execute("SELECT english_id, id FROM oshindonga WHERE word=(?)", (word,))
            result = c.fetchone()
            print("Result: ", result)
            if result == None:
                wordToDefine.set("Word not found")
                engIdDef.set("")
                oshIdDef.set("")
                return 
            else:
                engIdDef.set(result[0])
                oshIdDef.set(result[1])
                wordFound = "The word "'"{0}"'" was found in the database. Continue defining it below.".format(word)
                wordToDefine.set(wordFound)
                return    

    def select_definition_category():
        if newOrUpdateDef == "New":
            messagebox.askyesno(title="Confirm part of speech", message="You're about to add a {0} definition of '{1}'.\
             Click yes to continue or no to correct the part of speech.".format(partsOfSpeech, oshWordDefEbx.get()))
            if partsOfSpeech == "Noun":
                add_noun_definition(engId=int(engIdDef), oshId=int(oshIdDef), engdef=engDefTxt.get(), engEx=engExampleTxt.get(), oshDef=oshDefTxt.get(), oshEx=oshExampleTxt.get())
            elif partsOfSpeech == "Verb":
                add_verb_definition(engId=int(engIdDef), oshId=int(oshIdDef), engdef=engDefTxt.get(), engEx=engExampleTxt.get(), oshDef=oshDefTxt.get(), oshEx=oshExampleTxt.get())
            else:
                return messagebox.showerror(title="Part of speech error", message="No part of speech is selected. Select part of speech of your definition and try again.")
        elif newOrUpdateDef == "Update":
            if partsOfSpeech == "Noun":
                updat_noun_definition(engId=int(engIdDef), oshId=int(oshIdDef), engdef=engDefTxt.get(), engEx=engExampleTxt.get(), oshDef=oshDefTxt.get(), oshEx=oshExampleTxt.get())
            elif partsOfSpeech == "Verb":
                update_verb_definition(engId=int(engIdDef), oshId=int(oshIdDef), engdef=engDefTxt.get(), engEx=engExampleTxt.get(), oshDef=oshDefTxt.get(), oshEx=oshExampleTxt.get())
            else:
                return messagebox.showerror(title="Part of speech error", message="No part of speech is selected. Select part of speech of your definition and try again.")


    #FRAMES
    defMainFrame = ttk.Frame(defWindow, relief='raised', borderwidth=3)
    defMainFrame.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')
    #Configuring column and row resizability
    defMainFrame.columnconfigure(0, weight=1)
    defMainFrame.rowconfigure((0,1,2), weight=1)

    defTopFrame = ttk.Frame(defMainFrame, borderwidth=2)
    defTopFrame.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')
    #Configuring column and row resizability
    defTopFrame.columnconfigure((0,1,2), weight=1)
    defTopFrame.rowconfigure((0,1,2,3), weight=1)

    defMidFrame = ttk.Frame(defMainFrame, borderwidth=2)
    defMidFrame.grid(column=0, row=1, padx=5, pady=5, sticky='nesw')
    #Configuring column and row resizability
    defMidFrame.columnconfigure((0,1,2), weight=1)
    defMidFrame.rowconfigure((0,1,2,3), weight=1)

    newUpdateFrame = ttk.Frame(defTopFrame, borderwidth=2)
    newUpdateFrame.grid(column=1, row=1, padx=5, pady=5, sticky='nesw')
    #Configuring column and row resizability
    newUpdateFrame.columnconfigure((0,1), weight=1)
    newUpdateFrame.rowconfigure(0, weight=1)

    partsOfSpeechFrame = ttk.Frame(defTopFrame, borderwidth=2)
    partsOfSpeechFrame.grid(column=1, row=2, padx=5, pady=5, sticky='nesw')
    #Configuring column and row resizability
    partsOfSpeechFrame.columnconfigure((0,1,2,3), weight=1)
    partsOfSpeechFrame.rowconfigure(0, weight=1)

    searchOshFrame = ttk.Frame(defTopFrame, borderwidth=2)
    searchOshFrame.grid(column=1, row=3, padx=5, pady=5, sticky='nesw')
    #Configuring column and row resizability
    searchOshFrame.columnconfigure((0,1), weight=1)
    searchOshFrame.rowconfigure(0, weight=1)

    defBottomFrame = ttk.Frame(defMainFrame, borderwidth=2)
    defBottomFrame.grid(column=0, row=3, padx=5, pady=5, sticky='nesw')
    #Configuring column and row resizability
    defBottomFrame.columnconfigure((0,1), weight=1)
    defBottomFrame.rowconfigure(0, weight=1)

    #LABELS
    #In top frame
    defTitleLbl = ttk.Label(defTopFrame, text = "Add or update a definition", anchor=tk.CENTER, background="white")
    defTitleLbl.grid(column=0, columnspan=5, row=0, padx=5, sticky="nsew")
    newUpdateDefLbl = ttk.Label(defTopFrame, text = "Choose New/Update:", background="white")
    newUpdateDefLbl.grid(column=0, row=1, padx=5, pady=3, sticky="nsew")
    partOfSpeechLbl = ttk.Label(defTopFrame, text = "Choose part of speech of your definition:", background="white")
    partOfSpeechLbl.grid(column=0, row=2, padx=5, pady=3, sticky="nsew")
    oshWordDefLbl = ttk.Label(defTopFrame, text = "Enter Oshindonga word to define:", background="white")
    oshWordDefLbl.grid(column=0, row=3, padx=5, pady=3, sticky="nsew")
    wordInDatabaseLbl = ttk.Label(defTopFrame, textvariable = wordToDefine, anchor=tk.CENTER, background="white")
    wordInDatabaseLbl.grid(column=0, columnspan=5, row=4, padx=5, sticky="nsew")
    #In middle frame
    engIdDefLbl = ttk.Label(defMidFrame, text = "English word ID", background="cyan")
    engIdDefLbl.grid(column=0, row=0, padx=5, sticky="nsew")
    engDefLbl = ttk.Label(defMidFrame, text = "English definition", background="cyan")
    engDefLbl.grid(column=1, row=0, padx=5, sticky="nsew")
    engExampleLbl = ttk.Label(defMidFrame, text = "English example", background="cyan")
    engExampleLbl.grid(column=2, row=0, padx=5, sticky="nsew")
    displayEngIdLbl = tk.Label(defMidFrame, textvariable = engIdDef, background="white")    #Using the tk label because ttk label won't work with the stringvar
    displayEngIdLbl.grid(column=0, row=1, padx=5, sticky="nsew")
    

    oshIdDefLbl = ttk.Label(defMidFrame, text = "Oshindonga word ID", background="cyan")
    oshIdDefLbl.grid(column=0, row=2, padx=5, sticky="nsew")
    oshDefLbl = ttk.Label(defMidFrame, text = "Oshindonga definition", background="cyan")
    oshDefLbl.grid(column=1, row=2, padx=5, sticky="nsew")
    oshExampleLbl = ttk.Label(defMidFrame, text = "Oshindonga example", background="cyan")
    oshExampleLbl.grid(column=2, row=2, padx=5, sticky="nsew")
    displayOshIdLbl = tk.Label(defMidFrame, textvariable = oshIdDef, background="white")    #Using the tk label because ttk label won't work with the stringvar
    displayOshIdLbl.grid(column=0, row=3, padx=5, sticky="nsew")

    #BUTTONS
    searchDefBtn = ttk.Button(searchOshFrame, text = "Search", command=search_word_to_define)
    searchDefBtn.grid(column=1, row=0, padx=5, sticky="nsew")

    saveDefBtn = ttk.Button(defBottomFrame, text = "Save")
    saveDefBtn.grid(column=0, row=0, padx=5, sticky="nsew")
    cancelDefBtn = ttk.Button(defBottomFrame, text = "Cancel")
    cancelDefBtn.grid(column=1, row=0, padx=5, sticky="nsew")

    #RADIOBUTTONS
    newDefRbtn = ttk.Radiobutton(newUpdateFrame, text="New", variable=newOrUpdateDef, value="New")
    newDefRbtn.grid(column=0, row=0, sticky="nsew")
    updateRbtn = ttk.Radiobutton(newUpdateFrame, text="Update", variable=newOrUpdateDef, value="Update")
    updateRbtn.grid(column=1, row=0, sticky="nsew")
    nounRbtn = ttk.Radiobutton(partsOfSpeechFrame, text="Noun", variable=partsOfSpeech, value="Noun")
    nounRbtn.grid(column=0, row=0, sticky="nsew")
    verbRbtn = ttk.Radiobutton(partsOfSpeechFrame, text="Verb", variable=partsOfSpeech, value="Verb")
    verbRbtn.grid(column=1, row=0, sticky="nsew")
    adverbRbtn = ttk.Radiobutton(partsOfSpeechFrame, text="Adverb", variable=partsOfSpeech, value="Adverb")
    adverbRbtn.grid(column=2, row=0, sticky="nsew")
    adjectiveRbtn = ttk.Radiobutton(partsOfSpeechFrame, text="Adjective", variable=partsOfSpeech, value="Adjective")
    adjectiveRbtn.grid(column=3, row=0, sticky="nsew")

    #TEXT ENTRY for multi-line texts
    engDefTxt = tk.Text(defMidFrame, height=2, width=40)
    engDefTxt.grid(column=1, row=1, sticky="nsew", pady=2)
    engExampleTxt = tk.Text(defMidFrame, height=2, width=40)
    engExampleTxt.grid(column=2, row=1, sticky="nsew", pady=2)
    oshDefTxt = tk.Text(defMidFrame, height=2, width=40)
    oshDefTxt.grid(column=1, row=3, sticky="nsew", pady=2)
    oshExampleTxt = tk.Text(defMidFrame, height=2, width=40)
    oshExampleTxt.grid(column=2, row=3, sticky="nsew", pady=2)

    #ENTRY BOXES
    oshWordDefEbx = ttk.Entry(searchOshFrame)
    oshWordDefEbx.grid(column=0, row=0, sticky="nsew", pady=2)

    #SIZEGRIPs
    ttk.Sizegrip(defWindow).grid(column=999, row=999, sticky='se')

def open_delete_word_window():
    delWordWindow = tk.Toplevel(mainWindow)
    delWordWindow.title("Delete a word")
    delWordWindow.resizable(tk.FALSE,tk.FALSE)

    #VARIABLES
    #Variables for the radiobuttons
    engDel = tk.StringVar()
    oshDel = tk.StringVar()
    

    #FRAMES
    delWordMainFrame = ttk.Frame(delWordWindow, relief='raised', borderwidth=3)
    delWordMainFrame.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')

    #LABELS
    delWordTitleLbl = ttk.Label(delWordMainFrame, text = "Delete a word from the database", anchor=tk.CENTER, background="white")
    delWordTitleLbl.grid(column=0, columnspan=3, row=0, padx=5, sticky="nsew")
    oshEngDelLbl = ttk.Label(delWordMainFrame, text = "Choose English/Oshindonga:", background="white")
    oshEngDelLbl.grid(column=0, row=1, padx=5, pady=3, sticky="nsew")
    wordIdDelLbl = ttk.Label(delWordMainFrame, text = "ID of word to be deleted:", background="white")
    wordIdDelLbl.grid(column=0, row=2, padx=5, pady=3, sticky="nsew")
    wordToDelLbl = ttk.Label(delWordMainFrame, text = "The word you've to delete is:", anchor=tk.CENTER, background="white")
    wordToDelLbl.grid(column=0, columnspan=3, row=3, padx=5, pady=3, sticky="nsew")

    #BUTTONS
    searchWordIdDelBtn = ttk.Button(delWordMainFrame, text = "Search database")
    searchWordIdDelBtn.grid(column=2, row=2, padx=5, sticky="nsew")
    delWordBtn = ttk.Button(delWordMainFrame, text = "Delete")
    delWordBtn.grid(column=1, row=4, padx=5, sticky="nsew")
    cancelDelWordBtn = ttk.Button(delWordMainFrame, text = "Cancel")
    cancelDelWordBtn.grid(column=2, row=4, padx=5, sticky="nsew")
    
    #RADIOBUTTONS
    engDelRbtn = ttk.Radiobutton(delWordMainFrame, text="English", variable=engDel, value="English")
    engDelRbtn.grid(column=1, row=1, sticky="nsew")
    oshDelRbtn = ttk.Radiobutton(delWordMainFrame, text="Oshindonga", variable=oshDel, value="Oshindonga")
    oshDelRbtn.grid(column=2, row=1, sticky="nsew")

    #ENTRY BOXES
    wordIdDelEbx = ttk.Entry(delWordMainFrame)
    wordIdDelEbx.grid(column=1, row=2, sticky="nsew", pady=2)

def open_delete_definition_window():
    delDefWindow = tk.Toplevel(mainWindow)
    delDefWindow.title("Delete a definition")
    delDefWindow.resizable(tk.FALSE,tk.FALSE)

    #VARIABLES
    #Variables for the radiobuttons
    nounDefDel = tk.StringVar()
    verbDefDel = tk.StringVar()
    

    #FRAMES
    delDefMainFrame = ttk.Frame(delDefWindow, relief='raised', borderwidth=3)
    delDefMainFrame.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')

    #LABELS
    delDefTitleLbl = ttk.Label(delDefMainFrame, text = "Delete a definition from the database", anchor=tk.CENTER, background="white")
    delDefTitleLbl.grid(column=0, columnspan=3, row=0, padx=5, sticky="nsew")
    speechDefDelLbl = ttk.Label(delDefMainFrame, text = "Choose the part of speech:", background="white")
    speechDefDelLbl.grid(column=0, row=2, padx=5, pady=3, sticky="nsew")
    defDisplayDelLbl = ttk.Label(delDefMainFrame, text = "Definition to be deleted:", background="white")
    defDisplayDelLbl.grid(column=0, columnspan=3, row=3, padx=5, pady=3, sticky="nsew")

    #BUTTONS
    searchDefIdDelBtn = ttk.Button(delDefMainFrame, text = "Search database")
    searchDefIdDelBtn.grid(column=2, row=2, padx=5, sticky="nsew")
    delDefBtn = ttk.Button(delDefMainFrame, text = "Delete")
    delDefBtn.grid(column=1, row=4, padx=5, sticky="nsew")
    cancelDefDelBtn = ttk.Button(delDefMainFrame, text = "Cancel")
    cancelDefDelBtn.grid(column=2, row=4, padx=5, sticky="nsew")
    
    #RADIOBUTTONS
    nounDelRbtn = ttk.Radiobutton(delDefMainFrame, text="Noun", variable=nounDefDel, value="Noun")
    nounDelRbtn.grid(column=1, row=1, sticky="nsew")
    verbDelRbtn = ttk.Radiobutton(delDefMainFrame, text="Verb", variable=verbDefDel, value="Verb")
    verbDelRbtn.grid(column=2, row=1, sticky="nsew")

    #ENTRY BOXES
    defIdDelEbx = ttk.Entry(delDefMainFrame)
    defIdDelEbx.grid(column=1, row=2, sticky="nsew", pady=2)

def open_main_window():
    global mainWindow   #Makes it accessible to all other functions
    mainWindow =  ThemedTk(theme="arc") #tk.Tk()
    mainWindow.title("Oshinglish Dictionary First Edition")
    #mainWindow.configure(background = "#0970d2")
    #mainWindow.geometry("900x600+300+0")

    #THEMES & STYLE
    #theme = ttk.Style()
    #print(theme.theme_names()) #Prints theme names
    #print(theme.theme_use()) #Prints theme in use
    #theme.theme_use('winnative') #Changes theme in use

    #Configuring column and row resizability
    mainWindow.columnconfigure(0, weight=1)
    mainWindow.rowconfigure(0, weight=1)

    #VARIABLES
    #global inputLang
    searchedWord = tk.StringVar()
    searchedWord.set("No word to display")
    inputLang = tk.StringVar() #variable for input language radiobuttons
    #inputLang.set("English")
    # def set_input_language():
    #     inputLang.set(value)
    logo = tk.PhotoImage(file='Logo.gif')
    mainDefinition = "No definition to display"
                    
    def select_def_to_search():     #
        language = inputLang.get()  #Checks language input selected on radiobutton
        if language == "English":
            mainDefinition = find_definition(find_english_word(searchEbx.get()))    #gets word in the entrybox, passes it to find_english_word(), which is passed to find_definition(), then assigns it to mainDefinition
        elif language == "Oshindonga":
            mainDefinition = find_definition(find_oshindonga_word(searchEbx.get())) #gets word in the entrybox, passes it to find_oshindonga_word(), which is passed to find_definition(), then assigns it to mainDefinition
        else:
            return messagebox.showerror(title="Input language", message="You did not select an input language.\nSelect the input language and search again.")
        searchedWord.set(searchEbx.get())   #Gets the word in entrybox and assigns it to searchedWord StringVar for display at the top of the text widget
        definitionTxt.delete("1.0", tk.END) #Clears the text widget
        definitionTxt.insert(tk.END, mainDefinition)    #Inserts the value of mainDefinition into the text widget
        return

    #FRAMES
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

    #LABELS
    logoLbl = tk.Label(topFrame, image = logo) #Need to fix the problem with displaying logo
    logoLbl.image = logo #Keeps a reference to avoid blanking of the image (http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm)
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
    wordLbl = ttk.Label(bottomFrame, textvariable=searchedWord, background="white")
    wordLbl.grid(column=0, row=0, sticky="w")
   

    #BUTTONS
    deleteDefBtn = ttk.Button(rightFrame, text = "Delete definition from database", command=open_delete_definition_window)
    deleteDefBtn.grid(column=3, row=0, sticky="nsew")
    searchBtn = ttk.Button(leftFrame, text = "Search", command=select_def_to_search)
    searchBtn.grid(column=1, row=2)
    addEngBtn = ttk.Button(rightFrame, text = "Add/update English word", command=open_english_window)
    addEngBtn.grid(column=0, row=1, sticky="nsew")
    addOshBtn = ttk.Button(rightFrame, text = "Add/Update Oshindonga word", command=open_oshindonga_window)
    addOshBtn.grid(column=1, row=1, sticky="nsew")
    addDefBtn = ttk.Button(rightFrame, text = "Add/Update definition", command=open_definition_window)
    addDefBtn.grid(column=2, row=1, sticky="nsew")
    deleteWordBtn = ttk.Button(rightFrame, text = "Delete word from database", command=open_delete_word_window)
    deleteWordBtn.grid(column=3, row=1, sticky="nsew")

    #RADIOBUTTONS
    englishRbtn = ttk.Radiobutton(leftFrame, text="English", variable=inputLang, value="English")
    englishRbtn.grid(column=1, row=1, sticky="nsew")
    oshindongaRbtn = ttk.Radiobutton(leftFrame, text="Oshindonga", variable=inputLang, value="Oshindonga")
    oshindongaRbtn.grid(column=2, row=1, sticky="nsew")

    #ENTRY WIDGETS
    searchEbx = ttk.Entry(leftFrame)
    searchEbx.grid(column=0, row=2, sticky="nsew", pady=2)

    #TEXT WIDGETS
    definitionTxt = tk.Text(bottomFrame, background="white", height=10, width=100)
    definitionTxt.grid(column=0, row=1, sticky="nsew")
    definitionTxt.insert(tk.END, mainDefinition)
    #OPTION MENUES
    #SIZEGRIPs
    ttk.Sizegrip(mainWindow).grid(column=999, row=999, sticky='se')

    #SCROLLBARS
    defScrb = tk.Scrollbar(bottomFrame, orient=tk.VERTICAL, command=definitionTxt.yview)
    defScrb.grid(column=1, row=1, sticky="ns")
    definitionTxt.configure(yscrollcommand=defScrb.set)
    


open_main_window() #Opens the main window



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

english = c.execute("SELECT * FROM english")
print(c.fetchall())
oshindonga = c.execute("SELECT * FROM oshindonga")
print(c.fetchall())

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




#conn.close()

mainWindow.mainloop()
