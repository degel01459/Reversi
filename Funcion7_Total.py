def Total(player1,player2,fichas):
	if fichas==0 or player1.casilla==0 or player2.casilla==0:
		empate="Empate"
		if player1.casilla>player2.casilla:
			return player1.nombre
		elif player1.casilla<player2.casilla:
			return player2.nombre
		elif player1.casilla==player2.casilla:
			return empate