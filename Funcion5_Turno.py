def Turno(esTurno,player1, player2):		#Funcion que intercambia los jugadores dependiendo el turno.
	assert( esTurno>=1 )								#Toma en cuenta que la var turno inicializa en 1.
	if esTurno%2!=0:									#Turnos impares
		jugador = player1
	elif esTurno%2==0:								#Turnos pares
		jugador = player2
	print("Es el Turno: ",esTurno)
	print("Turno del jugador ",jugador.nombre)
	assert( jugador == player1 or jugador == player2 )
	return jugador