#ROJO - VERDE - AZUL (255,255,255)
import pygame
import sys																						
import os 	
import random 
from pygame.locals import *

pygame.init()							#INICIALIZACION DE LIBRERIA

#CLASES
class jugador():
	nombre=""
	j=0
	lineas=0
jugador1 = jugador()	#invoca la clase
jugador2 = jugador()	#invoca la clase
jugador1.j=1			#El valor del jugador1
jugador2.j=2			#El valor del jugador2
jugador1.lineas=0		#Cantidad de lineas del jugador1
jugador2.lineas=0		#Cantidad de lineas del jugador2

#	INICIALIZACION
width=1024								#ANCHO
height=768								#ALTO
x=0
y=0																							
partida = 1				#Numero de Partidas 
#	CREACION DE VENTANA
ventana = pygame.display.set_mode((width,height))				#CREACION DE VENTANA
pygame.display.set_caption("LA VIEJA EN N DIMENCIONES")			#NOMBRE DE VENTANA
color = (0,0,0)													#COLOR
fondo = pygame.Surface((width,height))							#COLOR DE VENTANA

#	RELOJ

reloj = pygame.time.Clock()

#	TEXTOS

fuente =  pygame.font.Font(None,30)																	#Creacion de Fuente(archivo fuente, tama;o letra)

titulo = fuente.render("LA VIEJA EN N DIMENSIONES", 0, (255,255,255))								#parametros(text, antialias, coordenada, color de fondo)
jugar = fuente.render("¿QUIERES JUGAR?", 0, (255,255,255))											#parametros(text, antialias, coordenada, color de fondo)
si = fuente.render("Espacio = COMENZAR", 0, (255,255,255))													#parametros(text, antialias, coordenada, color de fondo)
no = fuente.render("Esc = EXIT", 0, (255,255,255))														#parametros(text, antialias, coordenada, color de fondo)
exit = fuente.render("JUEGA CUANDO QUIERAS", 0, (255,255,255))														#parametros(text, antialias, coordenada, color de fondo)
numerodepartida = fuente.render("Esta es la partida: ", True, (255,255,255))
#imagen = pygame.image.load("D:/DEGEL/OneDrive/UNI_KEVIN/ALGORITMOI/LabAlgoritmo/Proyecto/3R.jpg")	#Load de imagen(archivo fuente, tama;o letra)

#	INTERFAZ

ventana.fill(color)
ventana.blit( titulo, (375, 100) )																#creacion en ventana (coordenadas x,y)
#ventana.blit( imagen, (400, 150) )																#creacion en ventana (coordenadas x,y)
ventana.blit( jugar, (430 , 450) )																#creacion en ventana (coordenadas x,y)
ventana.blit( si, (290,500) )																	#creacion en ventana (coordenadas x,y)
ventana.blit( no, (600,500) )

# crea un reloj
clock = pygame.time.Clock()
Play = True
# BUCLE DE VENTANA

while Play:
	clock.tick(5)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Play = False
		# si alguna tecla es presionada
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			ventana.fill(color)
			fuentejugadores =  pygame.font.Font(None,30)
				
			variables = ["","",""]

			iniciar = False

			while iniciar == False:
				ventana.fill(color)
				ventana.blit( numerodepartida, (375, 100) )
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key != 13:
							print(event.key)
							if key >= 97 and key <= 122:
								caracter = teclado(key)
								jugador1 = jugador1 + caracter
								jugador2 = jugador2 + caracter
							elif key == 32:
								jugador1 = jugador1 + " "
								jugador2 = jugador2 + " "
							elif key >= K_0 and key <= K_9:
								caracter = teclado(key)
								jugador1 = jugador1 + caracter
								jugador2 = jugador2 + caracter
								N = N + caracter
							elif key == 8:
								longitud1 = len(jugador1)
								longitud2 = len(jugador2)
								longitud3 = len(N)
								aux1 = jugador1
								aux2 = jugador2
								aux3 = N
								jugador1 = aux[0:longitud1-1]
								jugador2 = aux[0:longitud2-1]
								N = N[0:longitud3-1]
							print(variables)
							if 0 < N <= 9:
								iniciar = True
							else:
								pass
						elif event.type == QUIT:
							pygame.quit()
							sys.exit()
				jugador1 = fuentejugadores.render("NOMBRE DEL JUGADOR 1: ", True, (255,255,255))
				longitud1 = ventana.blit(jugador1, (0, 200))
				if len(longitud1) > 0:
					j1 = fuentejugadores.render(jugador1, True, (0, 0, 0))
					ventana.blit(j1, (longitud.width + 10, 200))
				jugador2 = fuentejugadores.render("NOMBRE DEL JUGADOR 2: ", True, (255,255,255))
				longitud2 = ventana.blit(jugador, (0, 200))
				if len(longitud2) > 0:
					j2 = fuentejugadores.render(jugador2, True, (0, 0, 0))
					ventana.blit(j2, (longitud.width + 10, 200))
				reloj.tick(40)
				pygame.display.update()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			ventana.fill(color)
			ventana.blit( exit, (175,200) )
			clock.tick(3)
			Play = False
							
	pygame.display.update()																			#ACTUALIZACION DE VENTANA

def teclado(key):
    if key == 97:
        caracter = "A"
    elif key == 98:
        caracter = "B"
    elif key == 99:
        caracter = "C"
    elif key == 100:
        caracter = "D"
    elif key == 101:
        caracter = "E"
    elif key == 102:
        caracter = "F"
    elif key == 103:
        caracter = "G"
    elif key == 104:
        caracter = "H"
    elif key == 105:
        caracter = "I"
    elif key == 106:
        caracter = "J"
    elif key == 107:
        caracter = "K"
    elif key == 108:
        caracter = "L"
    elif key == 109:
        caracter = "M"
    elif key == 110:
        caracter = "N"
    elif key == 111:
        caracter = "O"
    elif key == 112:
        caracter = "P"
    elif key == 113:
        caracter = "Q"
    elif key == 114:
        caracter = "R"
    elif key == 115:
        caracter = "S"
    elif key == 116:
        caracter = "T"
    elif key == 117:
        caracter = "U"
    elif key == 118:
        caracter = "V"
    elif key == 119:
        caracter = "W"
    elif key == 120:
        caracter = "X"
    elif key == 121:
        caracter = "Y"
    elif key == 122:
        caracter = "Z"
    elif key == 48:
        caracter = "0"
    elif key == 49:
        caracter = "1"
    elif key == 50:
        caracter = "2"
    elif key == 51:
        caracter = "3"
    elif key == 52:
        caracter = "4"
    elif key == 53:
        caracter = "5"
    elif key == 54:
        caracter = "6"
    elif key == 55:
        caracter = "7"
    elif key == 56:
        caracter = "8"
    elif key == 57:
        caracter = "9"

    return caracter