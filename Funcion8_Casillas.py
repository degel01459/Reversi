
def LlenaCasilla(A,player,player1,player2):
	x=1
	y=2
	i=0
	j=0
	contador=0
	z=[ 0 for k in range(1,3)]
	while x<=y:
		while i<8:
			while j<8:
				if x==A[i][j]:
					z[x]=contador+1

				j=j+1
			i=i+1
			j=0
		x=x+1
		contador=0
	print(z)	

	return z
	