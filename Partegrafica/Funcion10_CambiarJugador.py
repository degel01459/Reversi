def CambiarJugador(esTurno,player1,player2):	#Funcion que realiza el cambio de jugador
	if esTurno%2==0:
		return player1
	else:
		return player2
