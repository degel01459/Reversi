def jugadaizq(board,f,c,jug,jug1,jug2):
	EsValida=False	
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		jugadaizq(board,f,c-1,jug,jug1,jug2,)
		if 0<f<7 and 0<c<7 and board[f][c-1]==jug.j:
			EsValida=True
		else:
			pass
	return EsValida

def jugadadiagizqsup(board,f,c,jug,jug1,jug2):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		jugadadiagizqsup(board,f-1,c-1,jug,jug1,jug2)
		if 0<f<7 and 0<c<7 and board[f-1][c-1]==jug.j:
			EsValida=True
		else:
			pass
	return EsValida

def jugadasup(board,f,c,jug,jug1,jug2):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		jugadasup(board,f-1,c,jug,jug1,jug2)
		if 0<f<7 and 0<c<7 and board[f-1][c]==jug.j:
			EsValida=True
		else:
			pass
	return EsValida

def jugadadiagdersup(board,f,c,jug,jug1,jug2):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		jugadadiagdersup(board,f-1,c+1,jug,jug1,jug2)
		if 0<f<7 and 0<c<7 and board[f-1][c+1]==jug.j:
			EsValida=True
		else:
			pass
	return EsValida

def jugadader(board,f,c,jug,jug1,jug2):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		jugadader(board,f,c+1,jug,jug1,jug2)
		if 0<f<7 and 0<c<7 and board[f][c+1]==jug.j:
			EsValida=True
		else:
			pass
	return EsValida

def jugadadiagderinf(board,f,c,jug,jug1,jug2):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		jugadadiagderinf(board,f+1,c+1,jug,jug1,jug2)
		if 0<f<7 and 0<c<7 and board[f+1][c+1]==jug.j:
			EsValida=True
		else:
			pass
	return EsValida

def jugadainf(board,f,c,jug,jug1,jug2):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		jugadainf(board,f+1,c,jug,jug1,jug2)
		if 0<f<7 and 0<c<7 and board[f+1][c]==jug.j:
			EsValida=True
		else:
			pass
	return EsValida

def jugadadiagizqinf(board,f,c,jug,jug1,jug2):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		jugadadiagizqinf(board,f+1,c-1,jug,jug1,jug2)
		if 0<f<7 and 0<c<7 and board[f+1][c-1]==jug.j:
			EsValida=True
		else:
			pass
	return EsValida

def JugadaValida(tablero,cord1,cord2,player,player1,player2):
	valida=True
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]!=0:
		EsValida=False
	elif (cord1>=0 and cord1<8 and cord2>=0 and cord2<8 and tablero[cord1][cord2]==0):	
		if (jugadaizq(tablero,cord1,cord2,player,player1,player2) or jugadadiagizqsup(tablero,cord1,cord2,player,player1,player2)
		or jugadasup(tablero,cord1,cord2,player,player1,player2) or jugadadiagdersup(tablero,cord1,cord2,player,player1,player2)
		or jugadader(tablero,cord1,cord2,player,player1,player2) or jugadadiagderinf(tablero,cord1,cord2,player,player1,player2)
		or jugadainf(tablero,cord1,cord2,player,player1,player2) or jugadadiagizqinf(tablero,cord1,cord2,player,player1,player2)):
			pass
		else:
			valida=False
	return valida				

	
"""if jugadaizq(tablero,cord1,cord2,player,player1,player2):
			pass
		elif jugadadiagizqsup(tablero,cord1,cord2,player,player1,player2):
			pass
		elif jugadasup(tablero,cord1,cord2,player,player1,player2):
			pass
		elif jugadadiagdersup(tablero,cord1,cord2,player,player1,player2):
			pass
		elif jugadader(tablero,cord1,cord2,player,player1,player2):
			pass
		elif jugadadiagderinf(tablero,cord1,cord2,player,player1,player2):
			pass
		elif jugadainf(tablero,cord1,cord2,player,player1,player2):
			pass
		elif jugadadiagizqinf(tablero,cord1,cord2,player,player1,player2):
			pass"""		

"""def JugadaValida(tablero,cord1,cord2,player,player1,player2):
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
	return EsValida"""
	
def Vecinos(board,f,c,jug):
	jugar=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		jugar=True
	return jugar	
