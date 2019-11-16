import random
def Nombres(jugador,jugador1,jugador2,partida):											#Procedimiento que asigna los nombres de los jugadores
	print("Es la Partida: ",partida)													#Indica el número de partidas que se llevan jugando
	jugador1.nombre=random.choice(["Jose","Kevin","Angel","Carlos","Miguel"])			#input("Nombre del jugador1: ")
	jugador2.nombre=random.choice(["Carla","Karen","Luisa","Kathe","Gaby"])				#input("Nombre del jugador2: ")