def Total(player1,player2,fichas):		#Funcion que indica el resultado total de la partida.
	if fichas==0:
		empate="Empate"
		if player1.casilla>player2.casilla:
			return player1.nombre
		elif player1.casilla<player2.casilla:
			return player2.nombre
		elif player1.casilla==player2.casilla:
			return empate