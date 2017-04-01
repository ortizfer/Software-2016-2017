
#importing modules required
from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
import serial
import io

#Set up GUI
window = Tk()  #Makes main window
window.wm_title("Proti")

#Label frame
labelFrame = Frame(window)
labelFrame.pack(side = TOP, fill=BOTH, pady=10)

#Labels
label1 = Label(labelFrame, text="FRONT").pack(side = LEFT, padx=150)
label2 = Label(labelFrame, text="BOTTOM").pack(side = RIGHT, padx=150)

#Camera frame
videoFrame = Frame(window)
videoFrame.pack(side = TOP, fill=X)

#Stream frames
imageFrame = Frame(videoFrame)
imageFrame.grid(row=0, column=0, padx=10)
imageFrame.pack(side = LEFT)

imageFrame1 = Frame(videoFrame)
imageFrame1.grid(row=0, column=0, padx=10)
imageFrame1.pack(side = RIGHT)

#Capture video frames - CAMERA 1
lmain = Label(imageFrame)
lmain.grid(row=0, column=0)
lmain.pack(side = LEFT, padx=20, pady=20)

cap = cv2.VideoCapture('friends-bloopers-1994-2004.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

#Capture video frames - CAMERA 2
lmain1 = Label(imageFrame1)
lmain1.grid(row=0, column=0)
lmain1.pack(side = RIGHT, padx=20, pady=20)

cap1 = cv2.VideoCapture('friends-bloopers-1994-2004.mp4')
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

#Bottom frame
bottomFrame = Frame(window)

leftFrame = Frame(bottomFrame).pack( side = LEFT, padx=20)
rightFrame = Frame(bottomFrame).pack( side = RIGHT, padx=20)

bottomFrame.pack( side = BOTTOM, padx=20, pady=20)

#Data table
tree = ttk.Treeview(leftFrame,selectmode="extended", height="2", columns=("one"))
tree.heading("#0", text="Measurement")
tree.column("#0", minwidth=100, width=100)
tree.heading("one", text="Value")
tree.column("one", minwidth=100, width=100) 

tree.insert("", 0, text="Compas", values=(0), tags=('rowOne'))
tree.insert("", 1, text="Pressure", values=(0), tags=('rowTwo'))

tree.tag_configure('rowOne', background='cyan')
tree.tag_configure('rowTwo', background='yellow')

tree.pack(side = LEFT, padx=20)

#Button Commands
def goUp():
    print("going up")

def goDown():
    print("going down")
    
def stop():
    print("stop")
    
def goForward():
    print("move forward")

def turnRight():
    print("turn right")

def turnLeft():
    print("turn left")

def goBackward():
    print("move backward")

#Buttons
upDownFrame = Frame(rightFrame)
upButton = Button(upDownFrame, text = "Go Up", command=goUp).pack( side = TOP )
downButton = Button(upDownFrame, text = "Go Down", command=goDown).pack( side = TOP )
stopButton = Button(upDownFrame, text = "Stop", command=stop).pack( side = TOP)
upDownFrame.pack( side = RIGHT, padx=30, pady=10)

joystick = Frame(rightFrame)
forwardButton = Button(joystick, text = "Forward", command=goForward).pack( side = TOP )
leftButton = Button(joystick, text = "Left", command=turnLeft).pack( side = LEFT)
rightButton = Button(joystick, text = "Right", command=turnRight).pack( side = RIGHT)
backButton = Button(joystick, text = "Backward", command=goBackward).pack( side = BOTTOM)
joystick.pack( side = RIGHT, padx=30 )

#Configure video stream - Camera 1
def show_frame():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(20, show_frame) 

#Configure video stream - Camera 2
def show_frame2():
    _, frame = cap1.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain1.imgtk = imgtk
    lmain1.configure(image=imgtk)
    lmain1.after(20, show_frame2) 

#Mapping keyboard to commands
def key(event):
    if event.keycode == 8320768:
        goForward()
    if event.keycode == 8255233:
        goBackward()
    if event.keycode == 8189699:
        turnRight()
    if event.keycode == 8124162:
        turnLeft()
    if event.keycode == 2031727:
        goUp()
    if event.keycode == 2424940:
        goDown()
    if event.keycode == 458872:
        stop()
        
window.bind("<Key>", key)   #bind keyboard to gui
    
show_frame()  #Camera 1
show_frame2()   #Camera 2

#Update data on table
def updateTable():
    
#     ser = serial.Serial('/dev/ttyACM0', 2000000, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False)
#     sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

#     ser1 = serial.Serial('/dev/ttyACM1', 2000000, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False)
#     sio1 = io.TextIOWrapper(io.BufferedRWPair(ser1, ser1))
#     
#     newValue = sio.readline()
#     newValue1 = sio1.newline()
#     print(newValue)
    
    x = tree.get_children()
    item1_value = tree.item(x[0], "values")
    item2_value = tree.item(x[1], "values")
    tree.item(x[0], text="Compas", values=(int(item1_value[0]) + 1), tags=('rowOne'))
    tree.item(x[1], text="Pressure", values=(int(item2_value[0]) + 1), tags=('rowTwo'))
    print("update")
    window.after(2000, updateTable)

window.after(2000, updateTable)

window.mainloop()  #Starts GUI


