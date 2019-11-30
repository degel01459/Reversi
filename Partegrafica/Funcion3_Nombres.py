def Nombres(player1,player2,match):					#Procedimiento que asigna los nombres de los jugadores
	while True:						#Indica el número de partidas que se llevan jugando
		try:
			player1.nombre = "ALE"#input("Por favor ingrese nombre del jugador 1: ")
			player2.nombre = "KEV"#input("Por favor ingrese nombre del jugador 2: ")
			assert(len(player1.nombre)>0 and len(player2.nombre)>0)
			break
		except:
			pass
	