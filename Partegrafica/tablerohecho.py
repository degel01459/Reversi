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

#FUNSIONES


#COLORES
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 50, 200, 50)
ROJO = (255, 0, 0)
AZUL = (0,0,255)
FONDO = (24, 25, 30)

# Casillas
LARGO  = 20
ALTO = 20
MARGEN = 5

#IMAGENES
#tablero= pygame.image.load("tablero.bmp").convert()
#blanca= pygame.image.load("blanca.bmp").convert()
#negra= pygame.image.load("negra.bmp").convert()
#nada= pygame.image.load("nada.bmp").convert()
#selec= pygame.image.load("selec.bmp").convert()

#INICIALIZACION
x=0
y=0
PLAYERS = [1,2]

#VENTANA
DIMENCIONES = [600,600]
SELECCIONA = (220, 200, 0)
LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def dibujarTablero(screen, dimension, p_inicio, tamanio_fuente, fuente, seleccion):
	'''
	# Funcion que dibuja el tablero
	screen: 		referencia del lienzo donde dibujar
	dimension: 		tamanio de los rectangulos
	p_inicio: 		coordenadas del punto de inicio del tablero
	tamanio_fuente: tamanio de fuente segun el tablero
	fuente: 		Objeto fuente 
	seleccion: 		rectangulo seleccionado 
	'''
	color = 0
	for i in range(8):
		for j in range(8):
			x = i * dimension + p_inicio[0]
			y = j * dimension + p_inicio[1]
			pygame.draw.rect(screen, VERDE, [x, y, dimension, dimension], 0)
			if seleccion[0] == i and j == seleccion[1] :
				pygame.draw.rect(screen, SELECCIONA, [x, y, dimension, dimension], 0)
			color += 1
		color += 1
		dibujarTexto(screen, LETRAS[i], [i * dimension + p_inicio[0], p_inicio[1] - tamanio_fuente], fuente)
		dibujarTexto(screen, str(i + 1), [p_inicio[0] - tamanio_fuente, i * dimension + p_inicio[1]], fuente)

def dibujarTexto(screen, texto, posicion, fuente):
	Texto = fuente.render(texto, 1, AZUL)
	screen.blit(Texto, posicion)

def ajustarMedidas(tamanio_fuente):
	if DIMENCIONES[1] < DIMENCIONES[0]:
		ancho = int((DIMENCIONES[1] - (tamanio_fuente * 2)) / 8)
		inicio = ((DIMENCIONES[0] - DIMENCIONES[1]) / 2) + tamanio_fuente, tamanio_fuente
	else:
		ancho = int((DIMENCIONES[0] - (tamanio_fuente * 2)) / 8)
		inicio = tamanio_fuente, ((DIMENCIONES[1] - DIMENCIONES[0]) / 2) + tamanio_fuente
	return [inicio, ancho]

def obtenerPosicion(mouse, dimension, p_inicio, actual):
	xr, yr = mouse[0], mouse[1]
	for i in range(8):
		 for j in range(8):
		 	x = i * dimension + p_inicio[0]
		 	y = j * dimension + p_inicio[1]
		 	if (xr >= x) and (xr <= x + dimension) and (yr >= y) and (yr <= y + dimension):
		 		actual = [i, j]
	return actual

def main():
	pygame.init()
	screen = pygame.display.set_mode(DIMENCIONES)
	pygame.display.set_caption("Othello")
	game_over = False
	clock = pygame.time.Clock()
	tamanio_fuente = 30
	seleccion = [-1, -1]
	fuente =  pygame.font.Font(None,30)
	puntoInicio, dimension = ajustarMedidas(tamanio_fuente)
	while game_over is False:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				game_over = True
		botones = pygame.mouse.get_pressed()
		if botones[0]:
			pos = pygame.mouse.get_pos()
			seleccion = obtenerPosicion(pos, dimension, puntoInicio, seleccion)
			print(seleccion)
		screen.fill(FONDO)
		dibujarTablero(screen, dimension, puntoInicio, tamanio_fuente, fuente, seleccion)
		pygame.display.flip()
		clock.tick(60)
	pygame.quit()
if __name__ == "__main__":
	main()