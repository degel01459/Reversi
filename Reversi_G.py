# Descripción: Reversi es un cásico juego de mesa.
# Autores: Angel Rodriguez, Kevin Briceño
# Fecha de modificación: 29/11/2019
# Variables:
# jugador1
# jugador2
# i: int // cordenada para la fila
# j: int // cordenada para la columna
# reversi: list // Es el tablero de juego
# 0 // Casillas vacias
# 1 // Ficha Negra
# 2 // Ficha Blanca
import random
import sys
import pygame
import os

from Funcion0_Posicion			import inicio
from Funcion1_Imprimir			import imprimir
from Funcion2_QuieresJugar		import QuieresJugar
from Funcion3_Nombres			import Nombres
from Funcion4_QuedanFichas 		import QuedanFichas
from Funcion5_Turno		 		import Turno
from Funcion6_ObtenerJugada		import ObtenerJugada
from Funcion7_SePuedeJugar		import SePuedeJugar 
from Funcion8_Casillas			import LlenaCasilla
from Funcion9_Resultado			import Resultado
from Funcion10_CambiarJugador 	import CambiarJugador
from Funcion11_Total			import Total
from Funcion12_Juega			import RealizarJugada
from Funcion13_EsValida			import JugadaValida

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0,0,255)
FICHABLANCA = pygame.image.load("C:/Users/ANGRODHER/Desktop/Algoritmos/Reversi/circuloblanco.png")
FICHANEGRA = pygame.image.load("C:/Users/ANGRODHER/Desktop/Algoritmos/Reversi/circulonegro.png")
titulo = pygame.image.load("C:/Users/ANGRODHER/Desktop/Algoritmos/Reversi/titulo.jpg")

# Establecemos el LARGO, ALTO y MARGEN de cada celda de la retícula.
LARGO  = 50
ALTO = 50
MARGEN = 10

# Inicializamos pygame
pygame.init()

DIMENSION_VENTANA = [490, 490]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
os.environ['SDL_VIDEO_CENTERED'] = '1'	#Para centrar la ventana a la hora de abrirse 

# Establecemos el título de la pantalla.
pygame.display.set_caption("REVERSI")

# Iteramos hasta que el usuario pulse el botón de salir.
cerrar = False

# Lo usamos para establecer cuán rápido de refresca la pantalla.
reloj = pygame.time.Clock()


class Jugador():
		nombre=""
		j=0
		casilla=0

jugador1=Jugador()
jugador2=Jugador()
partida=1
#Nombres(jugador1,jugador2,partida)
jugador1.j=1
jugador2.j=2



"""def Partida():
	jugador1.casilla=2
	jugador2.casilla=2
	x=0
	y=0
	turno=1
	reversi=[[0 for j in range(0,8)]for i in range(0,8)]
	ficha=60
	print(" 1 =",jugador1.nombre,"2 =", jugador2.nombre)
	inicio(reversi)	
	imprimir(reversi)
	while QuedanFichas(ficha) and SePuedeJugar(jugador1,jugador2):
		jugador=Turno(turno,jugador1,jugador2)
		
		x,y=ObtenerJugada(x,y)
		
		if JugadaValida(reversi,x,y,jugador):
			RealizarJugada(reversi,x,y,jugador,jugador1,jugador2)
			ficha=ficha-1
			imprimir(reversi)
			turno=turno+1
			CambiarJugador(turno,jugador1,jugador2)
			jugador1.casilla=LlenaCasilla(reversi,jugador1)
			jugador2.casilla=LlenaCasilla(reversi,jugador2)		
			print("")
			print("jugador1:",jugador1.casilla,"jugador2:",jugador2.casilla)		
		else:
			print("error, la posicion no es válida")
			print("")
	Total(jugador1,jugador2)		
	Resultado(jugador1,jugador2)

Partida()


Nueva_partida=True
while Nueva_partida:
	while True:
			try:
				print("¿Jugar nuevamente?")
				print("Indique (SI) o (NO) en mayúscula")
				otra=input("ingrese: ")
				assert(otra=="SI" or otra=="NO")
				break
			except:
				print("El dato ingresado no es válido")
				print("Debe ingresar (SI) o (NO) en mayúscula")
				print("")
	if otra=="NO":
		Nueva_partida=False
		print("Fin del juego")
	elif otra=="SI":
		Partida()"""			
reversi=[[0 for j in range(0,8)]for i in range(0,8)]
inicio(reversi)	
imprimir(reversi)

while not cerrar:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			cerrar=True
		elif evento.type == pygame.MOUSEBUTTONDOWN:
			
			pos=pygame.mouse.get_pos()
			y=pos[0] // (LARGO + MARGEN)
			x=pos[1] // (ALTO + MARGEN)
			x,y=ObtenerJugada(x,y)
			print("Click ", pos, "Coordenadas de la retícula: ", x, y)
	# Establecemos el fondo de pantalla.
	pantalla.fill(NEGRO)

	for x in range(0,8):
		for y in range(0,8):
			color=BLANCO
			if reversi[x][y]==0:
				color=VERDE
			pygame.draw.rect(pantalla,color,[(MARGEN+LARGO) * y + MARGEN,(MARGEN+ALTO) * x + MARGEN,LARGO,ALTO])
	reloj.tick(60)
	pygame.display.flip()
pygame.quit()