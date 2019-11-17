def  QuieresJugar() -> str: 					# Función que preguntar al usuario si quiere comenzar el juego
	while True:
		try: # try/except
			print("")
			print("Quieres comenzar el juego :")
			print("Indique (SI) o (NO) en mayúscula")
			Jugar = str(input("Coloca una opcion:"))
			assert( Jugar == "SI" or Jugar == "NO" )
			break
		except:
			print("El dato ingresado no es válido")
			print("Debe ingresar (SI) o (NO) en mayúscula")
			print("")
	return Jugar