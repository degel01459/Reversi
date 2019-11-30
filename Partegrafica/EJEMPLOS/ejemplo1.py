# -*- coding: utf-8 -*-
import pygame
import sys
import os 	#Para centrar la ventana del juego cada vez que se abra
import random #Util para que se pueda elegir aleatoreamente quien juega primero
from pygame.locals import *

pygame.init() #Inicializar la pantalla del juego 

os.environ['SDL_VIDEO_CENTERED'] = '1'	#Para centrar la ventana a la hora de abrirse 

# RGB: Rojo, Verde, Azul
VERDE = (0,128,64) 
AZUL =(0, 0, 255)
BLACK = (0, 0, 0)  ##Forma de colocar color a la pantalla (TUPLA)
ROJO = (255, 0, 0)
Colorfondo = pygame.Color(255, 255, 255)  ##Segunda forma de colocar color

########################################################################

ventana = pygame.display.set_mode((1500, 700), pygame.RESIZABLE)  ##Establece el ancho y alto de la ventana a crear
pygame.display.set_caption("La vieja 3D")  #Para colocar el titulo a la ventana
reloj = pygame.time.Clock() #variable reloj usada para establecer nuestro tiempo de actualizacion de la pantalla, usando FPS

########### Escribo la fuente ##############
fuente = pygame.font.Font(None, 100) #Tamaño-letra del titulo
titulo = fuente.render("La vieja 3D", True, BLACK)  #Titulo en el juego
####################################################

def captureJugadores():

    fuenteJugador = pygame.font.Font(None, 80)
    fuenteJugador.set_italic(True)

    jugador = fuenteJugador.render("NOMBRE DEL JUGADOR 1:", True, VERDE)

    nombreJugador = ["","",""]

    nextPantalla = False
    turnoJugador = 0 ### turnoJugador = 0 Captura el nombre del jugador 1

    while nextPantalla == False:
        ventana.fill(Colorfondo)  ## se coloca la pantalla el color
        ventana.blit(titulo, (500, 10))

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key != 13:
                    print(evento.key)
                    llenarBuffer(nombreJugador,evento.key,turnoJugador)
                    print(nombreJugador)
                elif turnoJugador == 0 and evento.key == 13 and len(nombreJugador[0]) > 0 and len(nombreJugador[0]) <= 11:
                    turnoJugador = 1 ### turnoJugador = 1 Captura el nombre del jugador 2
                elif turnoJugador == 1 and evento.key == 13 and len(nombreJugador[1]) > 0 and len(nombreJugador[0]) <= 11:
                    turnoJugador = 2 ### turnoJugador = 2 Captura el tamaño del tablero
                elif turnoJugador == 2 and evento.key == 13 and len(nombreJugador[2]) > 0:
                    if int(nombreJugador[turnoJugador]) >= 1 and int(nombreJugador[turnoJugador]) <= 5:
                        nextPantalla = True
                    else:
                        pass

            elif evento.type == QUIT:
                pygame.quit()
                sys.exit()

        if turnoJugador == 0:
            longitud = ventana.blit(jugador, (0, 200))
            error = fuenteJugador.render("máximo de 11 caracteres", True, ROJO)
            if len(nombreJugador[turnoJugador]) > 0:
                nombre = fuenteJugador.render(nombreJugador[turnoJugador], True, BLACK)
                ventana.blit(nombre, (longitud.width + 10, 200))

                if len(nombreJugador[turnoJugador]) > 12:
                    ventana.blit(error, (0, 300))

        elif turnoJugador == 1:
            longitud = ventana.blit(jugador, (0, 200))
            ventana.blit(nombre, (longitud.width + 10, 200))

            jugador2 = fuenteJugador.render("NOMBRE DEL JUGADOR 2:", True, VERDE)
            longitud2 = ventana.blit(jugador2, (0, 400))
            if len(nombreJugador[turnoJugador]) > 0:
                nombre2 = fuenteJugador.render(nombreJugador[turnoJugador], True, BLACK)
                ventana.blit(nombre2, (longitud2.width + 10, 400))

                if len(nombreJugador[turnoJugador]) > 12:
                    ventana.blit(error, (0, 500))
        else:
            jugador = fuenteJugador.render("LONGITUD DEL TABLERO:", True, BLACK)
            longitud = ventana.blit(jugador, (0, 200))

            error = fuenteJugador.render("El tamaño del tablero debe ser entre 1 y 5", True, ROJO)
            if len(nombreJugador[turnoJugador]) > 0:
                Longitudtablero = fuenteJugador.render(nombreJugador[turnoJugador], True, BLACK)
                ventana.blit(Longitudtablero, (longitud.width + 10, 200))

                if int(nombreJugador[turnoJugador]) < 1 or int(nombreJugador[turnoJugador]) >= 6:
                    ventana.blit(error, (0, 400))

        reloj.tick(40)
        pygame.display.update()

    return nombreJugador

