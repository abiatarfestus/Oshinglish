from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Oshinglish Dictionary First Edition")
root.geometry("600x500")

nameWithLogo = ttk.Label(root, text = "Oshinglish Dictionary First Edition", font = "Times 28", background = "blue")
nameWithLogo.grid(columnspan = 20, rowspan = 5, sticky = W)

options = ttk.OptionMenu(root, variable = 3)
options.grid(columnspan = 3, row = 5, sticky = W)

infoMenu = ttk.Menubutton(root)
infoMenu.grid(column = 3, row = 5)

searchBox = ttk.Entry(root)
searchBox.grid(columnspan = 11, row = 6, sticky = W)

findButton = ttk.Button(root, text = "Find")
findButton.grid(column = 9, row = 6)

listLabel = ttk.Label(root, text = "List of words appears here", background = "white")
listLabel.grid(columnspan = 5, rowspan = 15, sticky = W)


definitionSpace = ttk.Label(root, text = "Definitions appear here")
definitionSpace.grid(columnspan = 15, rowspan = 15)



root.mainloop()
