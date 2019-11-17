def  ObtenerJugada(x,y):		#Funcion pregunta al usuario las coordenadas de la jugada.
	while True:
		try:
			x = int(input("Ingrese Fila: "))
			y = int(input("Ingrese Columna: "))
			assert(0 <= x < 8 and 0 <= y < 8 )
		except:
			print("Jugada Invalida: Fuera de limites")
			print("Intente Nuevamente")
			x = int(input("Ingrese Fila: "))
			y = int(input("Ingrese Columna: "))
		return x,y