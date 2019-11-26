
def LlenaCasilla(tablero,player):
	assert(all(all(0<=tablero[i][j]<3 for j in range(0,8)) for i in range(0,8)))
	contador=0
	
	for i in range(0,8):
		for j in range(0,8):
			if tablero[i][j]==player.j:

				contador=contador+1
			elif tablero[i][j]!=player:
				pass	
	assert(all(all(contador==sum(1 for k in range(0,64)) for j in range(0,8)) for i in range(0,8) if tablero[i][j]==player.j))		
		

	return contador
