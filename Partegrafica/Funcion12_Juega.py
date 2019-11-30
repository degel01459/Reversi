def jugadaizq(array,cord1,cord2,player,player1,player2):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or array[cord1][cord2]==player.j:
		pass
	elif array[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and array[cord1][cord2]!=0:
		j=1
		while j<=cord2:
			if 0<=cord1<8 and 0<cord2<8 and array[cord1][j-1]==player.j and array[cord1][j]!=0:
				array[cord1][j]=player.j
			else:
				pass
			j=j+1
	return array

def jugadadiagizqsup(array,cord1,cord2,player,player1,player2):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or array[cord1][cord2]==player.j:
		pass
	elif array[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and array[cord1][cord2]!=0:
		i=1
		j=1
		while i<=cord1 and j<=cord2:
			if 0<cord1<8 and 0<cord2<8 and array[i-1][j-1]==player.j and array[i][j]!=0:
				array[i][j]=player.j
			else:
				pass
			i=i+1
			j=j+1
	return array


def jugadasup(array,cord1,cord2,player,player1,player2):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or array[cord1][cord2]==player.j:
		pass
	elif array[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and array[cord1][cord2]!=0:
		j=1
		while j<=cord1:
			if 0<cord1<8 and 0<cord2<8 and array[j-1][cord2]==player.j and array[j][cord2]!=0:
				array[j][cord2]=player.j
			else:
				pass
			j=j+1
	return array


def jugadadiagdersup(array,cord1,cord2,player,player1,player2):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or array[cord1][cord2]==player.j:
		pass
	elif array[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and array[cord1][cord2]!=0:
		i=1
		j=6
		while i<=cord1 and j>=cord2:
			if 0<cord1<8 and 0<=cord2<7 and array[i-1][j+1]==player.j and array[i][j]!=0:
				array[i][j]=player.j
			else:
				pass
			i=i+1
			j=j-1
	return array


def jugadader(array,cord1,cord2,player,player1,player2):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or array[cord1][cord2]==player.j:
		pass
	elif array[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and array[cord1][cord2]!=0:
		j=6
		while j>=cord2:
			if 0<=cord1<8 and 0<cord2<8 and array[cord1][j+1]==player.j and array[cord1][j]!=0:
				array[cord1][j]=player.j
			else:
				pass
			j=j-1
	return array

def jugadadiagderinf(array,cord1,cord2,player,player1,player2):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or array[cord1][cord2]==player.j:
		pass
	elif array[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and array[cord1][cord2]!=0:
		i=6
		j=6
		while i>=cord1 and j>=cord2:
			if 0<=cord1<7 and 0<cord2<7 and array[i+1][j+1]==player.j and array[i][j]!=0:
				array[i][j]=player.j
			else:
				pass
			i=i-1
			j=j-1
	return array

def jugadainf(array,cord1,cord2,player,player1,player2):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or array[cord1][cord2]==player.j:
		pass
	elif array[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and array[cord1][cord2]!=0:
		i=6
		while i>=cord2:
			if 0<=cord1<8 and 0<cord2<8 and array[i+1][cord2]==player.j and array[i][cord2]!=0:
				array[i][cord2]=player.j
			else:
				pass
			i=i-1
	return array

def jugadadiagizqinf(array,cord1,cord2,player,player1,player2):
	if cord1<0 or cord1>=8 or cord2<0 or cord2>=8 or array[cord1][cord2]==player.j:
		pass
	elif array[cord1][cord2]!=player.j and 0<=cord1<8 and 0<=cord2<8 and array[cord1][cord2]!=0:
		i=6
		j=1
		while i>=cord1 and j<=cord2:
			if 0<cord1<8 and 0<cord2<8 and array[i+1][j-1]==player.j and array[i][j]!=0:
				array[i][j]=player.j
			else:
				pass
			i=i-1
			j=j+1
	return array

def RealizarJugada(tablero,cord1,cord2,player,player1,player2):
	tablero[cord1][cord2]=player.j
	i=cord1
	j=cord2
	jugadaizq(tablero,cord1,cord2-1,player,player1,player2)
	jugadadiagizqsup(tablero,cord1-1,cord2-1,player,player1,player2)
	jugadasup(tablero,cord1-1,cord2,player,player1,player2)
	jugadadiagdersup(tablero,cord1-1,cord2+1,player,player1,player2)
	jugadader(tablero,cord1,cord2+1,player,player1,player2)
	jugadadiagderinf(tablero,cord1+1,cord2+1,player,player1,player2)
	jugadainf(tablero,cord1+1,cord2,player,player1,player2)
	jugadadiagizqinf(tablero,cord1+1,cord2-1,player,player1,player2)
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