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

#LIBRERIAS
import random
import sys
import pygame
import os

#FUNCIONES
from Funcion3_Nombres			import Nombres
from Funcion4_QuedanFichas 		import QuedanFichas
from Funcion5_Turno		 		import Turno
from Funcion7_SePuedeJugar		import SePuedeJugar 
from Funcion8_Casillas			import LlenaCasilla
from Funcion9_Resultado			import Resultado
from Funcion10_CambiarJugador 	import CambiarJugador
from Funcion11_Total			import Total
from Funcion12_Juega			import RealizarJugada
from Funcion13_EsValida			import JugadaValida

#INICIALIZADORES

#COLORES
BLANCO = (255, 255, 255)
VERDE = ( 80, 180, 80)
ROJO = (255, 0, 0)
FONDO = (80,180,80)
NEGRO = (0, 0, 0)

#CASILLAS
LARGO  = 50
ALTO = 50
MARGEN = 10

#CONFIGURACION
DIMENCIONES = [500,500]
# Establecemos el título de la pantalla.
pygame.display.set_caption("OTHELLO")

#CLASE
class Jugador():
	nombre=""
	j=0
	casilla=0
jugador1=Jugador()
jugador2=Jugador()
partida=1
Nombres(jugador1,jugador2,partida)
jugador1.j=1
jugador2.j=2
u=0
def Partida():
	jugador1.casilla=2
	jugador2.casilla=2
	x=0
	y=0
	turno=1
	#TABLERO
	tablero=[[ 0 for j in range(0,8)]for i in range(0,8)]
	tablero[3][3]=1
	tablero[3][4]=2
	tablero[4][3]=2
	tablero[4][4]=1
	"""for i in range(0,8):
		print(tablero[i])"""
	ficha=60
	pygame.init()
	ventana = pygame.display.set_mode(DIMENCIONES)
	cerrar=False
	clock = pygame.time.Clock()
	fuente = pygame.font.Font(None,30)
	pygame.display.set_caption('Eventos del mouse')
	pygame.display.set_mode((500, 500))
	while True:
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			break
		if event.type == pygame.MOUSEBUTTONDOWN:
			if ficha > 0 and SePuedeJugar(jugador1,jugador2):
				jugador=Turno(turno,jugador1,jugador2)
				pos= (event.pos)
				y=pos[0] // (LARGO + MARGEN)
				x=pos[1] // (ALTO + MARGEN)
				print(tablero[x][y])
				print("Click ", pos, "Coordenadas de la retícula: ", x, y)
				if JugadaValida(tablero,x,y,jugador):
					RealizarJugada(tablero,x,y,jugador,jugador1,jugador2)
					ficha=ficha-1
					turno=turno+1
					CambiarJugador(turno,jugador1,jugador2)
					jugador1.casilla=LlenaCasilla(tablero,jugador1)
					jugador2.casilla=LlenaCasilla(tablero,jugador2)
				else:
					pass
				Total(jugador1,jugador2)		
				Resultado(jugador1,jugador2)
		# Establecemos el fondo de pantalla.
		ventana.fill(VERDE)	
		# Dibujamos la retícula
		for x in range(0,8):
			for y in range(0,8):
				color=FONDO
				if tablero[x][y] == 1:
					color = NEGRO
				if tablero[x][y] == 2:
					color = BLANCO
				pygame.draw.rect(ventana,color,[(MARGEN+LARGO) * y + MARGEN, (MARGEN+ALTO) * x + MARGEN, LARGO, ALTO])
		# Limitamos a 60 fotogramas por segundo.
		clock.tick(60)
		# Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
		pygame.display.flip()
pygame.quit()

print(Partida())



