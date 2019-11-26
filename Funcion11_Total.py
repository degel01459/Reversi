def Total(player1,player2):		#Funcion que indica el resultado total de la partida.
	if player1.casilla>player2.casilla:
		print("Gana: ",player1.nombre)
	elif player1.casilla<player2.casilla:
		print("Gana: ",player2.nombre)
	elif player1.casilla==player2.casilla:
		print("Empate")