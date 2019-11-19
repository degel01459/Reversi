def Nombres(player1,player2,match):					#Procedimiento que asigna los nombres de los jugadores
	print("")
	print("	REVERSI ")
	print("")
	print("Es la Partida: ",match)	
	while True:						#Indica el número de partidas que se llevan jugando
		try:
			print(" Jugardor1 Fichas negras=1 y Jugador2 Fichas blancas=2")
			player1.nombre = input("Por favor ingrese nombre del jugador 1: ")
			player2.nombre = input("Por favor ingrese nombre del jugador 2: ")
			assert(len(player1.nombre)>0 and len(player2.nombre)>0)
			break
		except:
			print("no puede queda en blanco")
			print("Debe intoducir al menos un caracter")
			print("")
	