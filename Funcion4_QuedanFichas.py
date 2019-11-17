def  QuedanFichas(fichas : int ) -> bool : 		#Funcion que verifica las fichas disponibles
	assert( 0<fichas<=60 )
	QuedanFichas=True
	print("Quedan: " + str(fichas) + " fichas")
	if (fichas > 0):
		print("realice una jugada")
		print("")
	else:
		QuedanFichas = False
	assert( QuedanFichas == True or QuedanFichas == False )
	return QuedanFichas
	