
def imprimir(tablero:[int])->"void":				# Procedimiento el tablero separándolo por pisos
	
	print("")
	#print("   1  2  3  4  5  6  7  8")
	print("   0  1  2  3  4  5  6  7")
	for i in range(0,8):
		print(i,tablero[i],i)
	print("   0  1  2  3  4  5  6  7")	
	#print("   1  2  3  4  5  6  7  8")	
		
"""def letra1(numero:int)->str:
	if numero==0:
		var="A"
	elif numero==1:
		var="B"
	elif numero==2:
		var="C"
	elif numero==3:
		var="D"
	elif numero==4:
		var="E"
	elif numero==5:
		var="F"
	elif numero==6:
		var="G"
	elif numero==7:
		var="H"
	return var	"""


				