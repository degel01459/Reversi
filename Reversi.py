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
# 1 // casillas blacas
# 2 // casillas Negras
import random
import sys

from Funcion0_Posicion			import incio
from Funcion1_Imprimir			import imprimir
from Funcion2_QuieresJugar		import QuieresJugar
from Funcion3_Nombres			import Nombres
from Funcion4_QuedanFichas 		import QuedanFichas
from Funcion5_Turno		 		import Turno

## CLASES ##
class jugador():
	nombre=""			# Definir string como valor de entrada para nombre
	j=0					# Definir string como valor de entrada para j que es jugada

"""class Cordenadas():
	i=0
	j=0"""

## INICIALIZACION ##
x = 0					#fila
y = 0					#columna
turno = 1				#turno empieza el jugador 1
fichas=64				#fichas
partida = 1				#Numero de Partidas 
jugador1 = jugador()	#invoca la clase
jugador2 = jugador()	#invoca la clase
jugador1.j = 1			#El valor del jugador1
jugador2.j = 2			#El valor del jugador2
jugador1.ficha=1
jugador2.ficha=2		


## PRE-PROGRAMA ##

print("")
print("		REVERSI		")
print("")

reversi=[[0 for j in range(0,8)]for i in range(0,8)]


## ESTRUCTURA ACTUAL ##

incio(reversi)
imprimir(reversi,fichas)

while QuieresJugar() == 1:
	otra = 1					#Otra partida
	while otra == 1 :
		Nombres(jugador,jugador1,jugador2,partida)
		while QuedanFichas(fichas):
			jugador = Turno(turno, jugador, jugador1, jugador2)



print("los nombres dados son: ",jugador1.nombre, jugador2.nombre)
print(jugador1.ficha, jugador2.ficha)
imprimir(reversi)


