def  QuedanFichas(fichas : int ) -> bool : 		#Funcion que verifica las fichas disponibles
	QuedanFichas=True
	print("Quedan " + str(fichas) + " fichas")
	if (fichas > 0):
		print("Se puede seguir jugando")
		QuedanFichas = True
	else:
		print("Se termina el juego porque no quedan fichas")
		QuedanFichas = False
	return QuedanFichas
	