def  ObtenerJugada(cord1,cord2):		#Funcion pregunta al usuario las coordenadas de la jugada.
	while True:
		try:
			cord1 = int(input("Ingrese Fila: "))
			cord2 = int(input("Ingrese Columna: "))
			assert(0 <= cord1 < 8 and 0 <= cord2 < 8 )
			break
		except:
			print("Jugada Invalida: Fuera de limites")
			print("Intente Nuevamente")
			print("")
	return cord1,cord2			
	