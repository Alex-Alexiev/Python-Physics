import time
from tkinter import *

animation = Tk()
cWidth = 800
cHeight = 600
canvas = Canvas(animation, width = cWidth, height = cHeight)
canvas.pack()

def main():
    o = makeCircle(10,100,10,"red")
    vx = 0
    vy = 0
    ay = 1
    while True:
        vy+=ay
        if getX(o) > cWidth or getX(o) < 0:
            vx *= -1
        if getY(o) > cHeight:
            vy *= -1
        canvas.move(o,vx,vy)
        animation.update()
        time.sleep(0.05)

def makeCircle(cx, cy, r, colour):
    return canvas.create_oval(cx-r,cy-r,cx+r,cy+r, fill=colour, outline=colour)

def getX(o):
    return canvas.coords(o)[2]

def getY(o):
    return canvas.coords(o)[3]

main()