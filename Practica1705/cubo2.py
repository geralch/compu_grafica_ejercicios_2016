# Geraldine Caicedo Hidalgo - 1527691
# Computacion Grafica
# Practica en Clase - 17/05/2016
# Cubo 2

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import os
import threading
import random

caraA = [ 0.5,0.8,0.5, 
				0.8,0.8,0.5, 
				0.8,0.8,0.8, 
				0.5,0.8,0.8]
caraB = [ 0.5,0.5,0.5, 
				0.8,0.5,0.5, 
				0.8,0.5,0.8,
				0.5,0.5,0.8]
caraC = [ 0.5,0.5,0.8, 
				0.8,0.5,0.8, 
				0.8,0.8,0.8, 
				0.5,0.8,0.8]
caraD = [ 0.5,0.5,0.5,
				0.8,0.5,0.5,
				0.8,0.8,0.5,
				0.5,0.8,0.5]
caraE = [0.5,0.5,0.5,
				0.5,0.5,0.8,
				0.5,0.8,0.8,
				0.5,0.8,0.5]
caraF = [0.8,0.5,0.5,
				0.8,0.5,0.8,
				0.8,0.8,0.8,
				0.8,0.8,0.5]

window = 0

DIRECTION = 1

def InitGL(Width, Height):

    glClearColor(0,0,0,0)		#Color del Fondo
    #glClearDepth(1.0)
    #glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    #glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def mostrarEscena():
    global X,Y,Z
    global  xs, ys, zs
    global colorR, colorG, colorB
    global DIRECTION
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Cubo
    glLoadIdentity()
    glTranslatef(0,0,-3)

	# Arriba
    glBegin(GL_QUADS)
    glColor3f(1,0,0) # Rojo
    glVertex3f(caraA[0], caraA[1],  caraA[2])
    glVertex3f(caraA[3], caraA[4],  caraA[5])
    glVertex3f(caraA[6], caraA[7],  caraA[8])
    glVertex3f(caraA[9], caraA[10], caraA[11])
    
    glEnd()

	# Abajo
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0) # Amarillo
    glVertex3f(caraB[0], caraB[1],  caraB[2])
    glVertex3f(caraB[3], caraB[4],  caraB[5])
    glVertex3f(caraB[6], caraB[7],  caraB[8])
    glVertex3f(caraB[9], caraB[10], caraB[11])
    
    glEnd()

	# Frente
    glBegin(GL_QUADS)
    glColor3f(0, 0, 1) # Azul
    glVertex3f(caraC[0], caraC[1],  caraC[2])
    glVertex3f(caraC[3], caraC[4],  caraC[5])
    glVertex3f(caraC[6], caraC[7],  caraC[8])
    glVertex3f(caraC[9], caraC[10], caraC[11])
    
    glEnd()

	# Atras
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1) # Blanco
    glVertex3f(caraD[0], caraD[1],  caraD[2])
    glVertex3f(caraD[3], caraD[4],  caraD[5])
    glVertex3f(caraD[6], caraD[7],  caraD[8])
    glVertex3f(caraD[9], caraD[10], caraD[11])
    
    glEnd()
    
	#  Izquierda
    glBegin(GL_QUADS)
    glColor3f(0,0.5, 0) #Verde
    glVertex3f(caraE[0], caraE[1],  caraE[2])
    glVertex3f(caraE[3], caraE[4],  caraE[5])
    glVertex3f(caraE[6], caraE[7],  caraE[8])
    glVertex3f(caraE[9], caraE[10], caraE[11])
   
    glEnd()

	# Derecha
    glBegin(GL_QUADS)
    glColor3f(1, 0.4, 0) # Naraja
    glVertex3f(caraF[0], caraF[1],  caraF[2])
    glVertex3f(caraF[3], caraF[4],  caraF[5])
    glVertex3f(caraF[6], caraF[7],  caraF[8])
    glVertex3f(caraF[9], caraF[10], caraF[11])
    
    glEnd()

    glutSwapBuffers()
    
def click(button,state,x,y):
	global r, g, b
	global X,Y,Z
	if (button==GLUT_LEFT_BUTTON and state==GLUT_UP):
		X = X + 0.30
		Y = Y - 0.30
		
def main():

		global window

		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
		glutInitWindowSize(600,600)
		glutInitWindowPosition(200,200)

		window = glutCreateWindow('Cubo y Esfera')

		glutDisplayFunc(mostrarEscena)
		glutIdleFunc(mostrarEscena)
		#glutMouseFunc(click)

		InitGL(500,500)
		glutMainLoop()

if __name__ == "__main__":
        main()
