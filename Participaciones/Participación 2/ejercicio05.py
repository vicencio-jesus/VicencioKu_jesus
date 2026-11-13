#Jesus Jonas Vicencio Ku
#Ejercicio 5. Acceso al sistema
#Un sistema escolar tiene registrado el usuario «alumno» con la contraseña «python2026». Pide ambos datos y muestra un mensaje según el caso. usuario y contraseña correctos: Bienvenido al sistema usuario correcto y contraseña distinta: Contraseña incorrecta usuario distinto: Usuario no encontrado Resuélvelo con condicionales anidados: primero comprueba el usuario y, solo si existe, comprueba la contraseña.

usuario = input("Ingresa el nombre de usuario: ").strip()

if usuario == "alumno":
    contrasena = input("Ingresa la contraseña: ")
    if contrasena == "python2026":
        print("Bienvenido al sistema")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")