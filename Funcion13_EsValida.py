def JugadaValida(tablero,cord1,cord2,player,player1,player2):
	EsValida=True
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]!=0:
		EsValida=False
	elif (cord1>=0 and cord1<8 and cord2>=0 and cord2<8 and tablero[cord1][cord2]==0):
		if Vecinos(tablero,cord1-1,cord2,player):
			pass
		elif Vecinos(tablero,cord1+1,cord2,player):
			pass
		elif Vecinos(tablero,cord1,cord2+1,player):
			pass
		elif Vecinos(tablero,cord1,cord2-1,player):
			pass
		elif Vecinos(tablero,cord1-1,cord2-1,player):
			pass
		elif Vecinos(tablero,cord1+1,cord2-1,player):
			pass
		elif Vecinos(tablero,cord1-1,cord2+1,player):
			pass
		elif Vecinos(tablero,cord1+1,cord2+1,player):	
			pass
		else:
			EsValida=False	 
	return EsValida
	
def Vecinos(board,f,c,jug):
	jugar=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		jugar=True
	return jugar	