def llenarBuffer(nombreJugador,key,turno):
    if key >= 97 and key <= 122 and (turno == 0 or turno == 1):
        caracter = traductor(key)
        nombreJugador[turno] = nombreJugador[turno] + caracter
    elif key == 32 and (turno == 0 or turno == 1):
        nombreJugador[turno] = nombreJugador[turno] + " "
    elif key >= K_0 and key <= K_9 and turno == 2:
        caracter = traductor(key)
        nombreJugador[turno] = nombreJugador[turno] + caracter
    elif key == 8:
        longitud = len(nombreJugador[turno])
        aux = nombreJugador[turno]
        nombreJugador[turno] = aux[0:longitud-1]
    return

def traductor(key):
    if key == 97:
        caracter = "A"
    elif key == 98:
        caracter = "B"
    elif key == 99:
        caracter = "C"
    elif key == 100:
        caracter = "D"
    elif key == 101:
        caracter = "E"
    elif key == 102:
        caracter = "F"
    elif key == 103:
        caracter = "G"
    elif key == 104:
        caracter = "H"
    elif key == 105:
        caracter = "I"
    elif key == 106:
        caracter = "J"
    elif key == 107:
        caracter = "K"
    elif key == 108:
        caracter = "L"
    elif key == 109:
        caracter = "M"
    elif key == 110:
        caracter = "N"
    elif key == 111:
        caracter = "O"
    elif key == 112:
        caracter = "P"
    elif key == 113:
        caracter = "Q"
    elif key == 114:
        caracter = "R"
    elif key == 115:
        caracter = "S"
    elif key == 116:
        caracter = "T"
    elif key == 117:
        caracter = "U"
    elif key == 118:
        caracter = "V"
    elif key == 119:
        caracter = "W"
    elif key == 120:
        caracter = "X"
    elif key == 121:
        caracter = "Y"
    elif key == 122:
        caracter = "Z"
    elif key == 48:
        caracter = "0"
    elif key == 49:
        caracter = "1"
    elif key == 50:
        caracter = "2"
    elif key == 51:
        caracter = "3"
    elif key == 52:
        caracter = "4"
    elif key == 53:
        caracter = "5"
    elif key == 54:
        caracter = "6"
    elif key == 55:
        caracter = "7"
    elif key == 56:
        caracter = "8"
    elif key == 57:
        caracter = "9"

    return caracter

