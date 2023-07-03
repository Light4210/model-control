from tkinter import *
from utils import buttonUtils

# menu for deleting buttons
def createMenu(self):
    menu = Menu(self.root, tearoff=0)

    def showMenu(event, buttonID):
        if self.dnd.editing_on():
            menu.post(event.x_root, event.y_root)
            menu.entryconfigure(0, command=lambda: buttonUtils.deleteButton(self, buttonID))

    menu.add_command(label="Delete", command=buttonUtils.deleteButton)

    for button in self.buttons:
        button.bind("<Button-3>", lambda event, btnID=button.id: showMenu(event, btnID))

# dialog window where we select parametrs of new button
def showDialog(self):
    dialog = Toplevel(self.root)

    # Create a label and a dropdown menu for the "Type" selection
    labelType = Label(dialog, text="Type:")
    labelType.pack()
    options = ["alarm", "light", "smoke", "fireSingle", "door", "panel", "cam", "emergency", "vent", "led", "fireFighter", "fire"]
    typeVar = StringVar(dialog)
    typeVar.set(options[0])
    typeMenu = OptionMenu(dialog, typeVar, *options)
    typeMenu.pack()

    labelColumn = Label(dialog, text="Column:")
    labelColumn.pack()
    column = Entry(dialog)
    column.insert(0, 1)
    column.pack()

    labelRow = Label(dialog, text="Row:")
    labelRow.pack()
    row = Entry(dialog)
    row.insert(0, 1)
    row.pack()

    labelIndex = Label(dialog, text="Index:")
    labelIndex.pack()
    index = Entry(dialog)
    index.pack()

    placeButton = Button(dialog, text="Place", command=lambda: buttonUtils.addButton(
        self, typeVar.get(), column.get(), row.get(), index.get()))
    placeButton.pack()