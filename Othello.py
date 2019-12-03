# Descripción: Reversi es un cásico juego de mesa.
# Autores: Angel Rodriguez, Kevin Briceño
# Fecha de modificación: 29/11/2019
# Variables:
# jugador1
# jugador2
# x: int // cordenada para la fila
# y: int // cordenada para la columna
# tablero: list // Es el tablero de juego
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
from Funcion1_SePuedeJugar		import SePuedeJugar 
from Funcion2_Turno		 		import Turno
from Funcion3_EsValida			import JugadaValida
from Funcion3_EsValida			import ListaJugadasValidas
from Funcion4_Juega				import RealizarJugada
from Funcion5_Casillas			import LlenaCasilla
from Funcion6_Resultado			import Resultado
from Funcion7_Total				import Total

#COLORES
BLANCO = (255, 255, 255)
AZUL = (20,20,100)
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

def Partida():
	pygame.init()
	# Establecemos el título de la pantalla.
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.display.set_caption("OTHELLO")
	#INICIALIZADORES
	DIMENCIONES = [490,700]
	ventana = pygame.display.set_mode(DIMENCIONES)
	clock = pygame.time.Clock()
	jugador1.casilla=2
	jugador2.casilla=2
	x=0
	y=0
	turno=1
	ficha=60
	#TABLERO
	tablero=[[ 0 for j in range(0,8)]for i in range(0,8)]
	tablero[3][3]=1
	tablero[3][4]=2
	tablero[4][3]=2
	tablero[4][4]=1
	for i in range(0,8):
		print(tablero[i])	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif ficha > 0 and SePuedeJugar(jugador1,jugador2):
				if event.type == pygame.MOUSEBUTTONDOWN:
					jugador=Turno(turno,jugador1,jugador2)
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
			elif ficha == 0 or SePuedeJugar(jugador1,jugador2)==False:
				print("¿Jugar nuevamente?")
				print("Indique (SI) o (NO) en mayúscula")
				while True:
					try:
						otra=input("ingrese: ")
						assert(otra=="SI" or otra=="NO")
						break
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
				if tablero[x][y] == 2:
					colorf = BLANCO
				pygame.draw.rect(ventana,color,[(MARGEN+LARGO) * y + MARGEN, (MARGEN+ALTO) * x + MARGEN, LARGO, ALTO])
				pygame.draw.circle(ventana,colorf,[(MARGEN+LARGO) * y + MARGEN+25, (MARGEN+ALTO) * x + MARGEN+25],LARGO//2)
		fn=jugador1.casilla
		fb=jugador2.casilla
		fn1=jugador1.nombre
		fb1=jugador2.nombre
		ft=turno
		jugador=Turno(turno,jugador1,jugador2)
		fja=jugador.nombre
		fw=Total(jugador1,jugador2,ficha)
		fuente0 = pygame.font.SysFont('arialblack',40)
		fuente1 = pygame.font.SysFont('arialblack',25)
		text0 = fuente0.render(str(fn), True, NEGRO)
		text1 = fuente0.render(str(fb), True, BLANCO)
		text2 = fuente1.render(str(fn1), True, NEGRO)
		text3 = fuente1.render(str(fb1), True, BLANCO)
		text4 = fuente1.render("FICHAS: "+str(ficha), True, AZUL)
		text5 = fuente1.render("Juega: "+str(fja), True, AZUL)
		text6 = fuente1.render("GANO JUGADOR: "+str(fw), True, AZUL)
		ventana.blit(text0,(40,540))
		ventana.blit(text1,(260,540))
		ventana.blit(text2,(40,490))
		ventana.blit(text3,(260,490))
		ventana.blit(text4,(170,590))
		ventana.blit(text5,(150,620))
		ventana.blit(text6,(100,660))
		# Limitamos a 60 fotogramas por segundo.
		clock.tick(60)
		# Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
		pygame.display.flip()
	sys.exit()
Partida()