
def imprimir(tablero:[int])->"void":				# Procedimiento el tablero separándolo por pisos
	
	print("")
	print("   1  2  3  4  5  6  7  8")
	for i in range(0,8):
		print(letra1(i),tablero[i],letra2(i))
		
	print("   8  7  6  5  4  3  2  1")	
def letra1(numero:int)->str:
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
	return var	

def letra2(numero:int)->str:
	if numero==0:
		var="H"
	elif numero==1:
		var="G"
	elif numero==2:
		var="F"
	elif numero==3:
		var="E"
	elif numero==4:
		var="D"
	elif numero==5:
		var="C"
	elif numero==6:
		var="B"
	elif numero==7:
		var="A"
	return var	
				