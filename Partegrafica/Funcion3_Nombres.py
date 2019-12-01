import random
def Nombres(player1,player2,match):					#Procedimiento que asigna los nombres de los jugadores
	while True:						#Indica el número de partidas que se llevan jugando
		try:
			name=[input("nombre del jugador "+str(i+1)+": ") for i in range(0,2)]
			assert(all(len(name[i])>0 for i in range(0,2)))
			break
		except:
			pass
			
			
	player1.nombre=random.choice([name[0],name[1]])
	if player1.nombre==name[0]:
		player2.nombre = name[1]#input("Por favor ingrese nombre del jugador 2: ")
	else:
		player2.nombre=name[0]	
	print(player1.nombre,player2.nombre)	
	assert(len(player1.nombre)>0 and len(player2.nombre)>0)