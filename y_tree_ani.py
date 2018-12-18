#Sobhan Mondal

from graphics import *
from random import randint
import math

ang = 0
angle = -90
depth = 8
x1 = 500
y1 = 500

# 2 - 2 branch
# 3 - 3 branch
# 4 - 4 branch
# 5 - 3-2 random
# 6 - 4-3 random
# a - change angle

win = GraphWin("My Window", 1000, 800,autoflush=False)
win.setBackground(color_rgb(0, 0, 0))

def drawTree2(x1, y1, angle, depth, ang):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        line = Line(Point(x1,y1), Point(x2,y2))
        line.setOutline(color_rgb(4, 140, 1))
        line.draw(win)
        drawTree2(x2, y2, angle - ang, depth - 1, ang)
        drawTree2(x2, y2, angle + ang, depth - 1, ang)
        
def drawTree3(x1, y1, angle, depth, ang):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        line = Line(Point(x1,y1), Point(x2,y2))
        line.setOutline(color_rgb(4, 140, 1))
        line.draw(win)
        drawTree3(x2, y2, angle, depth - 1, ang)
        drawTree3(x2, y2, angle - ang, depth - 1, ang)
        drawTree3(x2, y2, angle + ang, depth - 1, ang)
        
def drawTree4(x1, y1, angle, depth, ang):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        line = Line(Point(x1,y1), Point(x2,y2))
        line.setOutline(color_rgb(4, 140, 1))
        line.draw(win)
        drawTree4(x2, y2, angle - 2*ang, depth - 1, ang)
        drawTree4(x2, y2, angle + 2*ang, depth - 1, ang)
        drawTree4(x2, y2, angle - ang, depth - 1, ang)
        drawTree4(x2, y2, angle + ang, depth - 1, ang)

def drawTree3r(x1, y1, angle, depth, ang):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        line = Line(Point(x1,y1), Point(x2,y2))
        line.setOutline(color_rgb(4, 140, 1))
        line.draw(win)
        r = randint(0, 2)
        if(r==0):
            drawTree3r(x2, y2, angle - ang, depth - 1, ang)
            drawTree3r(x2, y2, angle + ang, depth - 1, ang)
        if(r==1):
            drawTree3r(x2, y2, angle, depth - 1, ang)
            drawTree3r(x2, y2, angle + ang, depth - 1, ang)
        if(r==2):
            drawTree3r(x2, y2, angle, depth - 1, ang)
            drawTree3r(x2, y2, angle - ang, depth - 1, ang)

def drawTree4r(x1, y1, angle, depth, ang):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        line = Line(Point(x1,y1), Point(x2,y2))
        line.setOutline(color_rgb(4, 140, 1))
        line.draw(win)
        r = randint(0, 3)
        if(r==0):
            drawTree4r(x2, y2, angle - 2*ang, depth - 1, ang)
            drawTree4r(x2, y2, angle + 2*ang, depth - 1, ang)
            drawTree4r(x2, y2, angle + ang, depth - 1, ang)
        if(r==1):
            drawTree4r(x2, y2, angle - 2*ang, depth - 1, ang)
            drawTree4r(x2, y2, angle + 2*ang, depth - 1, ang)
            drawTree4r(x2, y2, angle - ang, depth - 1, ang)
        if(r==2):
            drawTree4r(x2, y2, angle - 2*ang, depth - 1, ang)
            drawTree4r(x2, y2, angle - ang, depth - 1, ang)
            drawTree4r(x2, y2, angle + ang, depth - 1, ang)
        if(r==3):
            drawTree4r(x2, y2, angle + 2*ang, depth - 1, ang)
            drawTree4r(x2, y2, angle - ang, depth - 1, ang)
            drawTree4r(x2, y2, angle + ang, depth - 1, ang)

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

if(True):
    k1 = win.getKey()
    print ("key")
    print (k1)
    if(k1 == "2"):
        while(True):
            k2 = win.getKey()
            clear(win)
            if(k2 == "a"):
                print ("c_angle")
                print (ang)
                drawTree2(x1, y1, angle, depth - 1, ang)
                #drawTree(x2, y2, 90-angle, depth - 1, ang)
                ang = (ang+5)%360
    if(k1 == "3"):
        while(True):
            k2 = win.getKey()
            clear(win)
            if(k2 == "a"):
                print ("c_angle")
                print (ang)
                drawTree3(x1, y1, angle, depth - 1, ang)
                #drawTree(x2, y2, 90-angle, depth - 1, ang)
                ang = (ang+5)%360
    if(k1 == "4"):
        while(True):
            k2 = win.getKey()
            clear(win)
            if(k2 == "a"):
                print ("c_angle")
                print (ang)
                drawTree4(x1, y1, angle, depth - 1, ang)
                #drawTree(x2, y2, 90-angle, depth - 1, ang)
                ang = (ang+5)%360
    if(k1 == "5"):
        while(True):
            k2 = win.getKey()
            clear(win)
            if(k2 == "a"):
                print ("c_angle")
                print (ang)
                drawTree3r(x1, y1, angle, depth - 1, ang)
                #drawTree(x2, y2, 90-angle, depth - 1, ang)
                ang = (ang+5)%360
    if(k1 == "6"):
        while(True):
            k2 = win.getKey()
            clear(win)
            if(k2 == "a"):
                print ("c_angle")
                print (ang)
                drawTree4r(x1, y1, angle, depth - 1, ang)
                #drawTree(x2, y2, 90-angle, depth - 1, ang)
                ang = (ang+5)%360

