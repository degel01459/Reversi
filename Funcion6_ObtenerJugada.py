def  ObtenerJugada(x,y,z,N):		#Funcion pregunta al usuario las coordenadas de la jugada.
	try:
		z = int(input("Ingrese Piso: "))
		x = int(input("Ingrese Fila: "))
		y = int(input("Ingrese Columna: "))
		assert(0 <= x < N and 0 <= y < N and 0 <= z < N)
	except:
		while(0 > x or x >= N or 0 > y or y >= N or 0 > z or z >= N):
			print("Jugada Invalida: Fuera de limites")
			print("Intente Nuevamente")
			z = int(input("Ingrese Piso: "))
			x = int(input("Ingrese Fila: "))
			y = int(input("Ingrese Columna: "))
		return x,y,z
	return x,y,z