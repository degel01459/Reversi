def Turno(turno, jugador, jugador1, jugador2):		#Funcion que intercambia los jugadores dependiendo el turno.
	assert( 1<=turno<61 )								#Toma en cuenta que la var turno inicializa en 1.
	if turno%2!=0:									#Turnos impares
		jugador = jugador1
	elif turno%2==0:								#Turnos pares
		jugador = jugador2
	print("Es el Turno: ",turno)
	print("Turno del jugador ",jugador.nombre)
	assert( jugador == jugador1 or jugador == jugador2 )
	return jugador