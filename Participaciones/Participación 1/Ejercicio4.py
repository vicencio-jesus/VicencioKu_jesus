#Pide al usuario la longitud de tres lados. Verifica si se puede formar un triangulo valido evalualo con operadores logicos, que la suma de cualquier par de lados sea mayor que el tercer lado

lado1=float(input("Ingresa la longitud del primer lado: "))
lado2=float(input("Ingresa la longitud del segundo lado: "))
lado3=float(input("Ingresa la longitud del tercer lado: "))

triangulo= (lado1+lado2>lado3) and (lado1+lado2>lado2) and (lado2+lado3>lado1)

print(f"¿Se puede formar un triangulo? {triangulo}")