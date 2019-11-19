def jugadaizq(board,f,c,jug):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif 0<=f<8 and 0<=c<8 and board[f][c]!=jug.j:
		print("izq",f,c)
		jugadaizq(board,f,c-1,jug)
		if 0<=f<8 and 0<c<8 and board[f][c-1]==jug.j:
			EsValida=True
		elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
			EsValida=True
		else:
			pass
	return EsValida

def jugadadiagizqsup(board,f,c,jug):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		print("diagizqsup",f,c)
		jugadadiagizqsup(board,f-1,c-1,jug)
		if 0<f<8 and 0<c<8 and board[f-1][c-1]==jug.j:
			EsValida=True
		elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
			EsValida=True
		else:
			pass
	return EsValida

def jugadasup(board,f,c,jug):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		print("sup",f,c)
		jugadasup(board,f-1,c,jug)
		if 0<f<8 and 0<=c<8 and board[f-1][c]==jug.j:
			EsValida=True
		elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
			EsValida=True
		else:
			pass
	return EsValida

def jugadadiagdersup(board,f,c,jug):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		print("diagdersup",f,c)
		jugadadiagdersup(board,f-1,c+1,jug)
		if 0<f<8 and 0<=c<7 and board[f-1][c+1]==jug.j:
			EsValida=True
		elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
			EsValida=True
		else:
			pass
	return EsValida

def jugadader(board,f,c,jug):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		print("der",f,c)
		jugadader(board,f,c+1,jug)
		if 0<=f<8 and 0<=c<7 and board[f][c+1]==jug.j:
			EsValida=True
		elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
			EsValida=True
		else:
			pass
	return EsValida

def jugadadiagderinf(board,f,c,jug):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		print("diagderinf",f,c)
		jugadadiagderinf(board,f+1,c+1,jug)
		if 0<=f<7 and 0<=c<7 and board[f+1][c+1]==jug.j:
			EsValida=True
		elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
			EsValida=True
		else:
			pass
	return EsValida

def jugadainf(board,f,c,jug):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		print("inf",f,c)
		jugadainf(board,f+1,c,jug)
		if 0<=f<7 and 0<=c<8 and board[f+1][c]==jug.j:
			EsValida=True
		elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
			EsValida=True
		else:
			pass
	return EsValida

def jugadadiagizqinf(board,f,c,jug):
	EsValida=False
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8:
		print("diagizqinf",f,c)
		jugadadiagizqinf(board,f+1,c-1,jug)
		if 0<=f<7 and 0<c<8 and board[f+1][c-1]==jug.j:
			EsValida=True
		elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
			EsValida=True
		else:
			pass
	return EsValida

def JugadaValida(tablero,cord1,cord2,player):
	valida=True
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]!=0:
		valida=False
	elif (cord1>=0 and cord1<8 and cord2>=0 and cord2<8 and tablero[cord1][cord2]==0):	
		if (jugadaizq(tablero,cord1,cord2-1,player) or jugadadiagizqsup(tablero,cord1-1,cord2-1,player)
		or jugadasup(tablero,cord1-1,cord2,player) or jugadadiagdersup(tablero,cord1-1,cord2+1,player)
		or jugadader(tablero,cord1,cord2+1,player) or jugadadiagderinf(tablero,cord1+1,cord2+1,player)
		or jugadainf(tablero,cord1+1,cord2,player) or jugadadiagizqinf(tablero,cord1+1,cord2-1,player)):
			pass
		else:
			valida=False
	return valida				