def printPuntos(nombreJ1,nombreJ2,puntosJ1,puntosJ2,longitudT):
    count = 0

    fuente = pygame.font.Font(None, 40)
    fuente.set_italic(True)

    marcador = fuente.render("MARCADOR", True, BLACK)
    ventana.blit(marcador, (600, 5))

    pygame.draw.rect(ventana, BLACK, (0, 35, 1500, 150), 2)
    posicionLin = 500

    nombre = fuente.render("Nombre", True, BLACK)
    ubicacion = ventana.blit(nombre, (200, 40))
    pygame.draw.line(ventana, BLACK, (posicionLin, 35), (posicionLin, 185), 4)

    ############################# Puntos linea Horizontal #########

    lineaH = fuente.render("Lin.H", True, BLACK)
    ubicacion = ventana.blit(lineaH, (505, 40))
    posicionLin = posicionLin + ubicacion.width + 10
    pygame.draw.line(ventana, BLACK, (posicionLin, 35), (posicionLin, 185), 4)

    ############################# Coloco los puntos de las lineas horizontales de cada jugador #########

    turno = 1
    for i in range(0,longitudT):
        if lineaHorizontal(A, i, 0, 1, turno, pos_tablero):
            count = count + 1
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, (505 + 30, ubicacion.height + 55))
    turno = 2
    count = 0
    for i in range(0,longitudT):
        if lineaHorizontal(A, i, 0, 1, turno, pos_tablero):
            count = count + 1
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, (505 + 30, ubicacion.height + 55 + 55))

    ############################# Puntos linea Vertical #########

    lineaV = fuente.render("Lin.V", True, BLACK)
    ubicacion = ventana.blit(lineaV, (posicionLin + 5, 40))
    posicionLin = posicionLin + ubicacion.width + 10
    pygame.draw.line(ventana, BLACK, (posicionLin, 35), (posicionLin, 185), 4)

    ############################# Coloco los puntos de las lineas Verticales de cada jugador #########
    count = 0
    turno = 1
    for i in range(0, longitudT):
        if lineaVertical(A, 0, i, 1, turno, pos_tablero):
            count = count + 1
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, ((posicionLin - ubicacion.width + 10) + 15, ubicacion.height + 55))
    turno = 2
    count = 0
    for i in range(0, longitudT):
        if lineaVertical(A, 0, i, 1, turno, pos_tablero):
            count = count + 1
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, ((posicionLin - ubicacion.width + 10) + 15, ubicacion.height + 55 + 55))

    ############################# Puntos linea Diagonal #########

    lineaV = fuente.render("Lin.Dia", True, BLACK)
    ubicacion = ventana.blit(lineaV, (posicionLin + 5, 40))
    posicionLin = posicionLin + ubicacion.width + 10
    pygame.draw.line(ventana, BLACK, (posicionLin, 35), (posicionLin, 185), 4)

    ############################# Coloco los puntos de las lineas Diagonal de cada jugador #########
    count = 0
    turno = 1
    if lineaDiagonal(A, 0, 0, 1, turno, pos_tablero):
        count = count + 1
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, ((posicionLin - ubicacion.width + 10) + 20, ubicacion.height + 55))
    turno = 2
    count = 0
    if lineaDiagonal(A, 0, 0, 1, turno, pos_tablero):
        count = count + 1
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, ((posicionLin - ubicacion.width + 10) + 20, ubicacion.height + 55 + 55))

    ############################# Puntos linea Diagonal Inversa #########

    lineaV = fuente.render("Lin.Dia.Inv", True, BLACK)
    ubicacion = ventana.blit(lineaV, (posicionLin + 5, 40))
    posicionLin = posicionLin + ubicacion.width + 10
    pygame.draw.line(ventana, BLACK, (posicionLin, 35), (posicionLin, 185), 4)

    ############################# Coloco los puntos de las lineas Diagonal Inversa de cada jugador #########
    count = 0
    turno = 1
    if lineaDiagonalInversa(A, 0, longitudT - 1, 1, turno, pos_tablero):
        count = count + 1
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, ((posicionLin - ubicacion.width + 10) + 40, ubicacion.height + 55))
    turno = 2
    count = 0
    if lineaDiagonalInversa(A, 0, longitudT - 1, 1, turno, pos_tablero):
        count = count + 1
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, ((posicionLin - ubicacion.width + 10) + 40, ubicacion.height + 55 + 55))

    ############################# Puntos linea Entre tableros #########

    lineaV = fuente.render("Lin.Entre Tableros", True, BLACK)
    ubicacion = ventana.blit(lineaV, (posicionLin + 5, 40))
    posicionLin = posicionLin + ubicacion.width + 10
    pygame.draw.line(ventana, BLACK, (posicionLin, 35), (posicionLin, 185), 4)

    ########################### DESAROOLLAR !! JUGADAS ENTRE TABLEROS ##################################
    count = 0
    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, ((posicionLin - ubicacion.width + 10) + 90, ubicacion.height + 55))

    puntos = fuente.render(str(count), True, BLACK)
    ventana.blit(puntos, ((posicionLin - ubicacion.width + 10) + 90, ubicacion.height + 55 + 55))

    ###############################################################################################

    lineaV = fuente.render("TOTAL", True, BLACK)
    ventana.blit(lineaV, (posicionLin + 100, 40))

    puntos = fuente.render(str(puntosJ1), True, BLACK)
    ventana.blit(puntos, ((posicionLin) + 130, ubicacion.height + 55))

    puntos = fuente.render(str(puntosJ2), True, BLACK)
    ventana.blit(puntos, ((posicionLin) + 130, ubicacion.height + 55 + 55))

    pygame.draw.line(ventana, BLACK, (0, ubicacion.height + 40), (1500, ubicacion.height + 40), 4)

    nombrejugador1 = fuente.render(nombreJ1,True, BLACK)
    ubicacion = ventana.blit(nombrejugador1, (200, ubicacion.height + 55))

    pygame.draw.line(ventana, BLACK, (0, ubicacion.height + 90), (1500, ubicacion.height + 90), 2)

    nombrejugador2 = fuente.render(nombreJ2,True, BLACK)
    ubicacion = ventana.blit(nombrejugador2, (200, ubicacion.height + 55 + 55))


