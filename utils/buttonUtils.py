import json

import utils.database as db

def changeButonText(button, text1, text2):
    if button['text'] == text1:
        button['text'] = text2
    else:
        button['text'] = text1

# function to fill database with buttons
def fillButtonsDB():
    db.addButtonDB(7, 2, 'vent', 'vent_active', {'fan': [1]}, 0)
    db.addButtonDB(8, 2, 'light', 'light_active', {'light': [39]}, 1)

    db.addButtonDB(11, 1, 'cam', 'cam_active', {'camEnable': [6]}, 0)
    db.addButtonDB(12, 1, 'door', 'door_active', {'door': [7]}, 0)
    db.addButtonDB(13, 1, 'light', 'light_active', {'light': [37]}, 1)
    db.addButtonDB(14, 1, 'alarm', 'alarm_active', {'alarm': [7], 'sound': []}, 0)
    db.addButtonDB(15, 1, 'panel', 'panel_active', {'serverBlink': []}, 1)
    db.addButtonDB(16, 1, 'smoke', 'smoke_active', {'smoke': [1]}, 0)
    db.addButtonDB(17, 1, 'fire', 'fire_active', {'fireSingle': [3]}, 0)

    db.addButtonDB(11, 2, 'cam', 'cam_active', {'camEnable': [3]}, 0)
    db.addButtonDB(12, 2, 'door', 'door_active', {'door': [8]}, 0)
    db.addButtonDB(13, 2, 'light', 'light_active', {'light': [38]}, 1)
    db.addButtonDB(14, 2, 'alarm', 'alarm_active', {'alarm': [1], 'sound': []}, 0)
    db.addButtonDB(15, 2, 'smoke', 'smoke_active', {'smoke': [0]}, 0)
    db.addButtonDB(16, 2, 'fire', 'fire_active', {'fireSingle': [2]}, 0)

    db.addButtonDB(11, 4, 'cam', 'cam_active', {'camEnable': [5]}, 0)
    db.addButtonDB(12, 4, 'door', 'door_active', {'door': [9]}, 0)
    db.addButtonDB(13, 4, 'light', 'light_active', {'light': [34]}, 1)
    db.addButtonDB(14, 4, 'alarm', 'alarm_active', {'alarm': [15], 'sound': []}, 0)
    db.addButtonDB(15, 4, 'smoke', 'smoke_active', {'smoke': [2]}, 0)
    db.addButtonDB(16, 4, 'fire', 'fire_active', {'fireSingle': [14]}, 0)

    db.addButtonDB(11, 5, 'cam', 'cam_active', {'camEnable': [4]}, 0)
    db.addButtonDB(12, 5, 'door', 'door_active', {'door': [10]}, 0)
    db.addButtonDB(13, 5, 'light', 'light_active', {'light': [35]}, 1)
    db.addButtonDB(14, 5, 'alarm', 'alarm_active', {'alarm': [12], 'sound': []}, 0)
    db.addButtonDB(15, 5, 'smoke', 'smoke_active', {'smoke': [6]}, 0)
    db.addButtonDB(16, 5, 'fire', 'fire_active', {'fireSingle': [13]}, 0)

    db.addButtonDB(11, 9, 'cam', 'cam_active', {'camEnable': [1]}, 0)
    db.addButtonDB(12, 9, 'door', 'door_active', {'door': [12]}, 0)
    db.addButtonDB(13, 9, 'light', 'light_active', {'light': [47]}, 1)
    db.addButtonDB(14, 9, 'alarm', 'alarm_active', {'alarm': [11], 'sound': []}, 0)
    db.addButtonDB(15, 9, 'smoke', 'smoke_active', {'smoke': [5]}, 0)
    db.addButtonDB(16, 9, 'fire', 'fire_active', {'fire': [10, 8]}, 0)
    db.addButtonDB(17, 9, 'door', 'door_active', {'door': [13]}, 0)

    db.addButtonDB(2, 8, 'cam', 'cam_active', {'camEnable': [2]}, 0)
    db.addButtonDB(3, 8, 'door', 'door_active', {'door': [14]}, 0)
    db.addButtonDB(4, 8, 'light', 'light_active', {'light': [33]}, 1)
    db.addButtonDB(2, 9, 'alarm', 'alarm_active', {'alarm': [0], 'sound': []}, 0)
    db.addButtonDB(3, 9, 'smoke', 'smoke_active', {'smoke': [4]}, 0)
    db.addButtonDB(4, 9, 'fire', 'fire_active', {'fireSingle': [26]}, 0)

    db.addButtonDB(2, 4, 'alarm', 'alarm_active', {'alarm': [28], 'alarm': [31], 'fireFighterSound': []}, 0)
    db.addButtonDB(3, 4, 'vent', 'vent_active', {'fan': [0]}, 0)
    db.addButtonDB(4, 4, 'light', 'light_active', {'light': [48]}, 1)
    db.addButtonDB(3, 5, 'smoke', 'smoke_active', {'smoke': [3]}, 0)
    db.addButtonDB(4, 5, 'fire', 'fire_active', {'fire': [27, 29], 'fireSingle': [30]}, 0)
    db.addButtonDB(5, 5, 'cam', 'cam_active', {'camEnable': [0]}, 0)

    db.addButtonDB(7, 9, 'led', 'led_active', {'emergencyLight': []}, 0)
    db.addButtonDB(7, 5, 'emergency_active', 'emergency', {'emergency': []}, 0)
    db.addButtonDB(8, 5, 'light', 'light_active', {'light': [36]}, 1)

    db.addButtonDB(11, 8, 'light', 'light_active', {'light': [32]}, 1)
    db.addButtonDB(8, 9, 'door', 'door_active', {'door': [15]}, 0)

    db.addButtonDB(9, 2, 'alarm', 'alarm_active', {'alarm': [0], 'sound': []}, 0)
    db.addButtonDB(12, 8, 'alarm', 'alarm_active', {'alarm': [9], 'sound': []}, 0)

