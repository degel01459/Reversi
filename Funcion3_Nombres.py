def Nombres(player1,player2,match):					#Procedimiento que asigna los nombres de los jugadores
	while True:						#Indica el número de partidas que se llevan jugando
		try:
			name=[input("nombre"+str(i)+": ") for i in range(1,3)]
			#assert(len(player1.nombre)>0 and len(player2.nombre)>0)
			break
		except:
			pass
	if player1.nombre==name[1]:
		player2.nombre = name[2]#input("Por favor ingrese nombre del jugador 2: ")
	else:
		player2.nombre=name[1]	
	print(player1.nombre,player2.nombre)	
	#assert(len(player1.nombre)>0 and len(player2.nombre)>0)