def inicio():   #Pantalla de bienvenida

    fuenteOpcion = pygame.font.Font(None, 80)
    fuenteOpcion.set_italic(True)  #Le asigno el tipo de letra
    opcionJugar = fuenteOpcion.render("JUGAR", True, BLACK)
    opcionSalir = fuenteOpcion.render("SALIR", True, BLACK)

    nextPantalla = False  #mientras next pantalla sea False, no pasa de la pantalla de bienvenida

    while nextPantalla == False:
        ventana.fill(Colorfondo)  #se coloca el color de la pantalla
        ventana.blit(titulo, (500, 10)) #Blit es para que aparezca o se coloque en pantalla el string o letras guardadas

        botonJugar = ventana.blit(opcionJugar, (550, 200))
        botonSalir = ventana.blit(opcionSalir, (550, 400))

        for evento in pygame.event.get():
            coordenada = pygame.mouse.get_pos()  #esta funcion mouse.get.pos sirve para saber la coordenada o pixel donde este el cursor
            ancho = botonJugar.x + botonJugar.width
            largo = botonJugar.y + botonJugar.height
            if coordenada[0] >= botonJugar.x and coordenada[0] <= ancho and coordenada[1] >= botonJugar.y and coordenada[1] <= largo:
                fuenteOpcion.set_underline(True)  #si el cursor esta dentro del ancho y largo, se subraya el titulo
                opcionJugar = fuenteOpcion.render("JUGAR", True, VERDE) #le cambiamos el color de la letra para resaltar que el cursor esta por encima de este boton
            else:
                fuenteOpcion.set_underline(False)
                opcionJugar = fuenteOpcion.render("JUGAR", True, BLACK)

            ancho = botonSalir.x + botonSalir.width
            largo = botonSalir.y + botonSalir.height
            if coordenada[0] >= botonSalir.x and coordenada[0] <= ancho and coordenada[1] >= botonSalir.y and coordenada[1] <= largo:
                fuenteOpcion.set_underline(True)
                opcionSalir = fuenteOpcion.render("SALIR", True, ROJO)
            else:
                fuenteOpcion.set_underline(False)
                opcionSalir = fuenteOpcion.render("SALIR", True, BLACK)

            if evento.type == pygame.MOUSEBUTTONDOWN:
                coordenada = pygame.mouse.get_pos()

                ancho = botonJugar.x + botonJugar.width
                largo = botonJugar.y + botonJugar.height
                if coordenada[0] >= botonJugar.x and coordenada[0] <= ancho and coordenada[1] >= botonJugar.y and coordenada[1] <= largo:
                    nextPantalla = True

                ancho = botonSalir.x + botonSalir.width
                largo = botonSalir.y + botonSalir.height
                if coordenada[0] >= botonSalir.x and coordenada[0] <= ancho and coordenada[1] >= botonSalir.y and coordenada[1] <= largo:
                    pygame.quit()
                    sys.exit()
            elif evento.type == QUIT:
                pygame.quit()
                sys.exit()

        reloj.tick(40)
        pygame.display.update()

    return nextPantalla

