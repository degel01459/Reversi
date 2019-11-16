def  QuieresJugar() -> int: 					# Función que preguntar al usuario si quiere comenzar el juego
	try: # try/except
		print("Quieres comenzar el juego elige:")
		print("1 = Comenzar")
		print("0 = Exit")
		Jugar = int(input("Coloca una opcion:"))
		assert( Jugar == 1 or Jugar == 0 )
	except:
		assert( Jugar > 1 or Jugar < 0 )
		while Jugar > 1 or Jugar < 0:
			print("Opcion invalida intente nuevamente.")
			print("Quieres comenzar el juego elige:")
			print("1 = Comenzar")
			print("0 = Exit")
			Jugar = int(input("Coloca una opcion valida:"))
		assert( Jugar == 1 or Jugar == 0)
	assert( Jugar == 1 or Jugar == 0)
	return Jugar