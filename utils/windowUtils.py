from tkinter import *
from utils import buttonUtils

def createMenu(self):
    menu = Menu(self.root, tearoff=0)

    def showMenu(event, buttonID):
        if self.dnd.editing_on():
            menu.post(event.x_root, event.y_root)
            menu.entryconfigure(0, command=lambda: buttonUtils.deleteButton(self, buttonID))

    menu.add_command(label="Delete", command=buttonUtils.deleteButton)

    for button in self.buttons:
        button.bind("<Button-3>", lambda event, btnID=button.id: showMenu(event, btnID))