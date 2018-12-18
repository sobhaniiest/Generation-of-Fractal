#Sobhan Mondal

import OpenGL 
OpenGL.ERROR_ON_COPY = True 

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

width = 700
height = 500
maxR = 1
minR = -2.5
rangeR = maxR - minR
maxI = 1
minI = -1
rangeI = maxI - minI

def init2D(rc,gc,bc):
    glClearColor(rc,gc,bc,0.0)    
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D (0.0, 700.0, 0.0, 500.0)

def color(it,px,py):
    
    r = 0 
    g = 0
    b = 0
    if(it < 16):
        g = 16 * (16 - it)
        b = 0
        r = 16 * it -1
    elif(it < 16):
        g = 16 * (16 - it)
        b = 0
        r = 16 * it - 1
    elif(it > 16 and it < 32):
        g = 0
        b = 16 * (it - 16) 
        r = 16 * (32 - it) - 1
    elif(it > 32 and it < 64):
        g = 8 * (it - 32)
        b = 8 * (64 - it) - 1
        r = 0
    elif(it > 64 and it < 127):
        g = 255 - (it - 64) * 4
        b = 0
        r = 0

    rp = float(r)/255
    gp = float(g)/255
    bp = float(b)/255
    glColor3f(rp, gp, bp)
    glBegin(GL_POINTS)
    glVertex2i(px,py)
    glEnd()
    glFlush()
    

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    for py in range(0,height):
        for px in range(0,width):
            x0 = float(px) * (float(rangeR)/float(width)) + float(minR)
            y0 = float(py) * (float(rangeI)/float(height)) + float(minI)
            #print x0,y0
            x = 0.0
            y = 0.0

            iteration = 0
            max_iteration = 127

            while(x*x + y*y < 4.0 and iteration < max_iteration):
                
                xtemp = x*x - y*y + x0
                ytemp =  2*x*y + y0
                
                '''
                xtemp = x*(x*x - 3*y*y) + x0
                ytemp = y*(3*x*x-y*y) + y0
                '''
                if(x == xtemp and y == ytemp):
                    iteration = max_iteration
                    break
                x = xtemp
                y = ytemp
                iteration = iteration + 1

            color(iteration,px,py)

            
    
glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (700, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ('Mandelbrot Set')
init2D(1.0,1.0,1.0)
glutDisplayFunc(display)
glutMainLoop()

