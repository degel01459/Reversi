
def LlenaCasilla(esTurno,player1,player2):
	if esTurno%2==0:
		player2.casilla=player2.casilla+1
		player1.casilla=player1.casilla-1
	elif esTurno%2!=0:
		player1.casilla=player1.casilla-1
		player2.casilla=player2.casilla+1
		