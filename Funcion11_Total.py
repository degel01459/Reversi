def Total(jugador1,jugador2,jugador):		#Funcion que indica el resultado total de la partida.
	if jugador1.casillas>jugador2.casillas:
		print("Gana: ",jugador1.nombre)
	elif jugador1.casillas<jugador2.casillas:
		print("Gana: ",jugador2.nombre)
	else:
		print("Empate")