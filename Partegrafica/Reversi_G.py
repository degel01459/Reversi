
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
from Funcion0_Nombres			import Nombres
from Funcion2_Turno		 		import Turno
from Funcion1_SePuedeJugar		import SePuedeJugar 
from Funcion5_Casillas			import LlenaCasilla
from Funcion6_Resultado			import Resultado
from Funcion7_Total				import Total
from Funcion4_Juega				import RealizarJugada
from Funcion3_EsValida			import JugadaValida
from Funcion3_EsValida			import ListaJugadasValidas

#INICIALIZADORES

#COLORES
BLANCO = (255, 255, 255)
VERDE = ( 80, 180, 80)
GRIS = (50, 50, 50)
FONDO = (80,180,80)
NEGRO = (0, 0, 0)

#CASILLAS
LARGO  = 50
ALTO = 50
MARGEN = 10

#CLASE
class Jugador():
	nombre=""
	j=0
	casilla=0
jugador1=Jugador()
jugador2=Jugador()

jugador1.j=1
jugador2.j=2
Nombres(jugador1,jugador2)
print("Comienza jugador 1: ",jugador1.nombre)

def Partida():
	pygame.init()
	# Establecemos el título de la pantalla.
	pygame.display.set_caption("OTHELLO")
	#CONFIGURACION
	DIMENCIONES = [490,600]
	ventana = pygame.display.set_mode(DIMENCIONES)
	clock = pygame.time.Clock()
	fuente =  pygame.font.Font(None,30)
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
	for i in range(0,8):
		print(tablero[i])
	ficha=60
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif ficha > 0 and SePuedeJugar(jugador1,jugador2):
				if event.type == pygame.MOUSEBUTTONDOWN:
					jugador=Turno(turno,jugador1,jugador2)
					print("Es tuno de jugador: ",jugador.j," ",jugador.nombre)
					if ListaJugadasValidas(tablero,jugador)==True:
						pos= (event.pos)
						y=pos[0] // (LARGO + MARGEN)
						x=pos[1] // (ALTO + MARGEN)
						print("Click ", pos, "Coordenadas de la retícula: ", x, y)
						if JugadaValida(tablero,x,y,jugador):
							RealizarJugada(tablero,x,y,jugador)
							for i in range(0,8):
								print(tablero[i])
							ficha=ficha-1
							turno=turno+1
							jugador1.casilla=LlenaCasilla(tablero,jugador1)
							jugador2.casilla=LlenaCasilla(tablero,jugador2)
						else:
							pass
					else:
						turno=turno+1
					Resultado(jugador1,jugador2)
					Total(jugador1,jugador2,ficha)
			elif ficha == 0 or SePuedeJugar(jugador1,jugador2):
				print("¿Jugar nuevamente?")
				print("Indique (SI) o (NO) en mayúscula")
				while True:
					try:
						otra=input("ingrese: ")
						assert(otra=="SI" or otra=="NO")
					except:
						print("Debe ingresar SI no NO en mayúscula")	
				if otra=="SI":
					Partida()
				else:
					sys.exit()
		# Establecemos el fondo de pantalla.
		ventana.fill(GRIS)	
		# Dibujamos la retícula
		for x in range(0,8):
			for y in range(0,8):
				color=FONDO
				colorf=FONDO
				if tablero[x][y] == 1:
					colorf = NEGRO
				if tablero[x][y] == 2:# Establecemos el título de la pantalla.
					colorf = BLANCO
				inf0 = fuente.render("Es tuno de jugador: ", 0, (255,255,255))
				ventana.blit( inf0, (500 , 200) )
				pygame.draw.rect(ventana,color,[(MARGEN+LARGO) * y + MARGEN, (MARGEN+ALTO) * x + MARGEN, LARGO, ALTO])
				pygame.draw.circle(ventana,colorf,[(MARGEN+LARGO) * y + MARGEN+25, (MARGEN+ALTO) * x + MARGEN+25],LARGO//2)
		# Limitamos a 60 fotogramas por segundo.
		clock.tick(60)
		# Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
		pygame.display.flip()
	pygame.quit()
Partida()
