#Jesus Jonas Vicencio Ku
#Ejercicio 4. Piedra, papel o tijera
#Dos jugadores escriben su jugada: piedra, papel o tijera. El programa indica quién gana el round. piedra vence a tijera , tijera vence a papel ,papel vence a piedra.Si ambos escriben lo mismo, el resultado es «Empate». Si alguna de las dos jugadas no es piedra, papel o tijera, muestra «Jugada no válida» antes de comparar. Al final imprime uno de estos mensajes: «Gana el jugador 1», «Gana el jugador 2», «Empate» o «Jugada no válida». Puedes normalizar lo que escriben los jugadores con lower().

jugador1 = input("Jugador 1 (piedra, papel o tijera): ").strip().lower()
jugador2 = input("Jugador 2 (piedra, papel o tijera): ").strip().lower()

if (jugador1 != "piedra" and jugador1 != "papel" and jugador1 != "tijera") or \
   (jugador2 != "piedra" and jugador2 != "papel" and jugador2 != "tijera"):
    print("Jugada no válida")
elif jugador1 == jugador2:
    print("Empate")
elif (jugador1 == "piedra" and jugador2 == "tijera") or \
     (jugador1 == "tijera" and jugador2 == "papel") or \
     (jugador1 == "papel" and jugador2 == "piedra"):
    print("Gana el jugador 1")
else:
    print("Gana el jugador 2")