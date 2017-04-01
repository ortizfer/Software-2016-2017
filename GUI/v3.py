
#importing modules required
from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
import serial

global logMessage

def sendMessage(message):
    global logMessage
    logMessage = message

def getMessage():
    return logMessage

logMessage = "Proti Status"

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

tree.insert("", 0, text="Compass", values=(0), tags=('rowOne'))
tree.insert("", 1, text="Pressure", values=(0), tags=('rowTwo'))

tree.tag_configure('rowOne', background='cyan')
tree.tag_configure('rowTwo', background='yellow')

tree.pack(side = LEFT, padx=20)

#Buttons
upDownFrame = Frame(rightFrame)
# proti_status = Text(upDownFrame, width=50, height=5)
# proti_status.insert(INSERT, "Proti on...\n")

S = Scrollbar(upDownFrame)
T = Text(upDownFrame, height=4, width=50, relief=RAISED)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.insert(END, logMessage)

# proti_status.pack(side = RIGHT)
upDownFrame.pack( side = RIGHT, padx=30, pady=20)

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
    
show_frame()  #Camera 1
show_frame2()   #Camera 2

ser = serial.Serial('/dev/cu.usbmodem1A12323', 9600, timeout=0, xonxoff=False, rtscts=False, dsrdtr=False)
ser.flushInput()
ser.flushOutput()

ser1 = serial.Serial('/dev/cu.usbmodem1A12423', 9600, timeout=0, xonxoff=False, rtscts=False, dsrdtr=False)
ser1.flushInput()
ser1.flushOutput()

#Update data on table
def updateTable():
    
    newValue = ser.readline()
    newValue1 = ser1.readline()
    
    x = tree.get_children()

    tree.item(x[0], text="Compass", values=(newValue), tags=('rowOne'))
    tree.item(x[1], text="Pressure", values=(newValue1), tags=('rowTwo'))
    
#     newMessage = "New Status..."
#     sendMessage(newMessage)
    
    window.after(1000, updateTable)

def updataStatus():
    
    message = getMessage()
    print(message)
    global logMessage
    
    if (getMessage() != ""):
        T.insert(END, "\n" + logMessage)
        T.see(END)
        sendMessage("")
    
    window.after(1000, updataStatus)

window.after(1000, updateTable)
window.after(1000, updataStatus)

window.mainloop()  #Starts GUI


