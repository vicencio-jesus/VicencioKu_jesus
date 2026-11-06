#Solicita un número entero y determina si es un multiplo simultaneo de 3 y 5 (Es decir, que al dividirlo entre ambas el residuo sea cero).

num=int(input("Ingresa un número que sea entero: "))

multiplo_simu=(num%3 ==0) and (num%5==0)

print(f"¿El numero es multiplo simultaneo de 3 y 5? {multiplo_simu}")