def JugadaIzq(board,f,c,jug):
	EsValida=True
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0 :
		EsValida=False
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=0 and board[f][c]!=jug.j:
		
		while EsValida:
			if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==0:
				EsValida=False
			elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
				pass
			elif 0<=f<8 and 0<=c<8 and board[f][c]==jug.j:
				EsValida=True
				break
			c=c-1
	return EsValida		

def JugadaSup(board,f,c,jug):
	EsValida=True
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0 :
		EsValida=False
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=0 and board[f][c]!=jug.j:
		
		while EsValida:
			if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==0:
				EsValida=False
			elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
				pass
			elif 0<=f<8 and 0<=c<8 and board[f][c]==jug.j:
				EsValida=True
				break
			f=f-1
			
	return EsValida	

def JugadaDer(board,f,c,jug):
	EsValida=True
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0 :
		EsValida=False
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=0 and board[f][c]!=jug.j:
		
		while EsValida:
			if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==0:
				EsValida=False
			elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
				pass
			elif 0<=f<8 and 0<=c<8 and board[f][c]==jug.j:
				EsValida=True
				break
			c=c+1
	return EsValida		

def JugadaInf(board,f,c,jug):
	EsValida=True
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0 :
		EsValida=False
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=0 and board[f][c]!=jug.j:
		
		while EsValida:
			if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==0:
				EsValida=False
			elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
				pass
			elif 0<=f<8 and 0<=c<8 and board[f][c]==jug.j:
				EsValida=True
				break
			f=f+1
	return EsValida		

def JugadaDiaSupIzq(board,f,c,jug):
	EsValida=True
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0 :
		EsValida=False
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=0 and board[f][c]!=jug.j:
		
		while EsValida:
			if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==0:
				EsValida=False
			elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
				pass
			elif 0<=f<8 and 0<=c<8 and board[f][c]==jug.j:
				EsValida=True
				break
			f=f-1
			c=c-1
	return EsValida
			
def JugadaDiaSupDer(board,f,c,jug):
	EsValida=True
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0 :
		EsValida=False
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=0 and board[f][c]!=jug.j:
		
		while EsValida:
			if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==0:
				EsValida=False
			elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
				pass
			elif 0<=f<8 and 0<=c<8 and board[f][c]==jug.j:
				EsValida=True
				break
			f=f-1
			c=c+1
	return EsValida

def JugadaDiaInfIzq(board,f,c,jug):
	EsValida=True
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0 :
		EsValida=False
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=0 and board[f][c]!=jug.j:
		
		while EsValida:
			if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==0:
				EsValida=False
			elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
				pass
			elif 0<=f<8 and 0<=c<8 and board[f][c]==jug.j:
				EsValida=True
				break
			f=f+1
			c=c-1
	return EsValida		

def JugadaDiaInfDer(board,f,c,jug):
	EsValida=True
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0 :
		EsValida=False
	elif f>=0 and f<8 and c>=0 and c<8 and board[f][c]!=0 and board[f][c]!=jug.j:
		
		while EsValida:
			if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==0:
				EsValida=False
			elif 0<=f<8 and 0<c<8 and board[f][c]!=jug.j and board[f][c]!=0:
				pass
			elif 0<=f<8 and 0<=c<8 and board[f][c]==jug.j:
				EsValida=True
				break
			f=f+1
			c=c+1
	return EsValida	

def JugadaValida(tablero,cord1,cord2,player):
	valida=True
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]!=0:
		valida=False
	elif (cord1>=0 and cord1<8 and cord2>=0 and cord2<8 and tablero[cord1][cord2]==0):	
		if (JugadaIzq(tablero,cord1,cord2-1,player)
		or JugadaSup(tablero,cord1-1,cord2,player) 
		or JugadaDer(tablero,cord1,cord2+1,player)
		or JugadaInf(tablero,cord1+1,cord2,player)
		or JugadaDiaSupIzq(tablero,cord1-1,cord2-1,player)
		or JugadaDiaSupDer(tablero,cord1-1,cord2+1,player)
		or JugadaDiaInfIzq(tablero,cord1+1,cord2-1,player)
		or JugadaDiaInfDer(tablero,cord1+1,cord2+1,player)):
			pass
		else:
			valida=False
	return valida				