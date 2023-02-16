from turtle import *
from HanoiDisk import Disk
class Pole(object):
    def __init__(self, name="",xpos=0,ypos=0,thick=10,length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0 
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        setheading(0)
        penup()
        goto(self.pxpos, self.pypos)
        pendown()
    
        forward(self.pthick/2)
        left(90)
        forward(self.plength)
        left(90)
        forward(self.pthick)
        left(90)
        forward(self.plength)
        left(90)
        forward(self.pthick/2)

        setheading(0)

    def pushdisk(self, Disk: Disk):
        self.stack.append(Disk)
        Disk.cleardisk()

        Disk.newpos(self.pxpos, self.pypos - Disk.dheight * self.toppos)
        Disk.showdisk()

    def popdisk(self):
        return self.stack.pop()
        

w = Pole("x",0,0).showpole()
done()
        