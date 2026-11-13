#Jesus Jonas Vicencio Ku
#Ejercicio 3. El año bisiesto
#Pide un año y determina si es bisiesto. Un año es bisiesto si es divisible entre 4, excepto los que terminan en 00: esos solo son bisiestos si además son divisibles entre 400. Muestra el resultado con el año incluido, por ejemplo «El año 2024 es bisiesto» o «El año 1900 no es bisiesto». Comprueba tu programa con 2024, 1900 y 2000.

anio=int(input("Ingresa el año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} no es bisiesto")