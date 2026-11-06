#Haz un programa que reciba la velocidad de un automovil y determina de fomra booleana(true o false) si ha excedido el limite permitido de 90km/h

km=int(input("Ingresa la velocidad del vehiculo en kilometros: "))

exceso_velocidad=(km>90)

print(f"¿Supero el limite de velocidad? {exceso_velocidad}")