import threading
from tkinter import *
import asyncio
import time
import serial
from PIL import ImageTk, Image
from pygame import mixer
import cv2
from random import randrange
from threading import Event
from pynput.keyboard import Key,Controller
import json

from utils.DragManager import DragManager
from utils import buttonUtils
from utils import windowUtils
import utils.database as db

mixer.init()

class camThread(threading.Thread):
    def __init__(self, previewName, camID, event):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.event = event
    def run(self):
        try:
            camPreview(self.previewName, self.camID, self.event)
        except:
            camPreview(self.previewName, self.camID, self.event)


def camPreview(previewName, camID, event):
    cv2.namedWindow(previewName, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(previewName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cam = cv2.VideoCapture(camID)
    cam.set(cv2.CAP_PROP_FPS, 60.0)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        cv2.namedWindow(previewName, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(previewName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.moveWindow(previewName, 1024, 0)
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if event.is_set():
            break
    cv2.destroyWindow(previewName)

# Create two threads as follows

class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()


class WD_Images(Tk):
    def __init__(self, root):
        self.root = root

        self.manual = "img/manual.png"
        self.scenary_btn = "img/scenary.png"

        self.scenary_1 = "img/scenary-1.png"
        self.scenary_active_1 = "img/scenary-active-1.png"

        self.scenary_2 = "img/scenary-2.png"
        self.scenary_active_2 = "img/scenary-active-2.png"

        self.scenary_3 = "img/scenary-3.png"
        self.scenary_active_3 = "img/scenary-active-3.png"

        self.scenary_4 = "img/scenary-4.png"
        self.scenary_active_4 = "img/scenary-active-4.png"

        self.scenary_5 = "img/scenary-5.png"
        self.scenary_active_5 = "img/scenary-active-5.png"

        self.scenary_6 = "img/scenary-6.png"
        self.scenary_active_6 = "img/scenary-active-6.png"

        self.scenary_7 = "img/scenary-7.png"
        self.scenary_active_7 = "img/scenary-active-7.png"

        self.door = "img/door.png"
        self.door_active = "img/door-active.png"

        self.emergency = "img/emergency.png"
        self.emergency_active = "img/emergency-active.png"

        self.cam = "img/cam.png"
        self.cam_active = "img/cam-active.png"

        self.led = "img/led.png"
        self.led_active = "img/led-active.png"

        self.light = "img/light.png"
        self.light_active = "img/light-active.png"

        self.smoke = "img/smoke.png"
        self.smoke_active = "img/smoke-active.png"

        self.fire = "img/fire.png"
        self.fire_active = "img/fire-active.png"

        self.alarm = "img/alarm.png"
        self.alarm_active = "img/alarm-active.png"

        self.hair_dryer = "img/hair-dryer.png"
        self.hair_dryer_active = "img/hair-dryer-active.png"

        self.panel = "img/panel.png"
        self.panel_active = "img/panel-active.png"

        self.tree = "img/tree.png"
        self.tree_active = "img/tree-active.png"

        self.fireplace = "img/fireplace.png"
        self.fireplace_active = "img/fireplace-active.png"

        self.volumeUp = "img/sound-increase.png"
        self.volumeDown = "img/sound-decrease.png"

        self.kotel = "img/gaz.png"
        self.kotel_active = "img/gaz-active.png"

        self.torch = "img/torch.png"
        self.torch_active = "img/torch-active.png"

        self.vent = "img/vent.png"
        self.vent_active = "img/vent-active.png"

        self.balon = "img/balon.png"
        self.balon_active = "img/balon-active.png"

        self.wilka = "img/wilka.png"
        self.wilka_active = "img/wilka-active.png"

        self.cook = "img/food.png"
        self.cook_active = "img/food-active.png"

        self.ekosystem = "img/ekosystem.png"

        self.line = "img/line.png"
        self.office_text = "img/office-text.png"
        self.hall_text = "img/hall-text.png"
        self.sheaf_text = "img/sheaf-text.png"
        self.server_text = "img/server-text.png"
        self.kitchen_text = "img/kitchen-text.png"
        self.conf_text = "img/conf-text.png"


class WD_Button(Tk):
    count = 0
    def __init__(self, root):
        self.root = root


    def btn(self, pasive, active, command, status, x=50, y=50):
        self.active = ImageTk.PhotoImage(Image.open(active).resize((x, y)))
        self.pasive = ImageTk.PhotoImage(Image.open(pasive).resize((x, y)))
        ret = 'pasive'
        if status == 1:
            ret = 'active'
        btn = Button(self.root, text="", image=getattr(self, ret), borderwidth=0, activebackground='#ffffff', background='#ffffff',
                     relief=SUNKEN, command=command)
        btn.status = status
        btn.active = self.active
        btn.pasive = self.pasive
        return btn



class Window(Tk):

    def __init__(self, loop):
        self.alarmStatus = 0
        self.fireFighterStatus = 0
        self.volume = 50;
        self.keyboard = Controller()
        self.loop = loop
        self.name = 'frame'
        self.status = False
        self.root = Tk()
        self.root.config(background='#ffffff')
        self.keyboard = Controller()
        self.root.geometry("%dx%d" % (1024, 600))
        # all buton sizes must be equal for correct grid
        self.buttonWidth = 52
        self.buttonHeight = 52

        self.arduino = serial.Serial(port='COM9', baudrate=57600)
        # while True:
        #     id = input('id')
        #     self.blackout()
        #     string = "<LEDWRITE" + "\0" + id + "\0" + '255' + ">"
        #     print(string)
        #     self.arduino.write(bytes(string, 'utf-8'))
        #     data = self.arduino.read_all()
        #     print(data.decode())
        #     self.arduino.write(bytes(string, 'utf-8'))

        self.dnd = DragManager(self.root)

        self.app_backround = ImageTk.PhotoImage(Image.open("img/back.jpg").resize((1024, 550)))
        self.label1 = Label(self.root, image=self.app_backround, background='#ffffff', padx=50, pady=50)
        self.label1.place(x=0, y=0)

        self.img_father = WD_Images(self.root)
        self.btn_father = WD_Button(self.root)

        self.line1 = self.btn_father.btn(self.img_father.line, self.img_father.line,
                                             lambda: self.loop.create_task(self.none()), 0, 580, 4)
        self.line2 = self.btn_father.btn(self.img_father.line, self.img_father.line,
                                             lambda: self.loop.create_task(self.none()), 0, 580, 4)
        self.office = self.btn_father.btn(self.img_father.office_text, self.img_father.office_text,
                                             lambda: self.loop.create_task(self.none()), 0, 35, 14)

        self.office.place(x=700, y=167)
        self.kitchen = self.btn_father.btn(self.img_father.kitchen_text, self.img_father.kitchen_text,
                                             lambda: self.loop.create_task(self.none()), 0, 50, 12)
        self.kitchen.place(x=700, y=375)
        self.hall = self.btn_father.btn(self.img_father.hall_text, self.img_father.hall_text,
                                             lambda: self.loop.create_task(self.none()), 0, 35, 12)
        self.hall.place(x=190, y=378)
        self.server = self.btn_father.btn(self.img_father.server_text, self.img_father.server_text,
                                             lambda: self.loop.create_task(self.none()), 0, 80, 14)
        self.server.place(x=700, y=17)
        self.sheaf = self.btn_father.btn(self.img_father.sheaf_text, self.img_father.sheaf_text,
                                             lambda: self.loop.create_task(self.none()), 0, 140, 14)
        self.sheaf.place(x=700, y=193)
        self.conf = self.btn_father.btn(self.img_father.conf_text, self.img_father.conf_text,
                                             lambda: self.loop.create_task(self.none()), 0, 110, 14)
        self.conf.place(x=700, y=347)

        #interface buttons
        self.ekosystem = self.btn_father.btn(self.img_father.ekosystem, self.img_father.manual,
                                             lambda: self.loop.create_task(self.none()), 0, 222, 46)
        self.btnManual = self.btn_father.btn(self.img_father.manual, self.img_father.manual,
                                             lambda: self.loop.create_task(self.new()), 0, 222,46)
        self.btnVolumeUp = self.btn_father.btn(self.img_father.volumeUp, self.img_father.volumeUp,
                                               lambda: self.loop.create_task(self.volumeUp()), 0)
        self.btnVolumeDown = self.btn_father.btn(self.img_father.volumeDown, self.img_father.volumeDown,
                                                 lambda: self.loop.create_task(self.volumeDown()), 0)

        self.buttons = []

        # updating root to get width and height of root
        self.root.update()

        # set columns and rows size to size of button
        columnsSize = int(self.root.winfo_width() / self.buttonWidth)
        rowsSize = int(self.root.winfo_height() / self.buttonHeight)

        # set minsize of row and cloumn to size of button
        for i in range(columnsSize):
            self.root.grid_columnconfigure(i, minsize=self.buttonWidth)

        for j in range(rowsSize):
            self.root.grid_rowconfigure(j, minsize=self.buttonHeight)

        self.buttonsInfo = json.loads(db.getButtonsDB())
        buttonUtils.createButtons(self)
        
        # smokes and cams buttons in arrays for correct functions working
        self.smokes = [button for button in self.buttons if button.imgPassiveName == "smoke"]
        self.cams = [button for button in self.buttons if button.imgPassiveName == "cam"]

        buttonUtils.placeInterfaceButtons(self)

        windowUtils.createMenu(self)

        #button for to turn on edit mode and save changes
        self.editButton = Button(text="edit", command=lambda: [self.dnd.change_edit_mode(), buttonUtils.changeButonText(
            self.editButton, "edit", "save"), db.saveChangesToDb(buttons=self.buttons) if self.editButton["text"] == "edit" else None])
        self.editButton.place(x=550, y=550)

    def smokeSerial(self, param1, time = 5000):
        string = "<SMOKE" + "\0" + str(param1) + "\0" + str(time) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))

    def ledSerial(self, method, param1, param2):
        string = "<LEDWRITE" + "\0" + str(param1) + "\0" + str(param2) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))

    def fireSerial(self, param1, param2):
        string = "<LEDFIREA" + "\0" + str(param1) + "\0" + str(param2) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    def fireSerialSingle(self, param1):
        string = "<LEDFIREB" + "\0" + str(param1)  + "\0" + str(63) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())


    def servo(self, method, param1):
        string = "<" + method + "\0" + str(param1) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())
        self.arduino.write(bytes(string, 'utf-8'))

