def  QuieresJugar() -> int: 					# Función que preguntar al usuario si quiere comenzar el juego
	while True:
		try: # try/except
			print("Quieres comenzar el juego elige:")
			print("1 = Comenzar")
			print("0 = Exit")
			Jugar = int(input("Coloca una opcion:"))
			assert( Jugar == 1 or Jugar == 0 )
			break
		except:
			print("Opcion invalida intente nuevamente.")
			print("Quieres comenzar el juego elige:")
					
	assert( Jugar == 1 or Jugar == 0)
	return Jugar