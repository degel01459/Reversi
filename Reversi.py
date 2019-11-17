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
# 1 // Casillas Negras
# 2 // Casillas Blancas
import random
import sys

from Funcion0_Posicion			import inicio
from Funcion1_Imprimir			import imprimir
from Funcion2_QuieresJugar		import QuieresJugar
from Funcion3_Nombres			import Nombres
from Funcion4_QuedanFichas 		import QuedanFichas
from Funcion5_Turno		 		import Turno
from Funcion6_ObtenerJugada		import ObtenerJugada

from Funcion9_Resultado			import Resultado
from Funcion10_CambiarJugador 	import CambiarJugador
from Funcion11_Total			import Total

## CLASES ##
class jugador():
	nombre=""			# Definir string como valor de entrada para nombre
	j=0					# Definir string como valor de entrada para j que es jugada
	fichas=0			# Fichas acumuladas

## INICIALIZACION ##
x = 0					#fila
y = 0					#columna
turno = 1				#turno empieza el jugador 1
fichas= 60				#fichas
partida = 1				#Numero de Partidas 
jugador1 = jugador()	#invoca la clase
jugador2 = jugador()	#invoca la clase
jugador1.j = 1			#El valor del jugador1
jugador2.j = 2			#El valor del jugador2
jugador1.fichas = 0		#Fichas acumuladas del jugador1
jugador2.fichas = 0		#Fichas acumuladas del jugador2


## PRE-PROGRAMA ##

print("")
print("	REVERSI	")
print("")

reversi=[[0 for j in range(0,8)]for i in range(0,8)]


## PROGRAMA PRINCIPAL ##

inicio(reversi)
imprimir(reversi,fichas)
while QuieresJugar() == "SI":
	otra = "SI"
	while otra == "SI":
		Nombres(jugador,jugador1,jugador2,partida)
		print("Los nombres dados son: ",jugador1.nombre, jugador2.nombre)
		print("Fichas Negras: ",jugador1.j,"Fichas Blancas: ",jugador2.j)
		while QuedanFichas(fichas):
			jugador = Turno(turno, jugador, jugador1, jugador2)
			x,y = ObtenerJugada(x,y)
			"""
			try:
				assert ( EsValida(x,y,z,N,T)==True )
				print("Jugada Valida Posicion T[z][x][y] = T[",z,"][",x,"][",y,"]")		
			except:
				while EsValida(x,y,z,N,T)==False:
					print("Jugada Invalida: Fuera de limites o Posicion ya ocupada")
					print("Intente Nuevamente")
					x,y,z = ObtenerJugada(x,y,z,N)
			if T[z][x][y] == 0:
				T[z][x][y] = jugador.j
				jugador.lineas = jugador.lineas + HayLinea(x,y,z,T,N,turno)
				"""
			Resultado(reversi,jugador,jugador1,jugador2)
			fichas = fichas - 1
			CambiarJugador(jugador,jugador1,jugador2)
			turno = turno + 1
		Total(jugador1,jugador2,jugador)
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
		partida = partida + 1
		reversi=[[0 for j in range(0,8)]for i in range(0,8)]
		fichas= 60
		turno = 1




