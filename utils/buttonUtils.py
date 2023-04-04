from utils.DragManager import DragManager

def changeButonText(button, text1, text2):
    if button['text'] == text1:
        button['text'] = text2
    else:
        button['text'] = text1

def placeButtons(self):
    for button in self.buttons:
        buttonLocation = [x for x in self.buttonsLocation if x["id"]==str(button)][0]
        column = buttonLocation['column']
        row = buttonLocation['row'] 
        button.grid(column=column, row=row)
        self.dnd.add_dragable(button)

# this funciton used only if database is empty
def hardPlaceButtons(self):
    self.btnFan1.grid(column=7, row=2)
    self.btnLight10.grid(column=8, row=2)

    self.btnCam1.grid(column=11, row=1)
    self.btnDoor1.grid(column=12, row=1)
    self.btnLight1.grid(column=13, row=1)
    self.btnAlarm1.grid(column=14, row=1)
    self.btnPanel1.grid(column=15, row=1)
    self.btnSmoke1.grid(column=16, row=1)
    self.btnFire1.grid(column=17, row=1)

    self.btnCam2.grid(column=11, row=2)
    self.btnDoor2.grid(column=12, row=2)
    self.btnLight2.grid(column=13, row=2)
    self.btnAlarm2.grid(column=14, row=2)
    self.btnSmoke2.grid(column=15, row=2)
    self.btnFire2.grid(column=16, row=2)

    self.btnCam3.grid(column=11, row=4)
    self.btnDoor3.grid(column=12, row=4)
    self.btnLight3.grid(column=13, row=4)
    self.btnAlarm3.grid(column=14, row=4)
    self.btnSmoke3.grid(column=15, row=4)
    self.btnFire3.grid(column=16, row=4)

    self.btnCam4.grid(column=11, row=5)
    self.btnDoor4.grid(column=12, row=5)
    self.btnLight4.grid(column=13, row=5)
    self.btnAlarm4.grid(column=14, row=5)
    self.btnSmoke4.grid(column=15, row=5)
    self.btnFire4.grid(column=16, row=5)

    self.btnCam5.grid(column=11, row=9)
    self.btnDoor5.grid(column=12, row=9)
    self.btnLight5.grid(column=13, row=9)
    self.btnAlarm5.grid(column=14, row=9)
    self.btnSmoke5.grid(column=15, row=9)
    self.btnFire5.grid(column=16, row=9)
    self.btnDoor6.grid(column=17, row=9)

    self.btnCam6.grid(column=2, row=8)
    self.btnDoor8.grid(column=3, row=8)
    self.btnLight8.grid(column=4, row=8)
    self.btnAlarm6.grid(column=2, row=9)
    self.btnSmoke6.grid(column=3, row=9)
    self.btnFire6.grid(column=4, row=9)

    self.btnAlarm7.grid(column=2, row=4)
    self.btnFan2.grid(column=3, row=4)
    self.btnLight9.grid(column=4, row=4)
    self.btnSmoke7.grid(column=3, row=5)
    self.btnFire7.grid(column=4, row=5)
    self.btnCam7.grid(column=5, row=5)

    # self.btnCam8.place(x=100, y=245)

    self.btnLight6.grid(column=7, row=9)
    self.btnEmergency.grid(column=7, row=5)
    self.btnLight11.grid(column=8, row=5)

    # using x, y because this buttons do not use drag and drop
    self.btnVolumeUp.place(x=30, y=125)
    self.btnVolumeDown.place(x=100, y=125)
    self.btnManual.place(x=20, y=40)
    self.ekosystem.place(x=100, y=300)
    self.line1.place(x=350, y=365)
    self.line2.place(x=350, y=185)

    self.btnLight7.grid(column=11, row=8)
    self.btnDoor7.grid(column=8, row=9)

    self.btnAlarm8.grid(column=9, row=2)
    self.btnAlarm9.grid(column=12, row=8)

def placeInterfaceButtons(self):
    # using x, y because this buttons do not use drag and drop
    self.btnVolumeUp.place(x=30, y=125)
    self.btnVolumeDown.place(x=100, y=125)
    self.btnManual.place(x=20, y=40)
    self.ekosystem.place(x=100, y=300)
    self.line1.place(x=350, y=365)
    self.line2.place(x=350, y=185)

    self.btnLight7.grid(column=11, row=8)
    self.btnDoor7.grid(column=8, row=9)

    self.btnAlarm8.grid(column=9, row=2)
    self.btnAlarm9.grid(column=12, row=8)

def getButtons(self):
    # list of all dragable buttons
    buttons = [
        self.btnFan1,
        self.btnLight10,
        self.btnCam1,
        self.btnDoor1,
        self.btnLight1,
        self.btnAlarm1,
        self.btnPanel1,
        self.btnSmoke1,
        self.btnFire1,
        self.btnCam2,
        self.btnDoor2,
        self.btnLight2,
        self.btnAlarm2,
        self.btnSmoke2,
        self.btnFire2,
        self.btnCam3,
        self.btnDoor3,
        self.btnLight3,
        self.btnAlarm3,
        self.btnSmoke3,
        self.btnFire3,
        self.btnCam4,
        self.btnDoor4,
        self.btnLight4,
        self.btnAlarm4,
        self.btnSmoke4,
        self.btnFire4,
        self.btnCam5,
        self.btnDoor5,
        self.btnLight5,
        self.btnAlarm5,
        self.btnSmoke5,
        self.btnFire5,
        self.btnCam6,
        self.btnDoor8,
        self.btnLight8,
        self.btnAlarm6,
        self.btnSmoke6,
        self.btnFire6,
        self.btnCam7,
        self.btnFan2,
        self.btnLight9,
        self.btnAlarm7,
        self.btnSmoke7,
        self.btnFire7,
        self.btnDoor6,
        self.btnLight6,
        self.btnEmergency,
        self.btnLight11,
        self.btnLight7,
        self.btnDoor7,
        self.btnAlarm8,
        self.btnAlarm9,
    ]

    return buttons