
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
import random # usamos random para la elección quien comienza de los jugadores
import sys # importamos sys para
import pygame # importamos pygame para la creacion grafíca de los componentes logicos
import os

#FUNCIONES
from Funcion3_Nombres			import Nombres
from Funcion5_Turno		 		import Turno
from Funcion7_SePuedeJugar		import SePuedeJugar 
from Funcion8_Casillas			import LlenaCasilla
from Funcion9_Resultado			import Resultado
from Funcion10_CambiarJugador 	import CambiarJugador
from Funcion11_Total			import Total
from Funcion12_Juega			import RealizarJugada
from Funcion13_EsValida			import JugadaValida
from Funcion13_EsValida			import ListaJugadasValidas

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

#La clase permitira hacer uso practico de la variables, ademas de almacenar informacion que es usada en determinado momento 
#CLASE:
class Jugador():
	nombre=""
	j=0
	casilla=0
# Inicializamos alguna de la variables a usar en el prgrama	
jugador1=Jugador()
jugador2=Jugador()
partida=1
Nombres(jugador1,jugador2,partida)
jugador1.j=1
jugador2.j=2

#CONFIGURACION
DIMENCIONES = [490,600]
ventana = pygame.display.set_mode(DIMENCIONES)
clock = pygame.time.Clock()

pygame.init()
# Establecemos el título de la pantalla.
pygame.display.set_caption("OTHELLO")

# Función partida contiene al programa principal
def Partida():
	jugador1.casilla=2
	jugador2.casilla=2
	x=0
	y=0
	turno=1
	#TABLERO e inicialización de las primeras posiciones del juego
	tablero=[[ 0 for j in range(0,8)]for i in range(0,8)]
	tablero[3][3]=1
	tablero[3][4]=2
	tablero[4][3]=2
	tablero[4][4]=1
	# imprimimo un tablero en la ventana comandos CMD
	for i in range(0,8):
		print(tablero[i])
	# Cantidad de disponibles a jugar dado que el tablero por default inicia con 4 fichas	
	ficha=60
	while True:
		event = pygame.event.wait()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		# mientras queden fichas y los jugadores tengan almenos 1 ficha en el tablero, hay jugada!	
		elif ficha > 0 and SePuedeJugar(jugador1,jugador2):
			if event.type == pygame.MOUSEBUTTONDOWN:
				jugador=Turno(turno,jugador1,jugador2)
				print("ES tuno de",jugador.j)
				# La funcion ListaJugadaValida verfica todo el tablero y determina si
				# el jugador en turno puede hacer almenos 1 jugada
				if ListaJugadasValidas(tablero,jugador)==True:
					pos= (event.pos)
					y=pos[0] // (LARGO + MARGEN)
					x=pos[1] // (ALTO + MARGEN)
					print("Click ", pos, "Coordenadas de la retícula: ", x, y)
					# La función JugadaValida determina si la coordenada dada
					# es correcta para realizar una jugada
					if JugadaValida(tablero,x,y,jugador):
						# Realiza la jugada en la coordenada verificada
						RealizarJugada(tablero,x,y,jugador)
						# impresión de tablero despues de la jugada hecha 
						for i in range(0,8):
							print(tablero[i])
						# restamos una ficha, cambiamos de turnos y, por ende, de jugador	
						ficha=ficha-1
						turno=turno+1
						CambiarJugador(turno,jugador1,jugador2)
						# calcula cuantas casillas posee cada jugador
						jugador1.casilla=LlenaCasilla(tablero,jugador1)
						jugador2.casilla=LlenaCasilla(tablero,jugador2)
					# en caso de que la jugada no sea válida, da error o pasa
					else:
						pass
				# en caso de que el jugador en turno no pueda hacer una jugada, entonces cambia
				# turno y jugador
				else:
					turno=turno+1
					CambiarJugador(turno,jugador1,jugador2)	
				#imprime resultado de las casillas y quien gana				
				Resultado(jugador1,jugador2)
				Total(jugador1,jugador2,ficha)
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
				pygame.draw.rect(ventana,color,[(MARGEN+LARGO) * y + MARGEN, (MARGEN+ALTO) * x + MARGEN, LARGO, ALTO])
				pygame.draw.circle(ventana,colorf,[(MARGEN+LARGO) * y + MARGEN+25, (MARGEN+ALTO) * x + MARGEN+25],LARGO//2)

		# Limitamos a 60 fotogramas por segundo.
		clock.tick(60)
		# Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
		pygame.display.flip()

Partida() # llamada de la función principal
# Preguntar a los usuarios si quieren jugar otra rartida
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
		Partida()			
