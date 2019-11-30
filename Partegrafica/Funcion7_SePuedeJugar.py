def SePuedeJugar(player1,player2):
	jugar=True
	if player1.casilla>=1 and player2.casilla>=1:
		pass
	elif player1.casilla<1 or player2.casilla<1:
		jugar=False
	
	return jugar
			