############################################################

def lineaVertical(A, fila, columna, modo, turno, pos_tablero):
    if modo == 0:
        if fila == (longitudT - 1) and (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 3) and turno == 1:
            A[pos_tablero][fila][columna] = 3
            return True
        elif fila == (longitudT - 1) and (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 4) and turno == 2:
            A[pos_tablero][fila][columna] = 4
            return True
        elif (fila == (longitudT - 1) and A[pos_tablero][fila][columna] != turno) or (A[pos_tablero][fila][columna] != turno and A[pos_tablero][fila][columna] != 3 and A[pos_tablero][fila][columna] != 4):
            return False
        elif (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 3) and turno == 1:
            if lineaVertical(A, fila + 1, columna, modo, turno, pos_tablero) == True:
                A[pos_tablero][fila][columna] = 3
                return True
            else:
                return False
        elif (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 4) and turno == 2:
            if lineaVertical(A, fila + 1, columna, modo, turno, pos_tablero) == True:
                A[pos_tablero][fila][columna] = 4
                return True
            else:
                return False
        else:
            return False

    else:
        if fila == (longitudT - 1) and A[pos_tablero][fila][columna] == 3 and turno == 1:
            return True
        elif fila == (longitudT - 1) and A[pos_tablero][fila][columna] == 4 and turno == 2:
            return True
        elif fila == (longitudT - 1) and ((A[pos_tablero][fila][columna] != 3 and turno == 1) or (A[pos_tablero][fila][columna] != 4 and turno == 2)):
            return False
        elif A[pos_tablero][fila][columna] == 3 and turno == 1:
            return lineaVertical(A, fila + 1, columna, modo, turno, pos_tablero)
        elif A[pos_tablero][fila][columna] == 4 and turno == 2:
            return lineaVertical(A, fila + 1, columna, modo, turno, pos_tablero)
        else:
            return False

def lineaHorizontal(A, fila, columna, modo, turno, pos_tablero):
    if modo == 0:
        if columna == (longitudT - 1) and (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 3) and turno == 1:
            A[pos_tablero][fila][columna] = 3
            return True
        elif columna == (longitudT - 1) and (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 4) and turno == 2:
            A[pos_tablero][fila][columna] = 4
            return True
        elif (columna == (longitudT - 1) and A[pos_tablero][fila][columna] != turno) or (A[pos_tablero][fila][columna] != turno and A[pos_tablero][fila][columna] != 3 and A[pos_tablero][fila][columna] != 4):
            return False
        elif (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 3) and turno == 1:
            if lineaHorizontal(A, fila, columna + 1, modo, turno, pos_tablero) == True:
                A[pos_tablero][fila][columna] = 3
                return True
            else:
                return False
        elif (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 4) and turno == 2:
            if lineaHorizontal(A, fila, columna + 1, modo, turno, pos_tablero) == True:
                A[pos_tablero][fila][columna] = 4
                return True
            else:
                return False
        else:
            return False

    else:
        if columna == (longitudT - 1) and A[pos_tablero][fila][columna] == 3 and turno == 1:
            return True
        elif columna == (longitudT - 1) and A[pos_tablero][fila][columna] == 4 and turno == 2:
            return True
        elif columna == (longitudT - 1) and ((A[pos_tablero][fila][columna] != 3 and turno == 1) or (A[pos_tablero][fila][columna] != 4 and turno == 2)):
            return False
        elif A[pos_tablero][fila][columna] == 3 and turno == 1:
            return lineaHorizontal(A, fila, columna + 1, modo, turno, pos_tablero)
        elif A[pos_tablero][fila][columna] == 4 and turno == 2:
            return lineaHorizontal(A, fila, columna + 1, modo, turno, pos_tablero)
        else:
            return False

