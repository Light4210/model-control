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

siren = mixer.Sound('siren.mp3')
egg = mixer.Sound('egg.mp3')
fire = mixer.Sound('kotel_fire.mp3')

childFire = mixer.Sound('child_fire.mp3')
kotelFire = mixer.Sound('kotel_fire.mp3')
sleepFire = mixer.Sound('sleep_fire.mp3')
balonFire = mixer.Sound('balon.mp3')

preFire = mixer.Sound('child_pre_fire.mp3')
spark = mixer.Sound('spark.mp3')

def camPreview(previewName, camID, event):
    cam = cv2.VideoCapture(camID, cv2.CAP_DSHOW)
    cam.set(cv2.CAP_PROP_FPS, 30.0)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        cv2.namedWindow(previewName, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(previewName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
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

        self.scenary_1 = "img/child.png"
        self.scenary_active_1 = "img/child-active.png"

        self.scenary_2 = "img/cotel.png"
        self.scenary_active_2 = "img/cotel-active.png"

        self.scenary_3 = "img/sleep.png"
        self.scenary_active_3 = "img/sleep-active.png"

        self.scenary_4 = "img/main.png"
        self.scenary_active_4 = "img/main-active.png"

        self.scenary_5 = "img/kitchen.png"
        self.scenary_active_5 = "img/kitchen-active.png"

        self.scenary_6 = "img/scenary-5.png"
        self.scenary_active_6 = "img/scenary-active-5.png"

        self.door = "img/door.png"
        self.door_active = "img/door-active.png"

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
        btn = Button(self.root, text="", image=getattr(self, ret), borderwidth=0, activebackground='#ffffff',
                     background='#ffffff',
                     relief=SUNKEN, command=command)
        btn.status = status
        btn.active = self.active
        btn.pasive = self.pasive
        return btn


class Window(Tk):

    def __init__(self, loop):
        self.fireFighterStatus = 0;
        self.room1 = 'room1'
        self.room2 = 'room2'
        self.room3 = 'room3'
        self.room4 = 'room4'
        self.room5 = 'room5'
        self.room6 = 'room6'
        self.room7 = 'room7'
        self.room8 = 'room8'
        self.room9 = 'room9'
        self.room10 = 'room10'

        self.camera = 'camera'
        self.generalLight = 'generaLight'
        self.roomLight = 'roomLight'
        self.smokeName = 'smoke'
        self.doorName = 'door'
        self.signal = 'signal'
        self.detection = 'detection'
        self.fireRed = 'fireRed'
        self.fireYellow = 'fireYellow'
        self.action1 = 'action1'
        self.action2 = 'action2'
        self.firePlaceYellow = 'firePlaceYellow'
        self.firePlaceRed = 'firePlaceRed'

        self.roomKeys = {
            self.room1: {
                self.camera: 2,
                self.generalLight: 40,
                self.roomLight: 49,
                self.smokeName: 7,
                self.doorName: 3,
                self.signal: 0,
                self.fireRed: 10,
                self.fireYellow: 11,
                self.action1: 12,
                self.action2: 13
            },
            self.room2: {
                self.camera: 0,
                self.generalLight: 41,
                self.roomLight: 18,
                self.smokeName: 8,
                self.doorName: 1,
                self.detection: 7,
                self.signal: 1,
                self.firePlaceRed: 16,
                self.firePlaceYellow: 17,
                self.fireRed: 14,
                self.fireYellow: 15,
                self.action1: 19,
            },
            self.room3: {
                self.camera: 5,
                self.generalLight: 42,
                self.roomLight: 50,
                self.detection: 8,
                self.doorName: 0,
                self.signal: 2,
                self.fireRed: 10,
                self.fireYellow: 11,
                self.action1: 20,
                self.action2: 21
            },
            self.room4: {
                self.camera: 4,
                self.generalLight: 43,
                self.roomLight: 51,
                self.smokeName: 6,
                self.doorName: 4,
                self.signal: 3,
                self.detection: 9,
                self.fireRed: 23,
                self.firePlaceRed: 24,
                self.firePlaceYellow: 25,
                self.action1: 27,
            },
            self.room5: {
                self.camera: 3,
                self.generalLight: 44,
                self.roomLight: 52,
                self.smokeName: 10,
                self.doorName: 5,
                self.signal: 4,
                self.fireRed: 28,
                self.action1: 29,
            },
            self.room6: {
                self.camera: 1,
                self.generalLight: 45,
                self.roomLight: 53,
                self.smokeName: 9,
                self.doorName: 2,
                self.signal: 5,
                self.fireRed: 30,
                self.fireYellow: 31,
                self.action1: 32,
            },
            self.room7: {
                self.generalLight: 48,
                self.roomLight: 34,
            },
            self.room8: {
                self.generalLight: 47,
                self.roomLight: 35,
            },
            self.room9: {
                self.generalLight: 46,
                self.roomLight: 36,
            },
            self.room10: {
                self.camera: 3,
                self.generalLight: 54,
                self.smokeName: 11,
                self.fireRed: 38,
                self.fireYellow: 39,
                self.action1: 37

            }
        }
        self.alarmStatus = 0
        self.eggStatus = 0
        self.fireStatus = 0
        self.sparkStatus = 0

        self.childFireStatus = 0
        self.kotelFireStatus = 0
        self.sleepFireStatus = 0
        self.balonFireStatus = 0
        self.preFireStatus = 0

        self.fireCount = 0;
        self.volume = 50;
        self.keyboard = Controller()
        self.arduino = serial.Serial(port='COM10', baudrate=57600)
        self.loop = loop
        self.name = 'frame'
        self.status = False
        self.root = Tk()
        self.root.config(background='#ffffff')
        self.keyboard = Controller()
        width = 1024
        height = 600
        #primary_screen = monitors[1]  # Assuming the primary screen is the first one

        # Set the window geometry to open on the primary screen and located on the left
        self.root.geometry("%dx%d%+d%+d" % (width, height, 0, 0))

        self.app_backround = ImageTk.PhotoImage(Image.open("img/back.png").resize((1024, 585)))
        self.label1 = Label(self.root, image=self.app_backround, background='#ffffff', padx=50, pady=50)
        self.label1.place(x=0, y=0)
        self.img_father = WD_Images(self.root)
        self.btn_father = WD_Button(self.root)

        self.btnManual = self.btn_father.btn(self.img_father.manual, self.img_father.manual,
                                             lambda: self.loop.create_task(self.new()), 0, 222, 46)

        self.btnDoor5 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(5, self.btnDoor5)), 0)
        self.btnDoor2 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(2, self.btnDoor2)), 0)
        self.btnDoor0 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(0, self.btnDoor0)), 0)
        self.btnDoor4 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(4, self.btnDoor4)), 0)
        self.btnDoor3 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(3, self.btnDoor3)), 0)
        self.btnDoor1 = self.btn_father.btn(self.img_father.door, self.img_father.door_active,
                                            lambda: self.loop.create_task(self.door(1, self.btnDoor1)), 0)

        self.btnLed0 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room5][self.generalLight], self.btnLed0)),
                                           1)  # child
        self.btnLed1 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room6][self.generalLight], self.btnLed1)),
                                           1)  # sleep
        self.btnLed2 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room3][self.generalLight], self.btnLed2)),
                                           1)  # batroom
        self.btnLed3 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room9][self.generalLight], self.btnLed3)),
                                           1)  # middle3
        self.btnLed4 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room8][self.generalLight], self.btnLed4)), 1)
        self.btnLed5 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room4][self.generalLight], self.btnLed5)), 1)
        self.btnLed6 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room1][self.generalLight], self.btnLed6)),
                                           1)  # kitchen
        self.btnLed7 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room7][self.generalLight], self.btnLed7)),
                                           1)  # middle1
        self.btnLed8 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room2][self.generalLight], self.btnLed8)),
                                           1)  # kotel
        self.btnLed9 = self.btn_father.btn(self.img_father.led, self.img_father.led_active,
                                           lambda: self.loop.create_task(
                                               self.led(self.roomKeys[self.room10][self.generalLight], self.btnLed9)),
                                           1)  # kotel

        self.btnLight0 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light(self.roomKeys[self.room5][self.roomLight], self.btnLight0)),
                                             1)
        self.btnLight1 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light(self.roomKeys[self.room6][self.roomLight], self.btnLight1)),
                                             1)  # sleep
        self.btnLight2 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light(self.roomKeys[self.room3][self.roomLight], self.btnLight2)),
                                             1)
        self.btnLight3 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light(self.roomKeys[self.room9][self.roomLight], self.btnLight3)),
                                             1)
        self.btnLight4 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light((self.roomKeys[self.room8][self.roomLight]),
                                                            self.btnLight4)), 1)
        self.btnLight5 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light(self.roomKeys[self.room4][self.roomLight], self.btnLight5)),
                                             1)
        self.btnLight6 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light(self.roomKeys[self.room1][self.roomLight], self.btnLight6)),
                                             1)  # kitchen
        self.btnLight7 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light(self.roomKeys[self.room7][self.roomLight], self.btnLight7)),
                                             1)
        self.btnLight8 = self.btn_father.btn(self.img_father.light, self.img_father.light_active,
                                             lambda: self.loop.create_task(
                                                 self.light(self.roomKeys[self.room2][self.roomLight], self.btnLight8)),
                                             1)

        self.btnSmoke0 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(
                                                 self.smoke(self.roomKeys[self.room5][self.smokeName], self.btnSmoke0)),
                                             0)
        self.btnSmoke1 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(
                                                 self.smoke(self.roomKeys[self.room6][self.smokeName], self.btnSmoke1)),
                                             0)
        self.btnSmoke2 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(
                                                 self.smoke(self.roomKeys[self.room10][self.smokeName], self.btnSmoke2,
                                                            2000)), 0)
        self.btnSmoke3 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(
                                                 self.smoke(self.roomKeys[self.room4][self.smokeName], self.btnSmoke3)),
                                             0)
        self.btnSmoke4 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(
                                                 self.smoke(self.roomKeys[self.room1][self.smokeName], self.btnSmoke4)),
                                             0)
        self.btnSmoke5 = self.btn_father.btn(self.img_father.smoke, self.img_father.smoke_active,
                                             lambda: self.loop.create_task(
                                                 self.smoke(self.roomKeys[self.room2][self.smokeName], self.btnSmoke5)),
                                             0)

        self.btnCam1 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(
                                               self.camEnable(self.roomKeys[self.room5][self.camera], self.btnCam1)), 0)
        self.btnCam2 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(
                                               self.camEnable(self.roomKeys[self.room6][self.camera], self.btnCam2)), 0)
        self.btnCam3 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(
                                               self.camEnable(self.roomKeys[self.room3][self.camera], self.btnCam3)), 0)
        self.btnCam4 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(
                                               self.camEnable(self.roomKeys[self.room4][self.camera], self.btnCam4)), 0)
        self.btnCam5 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(
                                               self.camEnable(self.roomKeys[self.room1][self.camera], self.btnCam5)), 0)
        self.btnCam6 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(
                                               self.camEnable(self.roomKeys[self.room2][self.camera], self.btnCam6)), 0)
        self.btnCam7 = self.btn_father.btn(self.img_father.cam, self.img_father.cam_active,
                                           lambda: self.loop.create_task(
                                               self.camEnable(self.roomKeys[self.room10][self.camera], self.btnCam7)),
                                           0)

        self.btnFire1 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(
                                                self.fireSingle(self.roomKeys[self.room5][self.fireRed],
                                                                self.btnFire1)), 0)
        self.btnFire2 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(
                                                self.fire(self.roomKeys[self.room6][self.fireRed],
                                                          self.roomKeys[self.room6][self.fireYellow], self.btnFire2)),
                                            0)
        self.btnFire3 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(
                                                self.fire(self.roomKeys[self.room1][self.fireRed],
                                                          self.roomKeys[self.room1][self.fireYellow], self.btnFire3)),
                                            0)
        self.btnFire4 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(
                                                self.fireSingle(self.roomKeys[self.room4][self.fireRed],
                                                                self.btnFire4)), 0)
        self.btnFire6 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(
                                                self.fire(self.roomKeys[self.room2][self.fireRed],
                                                          self.roomKeys[self.room2][self.fireYellow], self.btnFire6)),
                                            0)
        self.btnFire7 = self.btn_father.btn(self.img_father.fire, self.img_father.fire_active,
                                            lambda: self.loop.create_task(
                                                self.fireSingle(self.roomKeys[self.room10][self.action1],
                                                                self.btnFire7)), 1)

        self.btnAlarm1 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(
                                                 self.alarm(self.roomKeys[self.room5][self.signal], self.btnAlarm1)),
                                                      self.loop.create_task(self.sound())], 0)
        self.btnAlarm2 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(
                                                 self.alarm(self.roomKeys[self.room6][self.signal], self.btnAlarm2)),
                                                      self.loop.create_task(self.sound())], 0)
        self.btnAlarm3 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(
                                                 self.alarm(self.roomKeys[self.room1][self.signal], self.btnAlarm3)),
                                                      self.loop.create_task(self.sound())], 0)
        self.btnAlarm4 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(
                                                 self.alarm(self.roomKeys[self.room3][self.signal], self.btnAlarm4)),
                                                      self.loop.create_task(self.sound())], 0)
        self.btnAlarm5 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(
                                                 self.alarm(self.roomKeys[self.room4][self.signal], self.btnAlarm5)),
                                                      self.loop.create_task(self.sound())], 0)
        self.btnAlarm6 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(
                                                 self.alarm(self.roomKeys[self.room2][self.signal], self.btnAlarm6)),
                                                      self.loop.create_task(self.sound())], 0)
        self.btnAlarm7 = self.btn_father.btn(self.img_father.alarm, self.img_father.alarm_active,
                                             lambda: [self.loop.create_task(
                                                 self.alarmFireTruck(self.roomKeys[self.room10][self.fireRed],
                                                                     self.roomKeys[self.room10][self.fireYellow],
                                                                     self.btnAlarm7)),
                                                      self.loop.create_task(self.fireFighterSound())], 0)

        self.btnHair5 = self.btn_father.btn(self.img_father.wilka, self.img_father.wilka_active,
                                            lambda: self.loop.create_task(
                                                self.fireSingle(self.roomKeys[self.room6][self.action1],
                                                                self.btnHair5)), 1)
        self.btnHair6 = self.btn_father.btn(self.img_father.hair_dryer, self.img_father.hair_dryer_active,
                                            lambda: self.loop.create_task(
                                                self.fireSingle(self.roomKeys[self.room3][self.action1],
                                                                self.btnHair6)), 1)

        self.btnVolumeUp = self.btn_father.btn(self.img_father.volumeUp, self.img_father.volumeUp,
                                               lambda: self.loop.create_task(self.volumeUp()), 0)
        self.btnVolumeDown = self.btn_father.btn(self.img_father.volumeDown, self.img_father.volumeDown,
                                                 lambda: self.loop.create_task(self.volumeDown()), 0)

        self.btnFirepalce = self.btn_father.btn(self.img_father.fireplace, self.img_father.fireplace_active,
                                                lambda: self.loop.create_task(
                                                    self.fire(self.roomKeys[self.room4][self.firePlaceRed],
                                                              self.roomKeys[self.room4][self.firePlaceYellow],
                                                              self.btnFirepalce)), 1)
        self.btnTree = self.btn_father.btn(self.img_father.tree, self.img_father.tree_active,
                                           lambda: self.loop.create_task(
                                               self.fireSingle(self.roomKeys[self.room4][self.action1], self.btnTree)),
                                           1)

        self.btnPanel3 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(
                                                 self.panel(self.roomKeys[self.room2][self.detection], self.btnPanel3)),
                                             0)
        self.btnPanel4 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(
                                                 self.panel(self.roomKeys[self.room2][self.detection], self.btnPanel4)),
                                             0)
        self.btnPanel5 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(
                                                 self.panel(self.roomKeys[self.room4][self.detection], self.btnPanel5)),
                                             0)
        self.btnPanel6 = self.btn_father.btn(self.img_father.panel, self.img_father.panel_active,
                                             lambda: self.loop.create_task(
                                                 self.panel(self.roomKeys[self.room3][self.detection], self.btnPanel6)),
                                             0)
        self.btnPanel7 = self.btn_father.btn(self.img_father.cook, self.img_father.cook_active,
                                             lambda: self.loop.create_task(
                                                 self.fireSingle(self.roomKeys[self.room1][self.action1],
                                                                 self.btnPanel7)), 1)

        self.btnTorch = self.btn_father.btn(self.img_father.torch, self.img_father.torch_active,
                                            lambda: self.loop.create_task(
                                                self.fireSingle(self.roomKeys[self.room5][self.action1],
                                                                self.btnTorch)), 1)
        self.btnFan1 = self.btn_father.btn(self.img_father.vent, self.img_father.vent_active,
                                           lambda: self.loop.create_task(self.fan(1, self.btnFan1)), 0)
        self.btnFan2 = self.btn_father.btn(self.img_father.vent, self.img_father.vent_active,
                                           lambda: self.loop.create_task(self.fan(2, self.btnFan2)), 0)
        self.btnBalon = self.btn_father.btn(self.img_father.balon, self.img_father.balon_active,
                                            lambda: self.loop.create_task(
                                                self.light(self.roomKeys[self.room2][self.action1], self.btnBalon)), 0)
        self.btnKotel = self.btn_father.btn(self.img_father.kotel, self.img_father.kotel_active,
                                            lambda: self.loop.create_task(
                                                self.fireSingle(self.roomKeys[self.room3][self.action2],
                                                                self.btnKotel)), 1)
        self.btnHot = self.btn_father.btn(self.img_father.kotel, self.img_father.kotel_active,
                                          lambda: self.loop.create_task(
                                              self.fire(self.roomKeys[self.room2][self.firePlaceYellow],
                                                        self.roomKeys[self.room2][self.firePlaceRed], self.btnHot)), 1)

        self.btnTorch.place(x=350, y=158)
        self.btnHair5.place(x=915, y=212)  # floor 3 l
        self.btnFan1.place(x=550, y=505)  # floor 3 l
        self.btnBalon.place(x=915, y=505)  # floor 3 l
        self.btnHot.place(x=915, y=450)  # floor 3 l
        self.btnKotel.place(x=350, y=353)  # floor 3 l

        self.btnManual.place(x=20, y=20)

        self.btnDoor5.place(x=185, y=212)  # floor 3 l
        self.btnDoor2.place(x=697, y=212)  # floor 3 r
        self.btnDoor0.place(x=185, y=353)  # floor 2 l
        self.btnDoor4.place(x=697, y=353)  # floor 2 r
        self.btnDoor3.place(x=185, y=505)  # floor 1 l
        self.btnDoor1.place(x=697, y=505)  # floor 1 r

        self.btnLed0.place(x=240, y=212)  # floor 3 l
        self.btnLed1.place(x=750, y=212)  # floor 3 l
        self.btnLed2.place(x=240, y=353)  # floor 3 l
        self.btnLed5.place(x=750, y=353)  # floor 3 l
        self.btnLed6.place(x=240, y=505)  # floor 3 l
        self.btnLed8.place(x=750, y=505)  # floor 3 l
        self.btnLed8.place(x=750, y=505)  # floor 3 l
        self.btnLed3.place(x=470, y=212)  # floor 3 l
        self.btnLed4.place(x=470, y=353)  # floor 3 l
        self.btnLed7.place(x=470, y=505)  # floor 3 l

        self.btnLight0.place(x=295, y=212)  # floor 3 l
        self.btnLight1.place(x=805, y=212)  # floor 3 l
        self.btnLight2.place(x=295, y=353)  # floor 3 l
        self.btnLight5.place(x=805, y=353)  # floor 3 l
        self.btnLight6.place(x=295, y=505)  # floor 3 l
        self.btnLight8.place(x=805, y=505)  # floor 3 l
        self.btnLight8.place(x=805, y=505)  # floor 3 l
        self.btnLight3.place(x=470, y=155)  # floor 3 l
        self.btnLight4.place(x=470, y=300)  # floor 3 l
        self.btnLight7.place(x=470, y=455)  # floor 3 l

        self.btnTree.place(x=915, y=353)  # floor 3 l
        self.btnFirepalce.place(x=915, y=299)  # floor 3 l

        self.btnSmoke0.place(x=350, y=212)  # floor 3 l
        self.btnSmoke1.place(x=860, y=212)  # floor 3 l
        self.btnSmoke3.place(x=860, y=353)  # floor 3 l
        self.btnSmoke4.place(x=350, y=505)  # floor 3 l
        self.btnSmoke5.place(x=860, y=505)  # floor 3 l

        self.btnCam1.place(x=185, y=158)
        self.btnCam2.place(x=697, y=158)
        self.btnCam3.place(x=185, y=299)
        self.btnCam4.place(x=697, y=299)
        self.btnCam5.place(x=185, y=450)
        self.btnCam6.place(x=697, y=450)

        self.btnFire1.place(x=240, y=158)
        self.btnFire2.place(x=750, y=158)
        self.btnFire3.place(x=240, y=450)
        self.btnFire4.place(x=750, y=299)
        self.btnFire6.place(x=750, y=450)

        self.btnAlarm1.place(x=295, y=158)
        self.btnAlarm2.place(x=805, y=158)
        self.btnAlarm3.place(x=295, y=450)
        self.btnAlarm4.place(x=240, y=299)
        self.btnAlarm5.place(x=805, y=299)
        self.btnAlarm6.place(x=805, y=450)

        self.btnHair6.place(x=295, y=299)

        self.btnPanel4.place(x=860, y=450)
        self.btnPanel5.place(x=860, y=299)
        self.btnPanel6.place(x=350, y=299)
        self.btnPanel7.place(x=350, y=450)

        self.btnVolumeUp.place(x=30, y=125)
        self.btnVolumeDown.place(x=100, y=125)

        time.sleep(3)
        self.cams = [self.btnCam6, self.btnCam5, self.btnCam4, self.btnCam3, self.btnCam2, self.btnCam1, self.btnCam7]
        self.smokes = [self.btnSmoke5, self.btnSmoke4, self.btnSmoke3, self.btnSmoke2, self.btnSmoke0, self.btnSmoke1]

    def smokeSerial(self, param1, time=1300):
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
        string = "<LEDFIREB" + "\0" + str(param1) + "\0" + str(63) + ">"
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

    def blink(self, param1, param2=200, param3=200):
        string = "<LEDBLINK" + "\0" + str(param1) + "\0" + str(param2) + "\0" + str(param3) + ">"
        print(string)
        self.arduino.write(bytes(string, 'utf-8'))
        data = self.arduino.read_all()
        print(data.decode())

    def serialFan(self, comand):
        string = f"<{comand}>"
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
        if (btn.status == 1):
            print('active')
            btn.config(image=btn.active)
        else:
            print('disabled')
            btn.config(image=btn.pasive)
        return btn

    def switchCam(self, camInstance):
        if (camInstance != ''):
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



    async def scenary_action_1(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(self.roomKeys[self.room6][self.camera], ''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"] = "disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(4)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room6][self.roomLight], 255)
        await asyncio.sleep(7)
        await self.soundPreFire()
        await asyncio.sleep(1)
        await self.soundChildFire()
        await asyncio.sleep(1)
        self.fireSerial(self.roomKeys[self.room6][self.fireRed], self.roomKeys[self.room6][self.fireYellow])
        await asyncio.sleep(3)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room6][self.roomLight], 0)
        await asyncio.sleep(1)
        self.smokeSerial(self.roomKeys[self.room6][self.smokeName])
        await asyncio.sleep(4)
        await self.sound()
        self.blink(self.roomKeys[self.room6][self.signal], 200, 200)
        await self.soundPreFire()
        self.ledSerial('LEDWRITE', self.roomKeys[self.room6][self.action1], 0)
        await asyncio.sleep(3)
        self.servo('SERVOOPEN', self.roomKeys[self.room6][self.doorName])
        await asyncio.sleep(.1)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(10)
        await self.soundChildFire()
        await self.sound()
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room6][self.signal], 0)
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room6][self.fireRed], 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room6][self.fireYellow], 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room6][self.roomLight], 255)
        await asyncio.sleep(60)
        await asyncio.sleep(.5)
        self.servo('SERVOCLOSE', self.roomKeys[self.room6][self.doorName])
        await asyncio.sleep(.5)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(.5)
        self.default()
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.change_img(btn)

    async def scenary_action_2(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(self.roomKeys[self.room2][self.camera], ''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"] = "disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(4)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.roomLight], 255)
        await asyncio.sleep(1)
        self.fireSerial(self.roomKeys[self.room2][self.firePlaceRed], self.roomKeys[self.room2][self.firePlaceYellow])
        await asyncio.sleep(4)
        await self.soundKotelFire()
        self.fireSerial(self.roomKeys[self.room2][self.fireRed], self.roomKeys[self.room2][self.fireYellow])
        await asyncio.sleep(4)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.roomLight], 0)
        await asyncio.sleep(.5)
        self.smokeSerial(self.roomKeys[self.room2][self.smokeName])
        await asyncio.sleep(4)
        await self.sound()
        self.blink(self.roomKeys[self.room2][self.signal], 200, 200)
        await asyncio.sleep(3)
        await self.soundBalonFire()
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.action1], 255)
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.action1], 0)
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.action1], 0)
        await asyncio.sleep(3)
        await self.soundBalonFire()
        self.servo('SERVOOPEN', self.roomKeys[self.room2][self.doorName])
        await asyncio.sleep(1)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(10)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.signal], 0)
        await asyncio.sleep(.1)
        await self.soundKotelFire()
        await self.sound()
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.fireRed], 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.fireYellow], 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room2][self.roomLight], 255)
        await asyncio.sleep(60)
        await asyncio.sleep(.5)
        self.servo('SERVOCLOSE', self.roomKeys[self.room2][self.doorName])
        await asyncio.sleep(.5)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(.5)
        self.default()
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.change_img(btn)

    async def scenary_action_3(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(self.roomKeys[self.room5][self.camera], ''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"] = "disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(4)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room5][self.roomLight], 255)
        await asyncio.sleep(4)
        self.fireSerialSingle(self.roomKeys[self.room5][self.action1])
        await asyncio.sleep(10)
        await self.soundSleepFire()
        self.fireSerialSingle(self.roomKeys[self.room5][self.fireRed])
        await asyncio.sleep(2)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room5][self.roomLight], 0)
        await asyncio.sleep(1)
        self.smokeSerial(self.roomKeys[self.room5][self.smokeName])
        await asyncio.sleep(4)
        self.blink(self.roomKeys[self.room5][self.signal], 200, 200)
        await self.sound()
        await asyncio.sleep(3)
        self.servo('SERVOOPEN', self.roomKeys[self.room5][self.doorName])
        await asyncio.sleep(1)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(10)
        await self.sound()
        await self.soundSleepFire()
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room5][self.signal], 0)
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room5][self.fireRed], 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room5][self.roomLight], 255)
        await asyncio.sleep(60)
        await asyncio.sleep(.5)
        self.servo('SERVOCLOSE', self.roomKeys[self.room5][self.doorName])
        await asyncio.sleep(.5)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(.5)
        self.default()
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.change_img(btn)

    async def sound(self):
        self.alarmStatus = not self.alarmStatus
        if self.alarmStatus == 1:
            mixer.music.load('siren.mp3')  # Loading Music File
            mixer.music.play()
            await asyncio.sleep(.1)
        else:
            mixer.music.stop()

    async def soundEgg(self):
        self.eggStatus = not self.eggStatus
        if self.eggStatus == 1:
            egg.play(fade_ms=1000)
            await asyncio.sleep(.1)
        else:
            egg.fadeout(1000)

    async def soundFire(self):
        self.fireStatus = not self.fireStatus
        if self.fireStatus == 1:
            fire.play(fade_ms=3000)
            await asyncio.sleep(.1)
        else:
            fire.fadeout(3000)

    async def soundPreFire(self):
        self.preFireStatus = not self.preFireStatus
        if self.preFireStatus == 1:
            preFire.play(fade_ms=3000)
            await asyncio.sleep(.1)
        else:
            preFire.fadeout(3000)


    async def soundSleepFire(self):
        self.sleepFireStatus = not self.sleepFireStatus
        if self.sleepFireStatus == 1:
            sleepFire.play(fade_ms=3000)
            await asyncio.sleep(.1)
        else:
            sleepFire.fadeout(3000)

    async def soundChildFire(self):
        self.childFireStatus = not self.childFireStatus
        if self.childFireStatus == 1:
            childFire.play(fade_ms=3000)
            await asyncio.sleep(.1)
        else:
            childFire.fadeout(3000)

    async def soundKotelFire(self):
        self.kotelFireStatus = not self.kotelFireStatus
        if self.kotelFireStatus == 1:
            kotelFire.play(fade_ms=3000)
            await asyncio.sleep(.1)
        else:
            kotelFire.fadeout(3000)

    async def soundBalonFire(self):
        self.balonFireStatus = not self.balonFireStatus
        if self.balonFireStatus == 1:
            balonFire.play()
            await asyncio.sleep(.1)
        else:
            balonFire.fadeout(3000)


    async def soundSpark(self):
        self.sparkStatus = not self.sparkStatus
        if self.sparkStatus == 1:
            spark.play()
            await asyncio.sleep(.1)
        else:
            spark.fadeout(3000)


    async def scenary_action_4(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(self.roomKeys[self.room4][self.camera], ''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"] = "disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(4)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room4][self.roomLight], 255)
        await asyncio.sleep(4)
        self.fireSerialSingle(self.roomKeys[self.room4][self.action1])
        await asyncio.sleep(1)
        self.fireSerial(self.roomKeys[self.room4][self.firePlaceRed], self.roomKeys[self.room4][self.firePlaceYellow])
        await asyncio.sleep(4)
        await self.soundSpark()
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room4][self.action1], 0)
        await asyncio.sleep(1)
        await self.soundFire()
        self.fireSerialSingle(self.roomKeys[self.room4][self.fireRed])
        await asyncio.sleep(3)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room4][self.roomLight], 0)
        await asyncio.sleep(1)
        self.smokeSerial(self.roomKeys[self.room4][self.smokeName])
        await asyncio.sleep(4)
        await self.soundSpark()
        await asyncio.sleep(.1)
        self.blink(self.roomKeys[self.room4][self.signal], 200, 200)
        await self.sound()
        await asyncio.sleep(3)
        self.servo('SERVOOPEN', self.roomKeys[self.room4][self.doorName])
        await asyncio.sleep(.2)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(10)
        await self.sound()
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room4][self.signal], 0)
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room4][self.fireRed], 0)
        await asyncio.sleep(.1)
        await self.soundFire()
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room4][self.roomLight], 255)
        await asyncio.sleep(60)
        await asyncio.sleep(.5)
        self.servo('SERVOCLOSE', self.roomKeys[self.room4][self.doorName])
        await asyncio.sleep(.5)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(.5)
        self.default()
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.change_img(btn)

    async def scenary_action_5(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(self.roomKeys[self.room1][self.camera], ''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"] = "disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(4)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room1][self.roomLight], 255)
        await asyncio.sleep(4)
        await self.soundEgg()
        self.fireSerialSingle(self.roomKeys[self.room1][self.action1])
        await asyncio.sleep(4)
        await self.soundEgg()
        await self.soundKotelFire()
        self.fireSerialSingle(self.roomKeys[self.room1][self.fireRed])
        await asyncio.sleep(3)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room1][self.roomLight], 0)
        await asyncio.sleep(1)
        self.smokeSerial(self.roomKeys[self.room1][self.smokeName])
        await asyncio.sleep(10)
        self.fireSerialSingle(self.roomKeys[self.room1][self.fireYellow])
        await asyncio.sleep(1)
        self.blink(self.roomKeys[self.room1][self.signal], 200, 200)
        await self.sound()
        await asyncio.sleep(1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room1][self.action1], 0)
        await asyncio.sleep(1)
        self.servo('SERVOOPEN', self.roomKeys[self.room1][self.doorName])
        await asyncio.sleep(1)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(10)
        await self.sound()
        await asyncio.sleep(.5)
        await self.soundKotelFire()
        self.ledSerial('LEDWRITE', self.roomKeys[self.room1][self.signal], 0)
        await asyncio.sleep(.5)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room1][self.fireRed], 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room1][self.fireYellow], 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room1][self.roomLight], 255)
        await asyncio.sleep(60)
        await asyncio.sleep(.5)
        self.servo('SERVOCLOSE', self.roomKeys[self.room1][self.doorName])
        await asyncio.sleep(.5)
        await self.fan(1, self.btnFan1)
        await asyncio.sleep(.5)
        self.default()
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.change_img(btn)

    async def scenary_action_6(self, btn):
        self.change_img(btn)
        self.loop.create_task(self.camEnable(self.roomKeys[self.room10][self.camera], ''))
        self.blackout()
        for scen in self.scenaries:
            scen["state"] = "disable"
        self.btnScenary["state"] = "disable"
        ##############
        await asyncio.sleep(4)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room10][self.generalLight], 255)
        await asyncio.sleep(4)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room10][self.generalLight], 0)
        await asyncio.sleep(3)
        self.fireSerialSingle(self.roomKeys[self.room10][self.action1])
        await asyncio.sleep(5)
        self.smokeSerial(self.roomKeys[self.room10][self.smokeName], 5000)
        await asyncio.sleep(8)
        await self.fireFighterSound()
        await self.alarmFireTruck(self.roomKeys[self.room10][self.fireRed], self.roomKeys[self.room10][self.fireYellow],
                                  self.btnAlarm7)
        await asyncio.sleep(10)
        await self.fan(2, self.btnFan2)
        await asyncio.sleep(10)
        await self.fireFighterSound()
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room10][self.fireRed], 0)
        await asyncio.sleep(.1)
        self.ledSerial('LEDWRITE', self.roomKeys[self.room10][self.fireYellow], 0)
        await asyncio.sleep(60)
        await asyncio.sleep(.5)
        await self.fan(2, self.btnFan2)
        await asyncio.sleep(.5)
        self.default()
        for scen in self.scenaries:
            scen["state"] = "active"
        self.btnScenary["state"] = "active"
        self.change_img(btn)

    async def new(self):
        self.scenary = Toplevel()
        self.scenary.geometry("1020x600")
        self.scenary.config(background='#ffffff')
        width = 1024
        height = 600
        #primary_screen = monitors[1]  # Assuming the primary screen is the first one

        # Set the window geometry to open on the primary screen and located on the left
        self.scenary.geometry("%dx%d%+d%+d" % (width, height, 0, 0))

        self.btn_father_sc = WD_Button(self.scenary)

        self.scenary1 = self.btn_father_sc.btn(self.img_father.scenary_1, self.img_father.scenary_active_1,
                                               lambda: self.loop.create_task(self.scenary_action_1(self.scenary1)), 0,
                                               400, 50)
        self.scenary1.place(x=300, y=100)  # floor 3 l

        self.scenary2 = self.btn_father_sc.btn(self.img_father.scenary_2, self.img_father.scenary_active_2,
                                               lambda: self.loop.create_task(self.scenary_action_2(self.scenary2)), 0,
                                               400, 50)
        self.scenary2.place(x=300, y=170)  # floor 3 l

        self.scenary3 = self.btn_father_sc.btn(self.img_father.scenary_3, self.img_father.scenary_active_3,
                                               lambda: self.loop.create_task(self.scenary_action_3(self.scenary3)), 0,
                                               400, 50)
        self.scenary3.place(x=300, y=240)  # floor 3 l

        self.scenary4 = self.btn_father_sc.btn(self.img_father.scenary_4, self.img_father.scenary_active_4,
                                               lambda: self.loop.create_task(self.scenary_action_4(self.scenary4)), 0,
                                               400, 50)
        self.scenary4.place(x=300, y=310)  # floor 3 l

        self.scenary5 = self.btn_father_sc.btn(self.img_father.scenary_5, self.img_father.scenary_active_5,
                                               lambda: self.loop.create_task(self.scenary_action_5(self.scenary5)), 0,
                                               400, 50)
        self.scenary5.place(x=300, y=380)  # floor 3 l

        self.scenaries = [self.scenary1, self.scenary2, self.scenary3, self.scenary4, self.scenary5]

        self.btnScenary = self.btn_father_sc.btn(self.img_father.scenary_btn, self.img_father.scenary_btn,
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

    async def fan(self, num, fan):
        self.change_img(fan)
        comand = 'FAN' + str(num) + 'OFF' if fan.status == 0 else 'FAN' + str(num) + 'ON'
        self.serialFan(comand)

    async def smoke(self, index, smoke, time=1500):
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"] = "disabled"
        self.smokeSerial(index, time)
        await asyncio.sleep(11)
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"] = "active"

    def fakeSmoke(self, index, smoke):
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"] = "disabled"
        self.smokeSerial(index)
        time.sleep(11)
        self.change_img(smoke)
        for smokeVal in self.smokes:
            smokeVal["state"] = "active"

    async def fire(self, index1, index2, fire):
        self.change_img(fire)
        status = 0 if fire.status == 0 else 255
        if status == 0:
            self.ledSerial("LEDWRITE", index1, 0)
            self.ledSerial("LEDWRITE", index2, 0)
        else:
            self.fireSerial(index1, index2)

    async def fireFighterSound(self):
        self.fireFighterStatus = not self.fireFighterStatus
        if self.fireFighterStatus == 1:
            mixer.music.load('img/firetruck.mp3')  # Loading Music File
            mixer.music.play(fade_ms=2000)
            await asyncio.sleep(.1)
        else:
            mixer.music.stop()

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
            self.ledSerial('LEDWRITE', index, 0)
        else:
            self.blink(index, 200, 200)
        print('alarm' + str(index))

    async def alarmFireTruck(self, index1, index2, alarm):
        self.change_img(alarm)
        status = 0 if alarm.status == 0 else 255
        if status == 0:
            self.ledSerial('LEDWRITE', index1, 0)
            self.ledSerial('LEDWRITE', index2, 0)

        else:
            self.blink(index1, 200, 200)
            await asyncio.sleep(.1)
            self.blink(index2, 200, 200)
        print('alarm' + str(index1))
        print('alarm' + str(index2))

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
