def JugadaValida(tablero,cord1,cord2,jugador):
	EsValida=True
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]!=0:
		EsValida=False
	elif cord1>=0 and cord1<8 and cord2>=0 and cord2<8 and tablero[cord1][cord2]==0:
		if (tablero[cord1+1][cord2]==jugador.j or tablero[cord1-1][cord2]==jugador.j
		or tablero[cord1][cord2+1]==jugador.j or tablero[cord1][cord2-1]==jugador.j):
			pass
		else:
			EsValida=False	
	return EsValida	