def lineaDiagonal(A, fila, columna, modo, turno, pos_tablero):
    if modo == 0:
        if (columna == (longitudT - 1) and fila == (longitudT - 1)) and (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 3) and turno == 1:
            A[pos_tablero][fila][columna] = 3
            return True
        elif (columna == (longitudT - 1) and fila == (longitudT - 1)) and (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 4) and turno == 2:
            A[pos_tablero][fila][columna] = 4
            return True
        elif ((columna == (longitudT - 1) and fila == (longitudT - 1)) and A[pos_tablero][fila][columna] != turno) or (A[pos_tablero][fila][columna] != turno and A[pos_tablero][fila][columna] != 3 and A[pos_tablero][fila][columna] != 4):
            return False
        elif (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 3) and turno == 1:
            if lineaDiagonal(A, fila + 1, columna + 1, modo, turno, pos_tablero) == True:
                A[pos_tablero][fila][columna] = 3
                return True
            else:
                return False
        elif (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 4) and turno == 2:
            if lineaDiagonal(A, fila + 1, columna + 1, modo, turno, pos_tablero) == True:
                A[pos_tablero][fila][columna] = 4
                return True
            else:
                return False
        else:
            return False

    else:
        if (columna == (longitudT - 1) and fila == (longitudT - 1)) and A[pos_tablero][fila][columna] == 3 and turno == 1:
            return True
        elif (columna == (longitudT - 1) and fila == (longitudT - 1)) and A[pos_tablero][fila][columna] == 4 and turno == 2:
            return True
        elif (columna == (longitudT - 1) and fila == (longitudT - 1)) and ((A[pos_tablero][fila][columna] != 3 and turno == 1) or (A[pos_tablero][fila][columna] != 4 and turno == 2)):
            return False
        elif A[pos_tablero][fila][columna] == 3 and turno == 1:
            return lineaDiagonal(A, fila + 1, columna + 1, modo, turno, pos_tablero)
        elif A[pos_tablero][fila][columna] == 4 and turno == 2:
            return lineaDiagonal(A, fila + 1, columna + 1, modo, turno, pos_tablero)
        else:
            return False

def lineaDiagonalInversa(A, fila, columna, modo, turno, pos_tablero):
    if modo == 0:
        if (columna == 0 and fila == (longitudT - 1)) and (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 3) and turno == 1:
            A[pos_tablero][fila][columna] = 3
            return True
        elif (columna == 0 and fila == (longitudT - 1)) and (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 4) and turno == 2:
            A[pos_tablero][fila][columna] = 4
            return True
        elif ((columna == 0 and fila == (longitudT - 1)) and A[pos_tablero][fila][columna] != turno) or (A[pos_tablero][fila][columna] != turno and A[pos_tablero][fila][columna] != 3 and A[pos_tablero][fila][columna] != 4):
            return False
        elif (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 3) and turno == 1:
            if lineaDiagonalInversa(A, fila + 1, columna - 1, modo, turno, pos_tablero) == True:
                A[pos_tablero][fila][columna] = 3
                return True
        elif (A[pos_tablero][fila][columna] == turno or A[pos_tablero][fila][columna] == 4) and turno == 2:
            if lineaDiagonalInversa(A, fila + 1, columna - 1, modo, turno, pos_tablero) == True:
                A[pos_tablero][fila][columna] = 4
                return True
            else:
                return False
        else:
            return False

    else:
        if (columna == 0 and fila == (longitudT - 1)) and A[pos_tablero][fila][columna] == 3 and turno == 1:
            return True
        elif (columna == 0 and fila == (longitudT - 1)) and A[pos_tablero][fila][columna] == 4 and turno == 2:
            return True
        elif (columna == 0 and fila == (longitudT - 1)) and ((A[pos_tablero][fila][columna] != 3 and turno == 1) or (A[pos_tablero][fila][columna] != 4 and turno == 2)):
            return False
        elif A[pos_tablero][fila][columna] == 3 and turno == 1:
            return lineaDiagonalInversa(A, fila + 1, columna - 1, modo, turno, pos_tablero)
        elif A[pos_tablero][fila][columna] == 4 and turno == 2:
            return lineaDiagonalInversa(A, fila + 1, columna - 1, modo, turno, pos_tablero)
        else:
            return False

