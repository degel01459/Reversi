def  Resultado(tablero,jugador,jugador1,jugador2):	#Procedimiento indica resultados actuales y lo refleja en el tablero.
	print("")
	print("Total de fichas Negras de ",jugador1.nombre,": ",jugador1.fichas)
	print("Total de fichas Negras de ",jugador2.nombre,": ",jugador2.fichas)
	print("")
	for i in tablero:
		print(i)
	print("")

