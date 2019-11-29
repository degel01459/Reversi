import pygame
import sys
import os
import random

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

# Establecemos el LARGO y ALTO de cada celda de la retícula.
LARGO  = 50
ALTO = 50

# Establecemos el margen entre las celdas.
MARGEN = 10

# Creamos un array bidimensional. Un array bidimensional
# no es más que una lista de listas.
reversi=[[0 for j in range(0,8)]for i in range(0,8)]
inicio(reversi)
imprimir(reversi)

# Inicializamos pygame
pygame.init()

# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [490, 490]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
os.environ['SDL_VIDEO_CENTERED'] = '1'	#Para centrar la ventana a la hora de abrirse 

# Establecemos el título de la pantalla.
pygame.display.set_caption("REVERSI")

# Iteramos hasta que el usuario pulse el botón de salir.
cerrar = False

# Lo usamos para establecer cuán rápido de refresca la pantalla.
reloj = pygame.time.Clock()

# Bucle Principal del Programa
while not cerrar:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            cerrar = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # El usuario presiona el ratón. Obtiene su posición.
            pos = pygame.mouse.get_pos()
            # Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            # Establece esa ubicación a cero
            reversi[fila][columna] = 1
            print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)
    # Establecemos el fondo de pantalla.
    pantalla.fill(NEGRO)
     # Dibujamos la retícula
    for fila in range(8):
        for columna in range(8):
            color = BLANCO
            if reversi[fila][columna] == 1:
                color = NEGRO
            pygame.draw.rect(pantalla,color,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])

    # Limitamos a 60 fotogramas por segundo.
    reloj.tick(60)
 
    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
     
# Pórtate bien con el IDLE.
pygame.quit()