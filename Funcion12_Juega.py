def jugadaizq(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadaizq(tablero,cord1,cord2-1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1][cord2-1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero

def jugadadiagizqsup(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadadiagizqsup(tablero,cord1-1,cord2-1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1-1][cord2-1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero

def jugadasup(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadasup(tablero,cord1-1,cord2,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1-1][cord2]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero

def jugadadiagdersup(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadadiagdersup(tablero,cord1-1,cord2+1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1-1][cord2+1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero

def jugadader(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadader(tablero,cord1,cord2+1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1][cord2+1]==player.j:
			print(cord2)
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero

def jugadadiagderinf(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadadiagderinf(tablero,cord1+1,cord2+1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1+1][cord2+1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero

def jugadainf(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadainf(tablero,cord1+1,cord2,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1+1][cord2]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero

def jugadadiagizqinf(tablero,cord1,cord2,player,player1,player2,i,j):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or tablero[cord1][cord2]==player.j:
		pass
	elif tablero[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8:
		jugadadiagizqinf(tablero,cord1+1,cord2-1,player,player1,player2,i,j)
		if 0<=cord1<7 and 0<=cord2<7 and tablero[cord1+1][cord2-1]==player.j:
			tablero[cord1][cord2]=player.j
		else:
			pass
	return tablero



def RealizarJugada(tablero,cord1,cord2,player,player1,player2):
	tablero[cord1][cord2]=player.j
	i=cord1
	j=cord2
	jugadaizq(tablero,cord1,cord2-1,player,player1,player2,i,j)
	jugadadiagizqsup(tablero,cord1-1,cord2-1,player,player1,player2,i,j)
	jugadasup(tablero,cord1-1,cord2,player,player1,player2,i,j)
	jugadadiagdersup(tablero,cord1-1,cord2+1,player,player1,player2,i,j)
	jugadader(tablero,cord1,cord2+1,player,player1,player2,i,j)
	jugadadiagderinf(tablero,cord1+1,cord2+1,player,player1,player2,i,j)
	jugadainf(tablero,cord1+1,cord2,player,player1,player2,i,j)
	jugadadiagizqinf(tablero,cord1+1,cord2-1,player,player1,player2,i,j)
	return tablero

