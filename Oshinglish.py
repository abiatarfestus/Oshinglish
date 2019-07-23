from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Oshinglish Dictionary First Edition")

nameWithLogo = ttk.Label(root, text = "Oshinglish Dictionary First Edition")
nameWithLogo.grid(columnspan = 10, row = 0, sticky = W)

options = ttk.OptionMenu(root, variable = 3)
options.grid(column = 0, row = 1, sticky = W)

infoMenu = ttk.Menubutton(root)
infoMenu.grid(column = 1, row = 1)

searchBox = ttk.Entry(root)
searchBox.grid(columnspan = 3, row = 2, sticky = W)

findButton = ttk.Button(root, text = "Find")
findButton.grid(column = 3, row = 2)

listLabel = ttk.Label(root, text = "")
listLabel.grid(columnspan = 3, rowspan = 5, sticky = W)

definitionSpace = ttk.Label(root, text = "")
definitionSpace.grid(columnspan = 5, rowspan = 5)



root.mainloop()
