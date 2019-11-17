def RealizarJugada(tablero,cord1,cord2,player):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif cord1>=0 and cord1<8 and cord2>=0 and cord2<8 and tablero[cord1][cord2]!=0 and tablero[cord1][cord2]!=player.j:
		tablero[cord1][cord2]=player.j
		RealizarJugada(tablero,cord1-1,cord2,player)
		RealizarJugada(tablero,cord1+1,cord2,player)
		RealizarJugada(tablero,cord1,cord2-1,player)
		RealizarJugada(tablero,cord1,cord2+1,player)
		RealizarJugada(tablero,cord1+1,cord2+1,player)
		RealizarJugada(tablero,cord1+1,cord2-1,player)
		RealizarJugada(tablero,cord1-1,cord2+1,player)
		RealizarJugada(tablero,cord1-1,cord2-1,player)
	elif tablero[cord1][cord2]==0:
		tablero[cord1][cord2]=player.j	
	return tablero	


