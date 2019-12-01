def jugadaizq(board,f,c,jug):
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif 0<=f<8 and 0<=c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		while c>0:
			if 0<=c<8 and board[f][c-1]==jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				board[f][c]=jug.j
				c=c+2
			elif board[f][c-1]!=jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				pass
			elif board[f][c]==0 or board[f][c]==jug.j:
				c=1	
			c=c-1
	return board

def jugadadiagizqsup(board,f,c,jug):
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif 0<=f<8 and 0<=c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		while f>0 and c>0:
			if board[f-1][c-1]==jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				board[f][c]=jug.j
				f=f+2
				c=c+2
			elif board[f-1][c-1]!=jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				pass
			elif board[f][c]==0 or board[f][c]==jug.j:
				f=0
			f=f-1
			c=c-1
	return board


def jugadasup(board,f,c,jug):
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif 0<=f<8 and 0<=c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		while f>0:
			if board[f-1][c]==jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				board[f][c]=jug.j
				f=f+2	
			elif board[f-1][c]!=jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				pass
			elif board[f][c]==0 or board[f][c]==jug.j:
				f=0
			f=f-1
	return board


def jugadadiagdersup(board,f,c,jug):
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif 0<=f<8 and 0<=c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		while f>0 and c<7:
			if board[f-1][c+1]==jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				board[f][c]=jug.j
				f=f+2
				c=c-2
			elif board[f-1][c+1]!=jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				pass
			elif board[f][c]==0 or board[f][c]==jug.j:
				f=1
			f=f-1
			c=c+1
	return board


def jugadader(board,f,c,jug):
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif board[f][c]!=jug.j and 0<=f<8 and 0<=c<8 and board[f][c]!=0:
		
		while c<7:
			if board[f][c+1]==jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				board[f][c]=jug.j
				c=c-2
			elif board[f][c+1]!=jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				pass
			elif board[f][c]==jug.j or board[f][c]==jug.j:
				c=7
			c=c+1
	return board

def jugadadiagderinf(board,f,c,jug):
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif 0<=f<8 and 0<=c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		while f<7 and c<7:
			if board[f+1][c+1]==jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				board[f][c]=jug.j
				f=f-2
				c=c-2
			elif board[f+1][c+1]!=jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				pass
			elif board[f][c]==0 or board[f][c]==jug.j:
				pass	
			f=f+1
			c=c+1
	return board

def jugadainf(board,f,c,jug):
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif 0<=f<8 and 0<=c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		while f<7:
			if board[f+1][c]==jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				board[f][c]=jug.j
				f=f-2
			elif board[f+1][c]!=jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				pass
			elif board[f][c]==0 or board[f][c]==jug.j:
				f=7
			f=f+1
	return board

def jugadadiagizqinf(board,f,c,jug):
	if f<0 or f>=8 or c<0 or c>=8 or board[f][c]==jug.j or board[f][c]==0:
		pass
	elif 0<=f<8 and 0<=c<8 and board[f][c]!=jug.j and board[f][c]!=0:
		while f<7 and c>0:
			if board[f+1][c-1]==jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				board[f][c]=jug.j
				f=f-2
				c=c+2
			elif board[f+1][c-1]!=jug.j and board[f][c]!=0 and board[f][c]!=jug.j:
				pass
			elif board[f][c]==0 or board[f][c]==jug.j:
				f=7	
			f=f+1
			c=c-1
	return board

def RealizarJugada(tablero,cord1,cord2,player):
	tablero[cord1][cord2]=player.j
	
	jugadaizq(tablero,cord1,cord2-1,player)
	jugadadiagizqsup(tablero,cord1-1,cord2-1,player)
	jugadasup(tablero,cord1-1,cord2,player)
	jugadadiagdersup(tablero,cord1-1,cord2+1,player)
	jugadader(tablero,cord1,cord2+1,player)
	jugadadiagderinf(tablero,cord1+1,cord2+1,player)
	jugadainf(tablero,cord1+1,cord2,player)
	jugadadiagizqinf(tablero,cord1+1,cord2-1,player)
	return tablero


"""def jugadaizq(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and tablero[cord1][cord2]!=0:
		jugadaizq(tablero,cord1,cord2-1,player,player1,player2,i,j)
		if 0<=cord1<8 and 0<cord2<8 and tablero[cord1][cord2-1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero"""

""""
def jugadadiagizqsup(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadadiagizqsup(tablero,cord1-1,cord2-1,player,player1,player2,i,j)
		if 0<cord1<8 and 0<cord2<8 and tablero[cord1-1][cord2-1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero
"""
"""
def jugadasup(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and tablero[cord1][cord2]!=0:
		jugadasup(tablero,cord1-1,cord2,player,player1,player2,i,j)
		if 0<cord1<8 and 0<=cord2<8 and tablero[cord1-1][cord2]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero 
""" 
"""
def jugadadiagdersup(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and tablero[cord1][cord2]!=0:
		jugadadiagdersup(tablero,cord1-1,cord2+1,player,player1,player2,i,j)
		if 0<cord1<8 and 0<=cord2<7 and tablero[cord1-1][cord2+1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero
""" 
"""
def jugadader(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and tablero[cord1][cord2]!=0:
		jugadader(tablero,cord1,cord2+1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1][cord2+1]==player.j:
			print(cord2)
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero
""" 
"""
def jugadadiagderinf(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and tablero[cord1][cord2]!=0:
		jugadadiagderinf(tablero,cord1+1,cord2+1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1+1][cord2+1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero
""" 

"""
def jugadainf(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and tablero[cord1][cord2]!=0:
		jugadainf(tablero,cord1+1,cord2,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<8 and tablero[cord1+1][cord2]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero
""" 
"""
def jugadadiagizqinf(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and tablero[cord1][cord2]!=0:
		jugadadiagizqinf(tablero,cord1+1,cord2-1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<cord2<8 and tablero[cord1+1][cord2-1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero
"""