def createButtons(self):
    for buttonInfo in self.buttonsInfo:
        id = buttonInfo["id"]
        column = buttonInfo["column"]
        row = buttonInfo["row"]
        imgPassiveName = buttonInfo["img_passive"]
        imgActiveName = buttonInfo["img_active"]
        command = json.loads(buttonInfo["command"])
        status = buttonInfo["status"]

        createButton(self, id, column, row, imgPassiveName, imgActiveName, command, status)

def createButton(self, id, column, row, imgPassiveName, imgActiveName, commandInfo, status):
    try:
        imgPassive = getattr(self.img_father, imgPassiveName)
        imgActive = getattr(self.img_father, imgActiveName)
        commands = list(commandInfo.keys())

        if len(commandInfo) == 1:
            commandName = commands[0]
            command = getattr(self, commandName)
            button = self.btn_father.btn(imgPassive, imgActive,
                                         lambda: self.loop.create_task(command(*[i for i in commandInfo[commandName]], button)), status)
        elif len(commandInfo) == 2:
            command1 = getattr(self, commands[0])
            command2 = getattr(self, commands[1])
            button = self.btn_father.btn(imgPassive, imgActive,
                                         lambda: [self.loop.create_task(command1(*[i for i in commandInfo[commands[0]]], button)), self.loop.create_task(command2(*[i for i in commandInfo[commands[1]]]))], status)
        elif len(commandInfo) == 3:
            command1 = getattr(self, commands[0])
            command2 = getattr(self, commands[1])
            command3 = getattr(self, commands[2])
            button = self.btn_father.btn(imgPassive, imgActive,
                                         lambda: [self.loop.create_task(command1(*[i for i in commandInfo[commands[0]]], button)), self.loop.create_task(command2(*[i for i in commandInfo[commands[1]]], button)), self.loop.create_task(command3(*[i for i in commandInfo[commands[2]]]))], status)
        else:
            raise ValueError(
                "The 'commandInfo' dictionary must contain up to 3 arguments")

        button.id = id
        button.imgPassiveName = imgPassiveName
        self.buttons.append(button)
        button.grid(column=column, row=row)
        self.dnd.add_dragable(button)
    except Exception as e:
        print("Error: ", e)


def placeButtons(self):
    for button in self.buttons:
        buttonLocation = [x for x in self.buttonsLocation if x["id"]==str(button)][0]
        column = buttonLocation['column']
        row = buttonLocation['row'] 
        button.grid(column=column, row=row)
        self.dnd.add_dragable(button)

def placeInterfaceButtons(self):
    # using x, y because this buttons do not use drag and drop
    self.btnVolumeUp.place(x=30, y=125)
    self.btnVolumeDown.place(x=100, y=125)
    self.btnManual.place(x=20, y=40)
    self.ekosystem.place(x=100, y=300)
    self.line1.place(x=350, y=365)
    self.line2.place(x=350, y=185)