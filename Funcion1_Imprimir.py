def imprimir(tablero:[int],fichas:[int])->"void":				# Procedimiento el tablero separándolo por pisos
	print("Fichas disponibles: "+str(fichas))
	print("")
	for i in tablero:
		print(i)