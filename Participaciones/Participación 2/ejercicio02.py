#Jesus Jonas Vicencio Ku
#Ejercicio 2. La pizzería Pide el tamaño de la pizza y la cantidad que desea el cliente. Los precios son: 1 = personal: $99 2 = mediana: $149 3 = familiar: $199 Si el tamaño no está entre 1 y 3, muestra «Tamaño no válido» y no calcules el total. Si el cliente lleva tres pizzas o más, aplica 10 % de descuento sobre el total. Muestra el total a pagar con dos decimales.
print("Familiar $199")
print("Mediana $149")
print("Personal $99")
Tamano=input("¿Qué tamaño de pizza gusta? (Familiar/Mediana/Personal): ").strip().lower()
cantidad=int(input("¿Cuántas pizzas? "))

if (Tamano=="familiar"):
    precio_unitario =199
elif (Tamano == "mediana"):
    precio_unitario =149
elif (Tamano == "personal"):
    precio_unitario =99
else:
    print("Tamaño no válido")
    precio_unitario=0

subtotal=precio_unitario*cantidad

if ( cantidad>=3 and Tamano==("personal/mediana/familiar")) :
    total = subtotal * 0.90
    print(f"Se aplico 10% de descuento por llevar 3 pizzas o mas y su total es: {total:.2f}")
elif(cantidad==1 or cantidad==2):
    print(f"Tu total a pagar es: {subtotal:.2f}")
else:
    print("Vuelve a ingresar un tamaño de pizza valido")