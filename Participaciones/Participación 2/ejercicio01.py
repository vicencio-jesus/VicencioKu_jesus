#Jesus Jonas Vicencio Ku
#Ejercicio 1. El semáforo Pide al usuario el color de un semáforo y muestra la acción que debe realizar el conductor. El programa debe aceptar el color con mayúsculas o minúsculas, es decir, «Rojo», «rojo» y «ROJO» son el mismo caso. rojo: Alto total ,amarillo: Precaución, disminuye la velocidad , verde: Puedes avanzar cualquier otro valor: Color no válido

color=input("Ingresa el color del semaforo (Rojo/Amarillo/Verde): ").strip().lower()

if (color=="verde"):
    print("Puedes avanzar")
elif (color=="rojo"):
    print("Alto total")
elif(color=="amarillo"):
    print("Precaución,disminuye la velocidad")
else:
    print("Color no válido")



#strip().lower() # Con la función strip eliminamos todos los espacios en blanco, y con lower convertimos la respuesta a minúsculas