def coorIsDiagonalInversa(coor, fila, columna):
    i = 0
    isDiagonal = False

    print(coor)

    while i < longitudT and isDiagonal == False:
        coordenadas = coor[i]
        print(coordenadas)
        if fila == int(coordenadas[0]) and columna == int(coordenadas[1]):
            isDiagonal = True

        i = i + 1

    return isDiagonal

def verificarLinea(A,fila,columna,turno,longitudT, pos_tablero):
    count = 0

    if lineaVertical(A,0,columna,0,turno, pos_tablero) == True:
        count = count+1

    if lineaHorizontal(A, fila, 0, 0, turno, pos_tablero) == True:
        count = count +1

    if fila == columna and lineaDiagonal(A, 0, 0, 0, turno, pos_tablero) == True:
        count = count + 1

    if coorIsDiagonalInversa(coorDiagonalInversa, fila, columna) == True and lineaDiagonalInversa(A, 0, longitudT - 1, 0, turno, pos_tablero) == True:
        count = count + 1

    return count

def printTablero(coordenadaX,coordenadaY,longitud):
    x = coordenadaX
    y = coordenadaY
    for i in range(0, longitud):
        for j in range(0, longitud):
            pygame.draw.rect(ventana, BLACK, (x, y, 66, 66), 1)
            x = x + 66
        x = coordenadaX
        y = y + 66

    return

def verificarJugada(A,fila,columna,turno, pos_tablero):
    valida = False
    if columna >= 0 and columna <= 9 and fila >= 0 and fila <= 9:
        if A[pos_tablero][fila][columna] == 0 and turno == 1:
            A[pos_tablero][fila][columna] = 1
            valida = True

        elif A[pos_tablero][fila][columna] == 0 and turno == 2:
            A[pos_tablero][fila][columna] = 2
            valida = True
        else:
            pass
    else:
        pass

    return valida


inicio()   #Aqui comienza la programacion del juego
infoJugadores = captureJugadores() 

longitudT = int(infoJugadores[2])

A = [[[0 for i in range(0, longitudT)] for j in range(0, longitudT)] for k in range(0,longitudT)]

coordenadaMouse = [0, 0]
coordenadaTablero = [555,350]
coorDiagonalInversa = []

j = longitudT - 1
for i in range(0, longitudT):
    coorDiagonalInversa = coorDiagonalInversa + [str(i) + str(j)]
    j = j - 1

turno = random.randint(1,2)
puntosJ2 = 0
puntosJ1 = 0
linea = False

pos_tablero= 0

fila = 99
columna = 99

