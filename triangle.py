#Sobhan Mondal


from graphics import *
from random import randint

win = GraphWin("My Window", 1000, 600)
win.setBackground(color_rgb(0, 0, 0))

x1 = 500
y1 = 50
x2 = 50
y2 = 550
x3 = 950
y3 = 550
x = 500
y = 450

pt1 = Point(x1, y1)
pt2 = Point(x2, y2)
pt3 = Point(x3, y3)

pt = Point(x, y)

pt1.setOutline(color_rgb(4, 140, 1))
pt1.draw(win)
pt2.setOutline(color_rgb(4, 140, 1))
pt2.draw(win)
pt3.setOutline(color_rgb(4, 140, 1))
pt3.draw(win)
pt.setOutline(color_rgb(4, 140, 1))
pt.draw(win)


while(True):
    r = randint(0, 5)
    if(r == 0 or r == 1):
        x = int((x+x1)/2)
        y = int((y+y1)/2)
        npt = Point(x, y)
        npt.setOutline(color_rgb(4, 140, 1))
        npt.draw(win)
    elif(r == 2 or r == 3):
        x = int((x+x2)/2)
        y = int((y+y2)/2)
        npt = Point(x, y)
        npt.setOutline(color_rgb(4, 140, 1))
        npt.draw(win)
    elif(r == 4 or r == 5):
        x = int((x+x3)/2)
        y = int((y+y3)/2)
        npt = Point(x, y)
        npt.setOutline(color_rgb(4, 140, 1))
        npt.draw(win)

'''
while(True):
    x = int((x+x1)/2)
    y = int((y+y1)/2)
    npt = Point(x, y)
    npt.setOutline(color_rgb(4, 140, 1))
    npt.draw(win)

    x = int((x+x2)/2)
    y = int((y+y2)/2)
    npt = Point(x, y)
    npt.setOutline(color_rgb(4, 140, 1))
    npt.draw(win)

    x = int((x+x3)/2)
    y = int((y+y3)/2)
    npt = Point(x, y)
    npt.setOutline(color_rgb(4, 140, 1))
    npt.draw(win)
'''
     
    
win.getMouse()
win.close()







