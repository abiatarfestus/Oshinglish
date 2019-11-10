from tkinter import*

root = Tk()
root.title("Oshinglish Dictionary First Edition")
root.configure(background = "#0970d2")
root.geometry("800x800")

nameWithLogo = Label(root, text = "Oshinglish Dictionary First Edition", font = "Times 28", background = "#982901")
nameWithLogo.grid()

#options = OptionMenu(root, variable = 3)
#options.grid(columnspan = 3, row = 5, sticky = W)

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



root.mainloop()