while True:
    ventana.fill(Colorfondo)  ## se coloca la pantalla el color

    for evento in pygame.event.get():  #Para verificar los eventos que estan sucediendo
        if evento.type == pygame.KEYDOWN:
            print(evento.key)
            fila = evento.key - 48
            columna = evento.key - 48

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            coordenadaMouse = pygame.mouse.get_pos()
            print(coordenadaMouse)
            i = 0
            x = coordenadaTablero[0]
            ancho = x + 66
            y = coordenadaTablero[1]
            largo = y + 66
            find = False
            while i < longitudT and find == False:
                if coordenadaMouse[0] >= x and coordenadaMouse[0] <= ancho:
                    columna = i
                    find = True
                i = i + 1
                ancho = ancho + 66
                x = x + 66
            if find == True:
                i = 0
                find = False
                while i < longitudT and find == False:
                    if coordenadaMouse[1] >= y and coordenadaMouse[1] <= largo:
                        fila = i
                        find = True
                    i = i + 1
                    largo = largo + 66
                    y = y + 66
        elif evento.type == QUIT:
            pygame.quit()
            sys.exit()

    printTablero(coordenadaTablero[0],coordenadaTablero[1],longitudT)

    if turno == 1 and verificarJugada(A,fila,columna,turno, pos_tablero) == True:
        puntosJ1 = puntosJ1 + verificarLinea(A,fila,columna,turno,longitudT, pos_tablero)
        turno = 2
    elif turno == 2 and verificarJugada(A,fila,columna,turno, pos_tablero) == True:
        puntosJ2 = puntosJ2 + verificarLinea(A,fila,columna,turno,longitudT, pos_tablero)
        turno = 1
        
    printPuntos(infoJugadores[0],infoJugadores[1],puntosJ1,puntosJ2,longitudT)

    fila = 99
    columna = 99

    print(puntosJ1)
    print(puntosJ2)
    print(A)
    for i in range(0, longitudT):
        for j in range(0, longitudT):
            if A[pos_tablero][i][j] == 1 or A[pos_tablero][i][j] == 3:
                x = coordenadaTablero[0] + 66 * j
                y = coordenadaTablero[1] + 66 * i
                pygame.draw.line(ventana, BLACK, (x + 5, y + 5), (x + 60, y + 60), 3)
                pygame.draw.line(ventana, BLACK, (x + 60, y + 5), (x + 5, y + 60), 3)
            elif A[pos_tablero][i][j] == 2 or A[pos_tablero][i][j] == 4:
                x = coordenadaTablero[0] + 66 * j
                y = coordenadaTablero[1] + 66 * i
                pygame.draw.circle(ventana, BLACK, [x + 33, y + 33], 30)
    x = coordenadaTablero[0] + 33
    y = coordenadaTablero[1] + 33

    for i in range(0, longitudT): ## Verifico las lineas verticales jugador 1
        if lineaVertical(A, 0, i, 1, 1, pos_tablero) == True:
            pygame.draw.line(ventana, ROJO, (x + (33*i), coordenadaTablero[1] + 0), (x + (33*i), coordenadaTablero[1] + (60 * longitudT)), 4)

        x = x + 33
    x = coordenadaTablero[0] + 33
    for i in range(0, longitudT): # Verifico las lineas verticales jugador 2
        if lineaVertical(A, 0, i, 1, 2, pos_tablero) == True:
            pygame.draw.line(ventana, ROJO, (x + (33*i), coordenadaTablero[1] + 0), (x + (33*i), coordenadaTablero[1] + (60 * longitudT)), 4)

        x = x + 33

    for i in range(0, longitudT): # Verifico las lineas horizonatles jugador 1
        if lineaHorizontal(A, i, 0, 1, 1, pos_tablero) == True:
            pygame.draw.line(ventana, ROJO, (coordenadaTablero[0] + 0, y + (33*i)), (coordenadaTablero[0] + (60 * longitudT), y + (33*i)), 4)

        y = y + 33
    y = coordenadaTablero[1] + 33
    for i in range(0, longitudT): # Verifico las lineas horizonatles jugador 2
        if lineaHorizontal(A, i, 0, 1, 2, pos_tablero) == True:
            pygame.draw.line(ventana, ROJO, (coordenadaTablero[0] + 0, y + (33*i)), (coordenadaTablero[0] + (60 * longitudT), y + (33*i)), 4)

        y = y + 33

    x = coordenadaTablero[0]
    y = coordenadaTablero[1]
    if lineaDiagonal(A, 0, 0, 1, 1, pos_tablero) == True: # Verifico las lineas diagonal jugador 1
        pygame.draw.line(ventana, ROJO, (x, y), (x + (60 *longitudT), y + (60*longitudT)), 4)
    if lineaDiagonal(A, 0, 0, 1, 2, pos_tablero) == True: # Verifico las lineas diagonal jugador 2
        pygame.draw.line(ventana, ROJO, (x, y), (x + (60 *longitudT), y + (60*longitudT)), 4)

    x = coordenadaTablero[0] + (66*longitudT)
    y = coordenadaTablero[1]
    if lineaDiagonalInversa(A, 0, longitudT - 1, 1, 1, pos_tablero) == True: # Verifico las lineas diagonal inversa jugador 1
        pygame.draw.line(ventana, ROJO, (x, y), (coordenadaTablero[0] , y + (66*longitudT)), 4)
    if lineaDiagonalInversa(A, 0, longitudT - 1, 1, 2, pos_tablero) == True: # Verifico las lineas diagonal inversa jugador 2
        pygame.draw.line(ventana, ROJO, (x, y), (coordenadaTablero[0] , y + (66*longitudT)), 4)



    reloj.tick(40)  #nos permitira configurar la pantalla para que se actualice cada cuanto nosotros queramos
    pygame.display.update()
