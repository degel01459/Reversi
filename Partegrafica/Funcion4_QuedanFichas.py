def  QuedanFichas(fichas : int ) -> bool : 		#Funcion que verifica las fichas disponibles
	assert( 0<fichas<=60 )
	QuedanFichas=True
	if (fichas > 0):
		pass
	elif (fichas <= 0):
		QuedanFichas = False
	assert( QuedanFichas == True or QuedanFichas == False )
	return QuedanFichas
	