#TODO end this
    async def emergency(self, emergency):
        self.change_img(emergency)
        status = 0 if emergency.status == 0 else 1
        if status == 1:
            self.blackout()
            await asyncio.sleep(.1)
            self.ledSerial('LEDWRITE', 20, 255)
            await asyncio.sleep(.1)
            self.ledSerial('LEDWRITE', 21, 255)
        else:
            self.default()
            await asyncio.sleep(.1)
            self.ledSerial('LEDWRITE', 20, 0)
            await asyncio.sleep(.1)
            self.ledSerial('LEDWRITE', 21, 0)
    def blink(self, param1, param2, param3):
        string = "<LEDBLINK" + "\0" + str(param1) + "\0" + str(param2) + "\0" + str(param3) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    def serialFan(self, comand, id):
        status = 0 if self.btnFan1.status == 0 else 1
        print(id)
        servoComand = 'SERVOOPEN' if comand == 'FANON' else 'SERVOCLOSE'
        if id == '1':
            self.servo(servoComand, 11)
        string = f"<{comand}"+ "\0" + id+">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    def blackout(self):
        string = "<BLACKOUT>"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    async def serverBlink(self, btn):
        self.change_img(btn)
        status = 0 if btn.status == 0 else 1
        if status == 1:
            await asyncio.sleep(.01)
            self.blink(4, 400, 700)
            await asyncio.sleep(.3)
            self.blink(5, 650, 300)
            await asyncio.sleep(.1)
            self.blink(6, 500,900)
            await asyncio.sleep(.01)
        else:
            await asyncio.sleep(.01)
            self.ledSerial('LEDWRITE', 4, 0)
            await asyncio.sleep(.2)
            self.ledSerial('LEDWRITE', 5, 0)
            await asyncio.sleep(.1)
            self.ledSerial('LEDWRITE', 6, 0)
            await asyncio.sleep(.01)

    def default(self):
        string = "<DEFAULT>"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    async def show(self):
        while True:
            self.root.update()
            await asyncio.sleep(.1)

    def change_img(self, btn):
        btn.status = not btn.status
        if (btn.status  == 1):
            print('active')
            btn.config(image=btn.active)
        else:
            print('disabled')
            btn.config(image=btn.pasive)
        return btn

    def switchCam(self, camInstance):
        if(camInstance != ''):
            for camVal in self.cams:
                camVal.config(image=camInstance.pasive)
                camVal["state"] = "active"
            self.change_img(camInstance)
            camInstance["state"] = "disable"

    async def camEnable(self, camName, cam):
        self.switchCam(cam)
        print(camName)
        for smokeVal in self.cams:
            smokeVal["state"]="disabled"
        num = randrange(1000000)
        print('cur:' + str(num))
        try:
            prev = getattr(self, 'prev')
            print('prev:'+str(prev))
            getattr(self, str(prev)+'_event').set()
        except:
            print('gas')
        setattr(self, 'prev', num)
        prevEvent = str(num)+'_event'
        setattr(self, prevEvent, Event())
        setattr(self, str(num), camThread("Camera 1", camName, getattr(self, prevEvent)))
        getattr(self, str(num)).start()
        print('started')
        await asyncio.sleep(3)
        for smokeVal in self.cams:
            smokeVal["state"]="active"



    async  def scenary_action_1(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(3,''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(2)
        self.ledSerial('LEDWRITE', 38, 255)
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 38, 0)
        await asyncio.sleep(1)
        self.fireSerialSingle(2)
        await asyncio.sleep(1)
        #TODO smoke
        self.smokeSerial(1)
        await asyncio.sleep(3)
        self.blink(1, 200, 200)
        await self.sound()
        await asyncio.sleep(7)
        self.servo('SERVOOPEN', 8)
        await asyncio.sleep(1)
        self.serialFan('FANON','1')
        await asyncio.sleep(10)
        await self.sound()
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 38, 255)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 1, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 2, 0)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()
        self.change_img(btn)

    async def scenary_action_2(self, btn):
        self.change_img(btn)
        self.blackout()
        self.loop.create_task(self.camEnable(6,''))
        for scen in self.scenaries:
            scen["state"] = "disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(2)
        self.ledSerial('LEDWRITE', 37, 255)
        await asyncio.sleep(2)
        self.blink(4, 400, 700)
        await asyncio.sleep(.3)
        self.blink(5, 650, 300)
        await asyncio.sleep(.1)
        self.blink(6, 500, 900)
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 37, 0)
        await asyncio.sleep(.01)
        self.ledSerial('LEDWRITE', 4, 0)
        await asyncio.sleep(.2)
        self.ledSerial('LEDWRITE', 5, 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', 6, 0)
        await asyncio.sleep(1)
        self.fireSerialSingle(3)
        await asyncio.sleep(1)
        #TODO smoke
        self.smokeSerial(0)
        await asyncio.sleep(3)
        self.blink(7, 200, 200)
        await self.sound()
        await asyncio.sleep(7)
        self.servo('SERVOOPEN', 7)
        await asyncio.sleep(1)
        self.servo('SERVOOPEN', 8)
        await asyncio.sleep(1)
        self.serialFan('FANON','1')
        await asyncio.sleep(10)
        await self.sound()
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 37, 255)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 7, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 3, 0)
        await asyncio.sleep(1)
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.default()
        self.change_img(btn)


    async def scenary_action_3(self, btn):
        self.change_img(btn)
        self.blackout()
        self.loop.create_task(self.camEnable(5,''))
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(2)
        self.ledSerial('LEDWRITE', 34, 255)
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 34, 0)
        await asyncio.sleep(1)
        self.fireSerialSingle(14)
        await asyncio.sleep(1)
        #TODO smoke
        self.smokeSerial(2)
        await asyncio.sleep(3)
        self.blink(15, 200, 200)
        await self.sound()
        await asyncio.sleep(7)
        self.servo('SERVOOPEN', 10)
        await asyncio.sleep(1)
        self.servo('SERVOOPEN', 9)
        await asyncio.sleep(1)
        self.serialFan('FANON','1')
        await asyncio.sleep(10)
        await self.sound()
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 34, 255)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 15, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 14, 0)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()
        self.change_img(btn)

    async def sound(self):
        self.alarmStatus = not self.alarmStatus
        if self.alarmStatus == 1:
            mixer.music.load('siren.mp3')  # Loading Music File
            mixer.music.play()
            await asyncio.sleep(.1)
        else:
            mixer.music.stop()

    async def fireFighterSound(self):
        self.fireFighterStatus = not self.fireFighterStatus
        if self.fireFighterStatus == 1:
            mixer.music.load('img/firetruck.mp3')  # Loading Music File
            mixer.music.play(fade_ms=2000)
            await asyncio.sleep(.1)
        else:
            mixer.music.stop()

    async def emergencyLight(self, btn):
        self.change_img(btn)
        status = 0 if btn.status == 0 else 255
        self.ledSerial("LEDWRITE", 21, status)
        await asyncio.sleep(.01)
        self.ledSerial("LEDWRITE", 20, status)


    async def scenary_action_4(self, btn):
        self.change_img(btn)
        self.blackout()
        self.loop.create_task(self.camEnable(5,''))
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(2)
        self.ledSerial('LEDWRITE', 35, 255)
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 35, 0)
        await asyncio.sleep(1)
        self.fireSerialSingle(13)
        await asyncio.sleep(1)
        #TODO smoke
        self.smokeSerial(6)
        await asyncio.sleep(3)
        self.blink(12, 200, 200)
        await self.sound()
        await asyncio.sleep(7)
        self.servo('SERVOOPEN', 10)
        await asyncio.sleep(1)
        self.serialFan('FANON','1')
        await asyncio.sleep(10)
        await self.sound()
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 35, 255)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 13, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 34, 0)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()
        self.change_img(btn)

    async def scenary_action_5(self, btn):
        self.change_img(btn)
        self.blackout()
        self.loop.create_task(self.camEnable(1,''))
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ##############
        print('dwad')
        await asyncio.sleep(2)
        self.ledSerial('LEDWRITE', 47, 255)
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 47, 0)
        await asyncio.sleep(1)
        self.fireSerialSingle(8)
        await asyncio.sleep(3)
        self.smokeSerial(5)
        await asyncio.sleep(3)
        await self.sound()
        self.blink(11, 200, 200)
        await asyncio.sleep(7)
        self.ledSerial('LEDWRITE', 10, 255)
        await asyncio.sleep(.9)
        self.ledSerial('LEDWRITE', 10, 0)
        #TODO smoke
        await asyncio.sleep(1)
        await asyncio.sleep(7)
        #TODO change door
        self.servo('SERVOOPEN', 12)
        await asyncio.sleep(1)
        self.servo('SERVOOPEN', 13)
        await asyncio.sleep(1)
        self.serialFan('FANON','1')
        await asyncio.sleep(10)
        await self.sound()
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 47, 255)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 8, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 11, 0)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()
        self.change_img(btn)

    async def scenary_action_6(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(2,''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"]="disable"
        self.btnScenary["state"] = "disable"
        ###################
        await asyncio.sleep(2)
        self.ledSerial('LEDWRITE', 33, 255)
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 33, 0)
        await asyncio.sleep(1)
        self.fireSerialSingle(23)
        await asyncio.sleep(3)
        self.smokeSerial(4)
        await asyncio.sleep(3)
        await self.sound()
        self.blink(22, 200, 200)
        await asyncio.sleep(7)
        #TODO smoke
        #TODO change door
        self.servo('SERVOOPEN', 14)
        await asyncio.sleep(1)
        self.serialFan('FANON','1')
        await asyncio.sleep(10)
        await self.sound()
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 33, 255)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 22, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 23, 0)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"]="active"
        self.btnScenary["state"] = "active"
        self.default()
        self.change_img(btn)

    async def scenary_action_7(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(0,''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"]="disable"
        await asyncio.sleep(2)
        self.ledSerial('LEDWRITE', 48, 255)
        await asyncio.sleep(5)
        self.ledSerial('LEDWRITE', 48, 0)
        self.fireSerialSingle(30)
        await asyncio.sleep(10)
        self.smokeSerial(3, 10000)
        await asyncio.sleep(4)
        self.fireSerialSingle(27)
        await asyncio.sleep(7)
        self.fireSerialSingle(29)
        await asyncio.sleep(1)
        #TODO smoke
        await asyncio.sleep(1)
        await self.fireFighterSound()
        await asyncio.sleep(1)
        self.blink(31, 200, 200)
        await asyncio.sleep(.3)
        self.blink(28, 200, 200)
        await asyncio.sleep(10)
        self.serialFan('FANON','2')
        await asyncio.sleep(10)
        await self.fireFighterSound()
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', 30, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 27, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 29, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 31, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 28, 0)
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', 48, 255)
        await asyncio.sleep(10)
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.default()
        self.change_img(btn)

    async def new(self):
        self.scenary = Toplevel()
        self.scenary.geometry("1020x600")
        self.scenary.config(background='#ffffff')
        self.scenary.geometry("%dx%d" % (1024, 600))


        self.btn_father_sc = WD_Button(self.scenary)

        self.scenary1 = self.btn_father_sc.btn(self.img_father.scenary_1, self.img_father.scenary_active_1,
                                            lambda: self.loop.create_task(self.scenary_action_1(self.scenary1)), 0, 400, 50)
        self.scenary1.place(x=100, y=100)  # floor 3 l

        self.scenary2 = self.btn_father_sc.btn(self.img_father.scenary_2, self.img_father.scenary_active_2,
                                            lambda: self.loop.create_task(self.scenary_action_2(self.scenary2)), 0, 400, 50)
        self.scenary2.place(x=100, y=170)  # floor 3 l

        self.scenary3 = self.btn_father_sc.btn(self.img_father.scenary_3, self.img_father.scenary_active_3,
                                            lambda: self.loop.create_task(self.scenary_action_3(self.scenary3)), 0, 400, 50)
        self.scenary3.place(x=100, y=240)  # floor 3 l

        self.scenary4 = self.btn_father_sc.btn(self.img_father.scenary_4, self.img_father.scenary_active_4,
                                            lambda: self.loop.create_task(self.scenary_action_4(self.scenary4)), 0, 400, 50)
        self.scenary4.place(x=520, y=100)  # floor 3 l

        self.scenary5 = self.btn_father_sc.btn(self.img_father.scenary_5, self.img_father.scenary_active_5,
                                            lambda: self.loop.create_task(self.scenary_action_7(self.scenary5)), 0, 400, 50)
        self.scenary5.place(x=300, y=300)  # floor 3 l

        self.scenary6 = self.btn_father_sc.btn(self.img_father.scenary_6, self.img_father.scenary_active_6,
                                            lambda: self.loop.create_task(self.scenary_action_6(self.scenary6)), 0, 400, 50)

        self.scenary6.place(x=520, y=240)  # floor 3 l

        self.scenary7 = self.btn_father_sc.btn(self.img_father.scenary_7, self.img_father.scenary_active_7,
                                            lambda: self.loop.create_task(self.scenary_action_5(self.scenary7)), 0, 400, 50)
        self.scenary7.place(x=520, y=170)  # floor 3 l

        self.scenaries = [self.scenary1, self.scenary2, self.scenary3, self.scenary4, self.scenary5, self.scenary6, self.scenary7]

        self.btnScenary = self.btn_father_sc.btn(self.img_father.scenary_btn,self.img_father.scenary_btn,
                                                 lambda: self.loop.create_task(self.scenary_close()), 0, 222, 46)
        self.btnScenary.place(x=20, y=20)

        self.btnVolumeUp = self.btn_father_sc.btn(self.img_father.volumeUp, self.img_father.volumeUp,
                                               lambda: self.loop.create_task(self.volumeUp()), 0)
        self.btnVolumeDown = self.btn_father_sc.btn(self.img_father.volumeDown, self.img_father.volumeDown,
                                                 lambda: self.loop.create_task(self.volumeDown()), 0)
        self.btnVolumeUp.place(x=870, y=20)
        self.btnVolumeDown.place(x=800, y=20)

    async def scenary_close(self):
        self.scenary.destroy()

    async def fireplace(self, index, fpalce):
        self.change_img(fpalce)

    async def tree(self, index, tree):
        self.change_img(tree)
        status = 0 if tree.status == 0 else 255
        self.ledSerial("LEDWRITE", index, status)

    async def door(self, index, door):
        self.change_img(door)
        comand = 'SERVOOPEN' if door.status == 1 else 'SERVOCLOSE'
        self.servo(comand, index)

    async def led(self, index, led):
        self.change_img(led)
        status = 0 if led.status == 0 else 255
        self.ledSerial("LEDWRITE", index, status)

    async def light(self, index, light):
        self.change_img(light)
        status = 0 if light.status == 0 else 255
        self.ledSerial("LEDWRITE", index, status)

    async def fan(self, fan, id):
        self.change_img(fan)
        comand = 'FANOFF' if fan.status == 0 else 'FANON'
        self.serialFan(comand, str(id))

    async def smoke(self, index, smoke, time = 5000):
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"]="disabled"
        self.smokeSerial(index)
        await asyncio.sleep(5)
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"]="active"
    def fakeSmoke(self, index, smoke):
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"]="disabled"
        self.smokeSerial(index)
        time.sleep(11)
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"]="active"
    async def fire(self, index1, index2, fire):
        self.change_img(fire)
        status = 0 if fire.status == 0 else 255
        if status == 0:
            self.ledSerial("LEDWRITE", index1, 0)
            self.ledSerial("LEDWRITE", index2, 0)
        else:
            self.fireSerial(index1, index2)

    async def fireSingle(self, index1, fire):
        self.change_img(fire)
        status = 0 if fire.status == 0 else 255
        if status == 0:
            self.ledSerial("LEDWRITE", index1, 0)
        else:
            self.fireSerialSingle(index1)

    async def alarm(self, index, alarm):
        self.change_img(alarm)
        status = 0 if alarm.status == 0 else 255
        if status == 0:
            self.ledSerial('LEDWRITE',index, 0)
        else:
            self.blink(index, 200, 200)
        print('alarm' + str(index))

    async def hair(self, index, hair):
        self.change_img(hair)
        status = 0 if hair.status == 0 else 255
        self.ledSerial("LEDWRITE", index, status)
        print('hair' + str(index))

    async def panel(self, index, panel):
        self.change_img(panel)
        status = 0 if panel.status == 0 else 255
        if status == 0:
            self.ledSerial('LEDWRITE',index, 0)
        else:
            self.blink(index, 200, 200)
        print('alarm' + str(index))
    async def volumeDown(self):
        self.keyboard.press(Key.media_volume_down)


    async def volumeUp(self):
        self.keyboard.press(Key.media_volume_up)


def main():
    asyncio.run(App().exec())

main()
