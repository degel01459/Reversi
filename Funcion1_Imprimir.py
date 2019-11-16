def imprimir(reversi:[int],fichas:[int])->"void":				# Procedimiento el tablero separándolo por pisos
	print("Fichas disponibles: "+str(fichas))
	for i in reversi:
		print(i)