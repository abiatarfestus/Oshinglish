from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Oshinglish Dictionary First Edition")
root.geometry("600x500")

nameWithLogo = ttk.Label(root, text = "Oshinglish Dictionary First Edition", background = "blue")
nameWithLogo.grid(rowspan = 3, sticky = W+E)

options = ttk.OptionMenu(root, variable = 3)
options.grid(column = 0, row = 3, sticky = W)

infoMenu = ttk.Menubutton(root)
infoMenu.grid(column = 1, row = 3)

searchBox = ttk.Entry(root)
searchBox.grid(columnspan = 3, row = 4, sticky = W)

findButton = ttk.Button(root, text = "Find")
findButton.grid(column = 3, row = 4)

listLabel = ttk.Label(root, text = "List of words appears here", background = "white")
listLabel.grid(columnspan = 3, rowspan = 15, sticky = W)

definitionSpace = ttk.Label(root, text = "Definitions appear here")
definitionSpace.grid(columnspan = 5, rowspan = 5)



root.mainloop()
