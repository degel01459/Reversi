# Descripción: Reversi es un cásico juego de mesa.
# Autores: Angel Rodriguez, Kevin Briceño
# Fecha de modificación: 12/11/2019
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

def Partida():	
	jugador1.casilla=2
	jugador2.casilla=2
	x=0
	y=0
	turno=1
	reversi=[[0 for j in range(0,8)]for i in range(0,8)]
	ficha=60
	print("jugador1 es: ",jugador1.nombre,"jugador2 es: ", jugador2.nombre)
	inicio(reversi)	
	imprimir(reversi)
	while QuedanFichas(ficha) and SePuedeJugar(jugador1,jugador2):
		jugador=Turno(turno,jugador1,jugador2)
		
		x,y=ObtenerJugada(x,y)
		
		if JugadaValida(reversi,x,y,jugador):
			RealizarJugada(reversi,x,y,jugador,jugador1,jugador2)
			ficha=ficha-1
			LlenaCasilla(reversi,jugador,jugador1,jugador2)
			imprimir(reversi)
			turno=turno+1
			CambiarJugador(turno,jugador1,jugador2)
		else:
			print("error, la posicion no es válida")
	imprimir(reversi)		
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
		Partida()			

