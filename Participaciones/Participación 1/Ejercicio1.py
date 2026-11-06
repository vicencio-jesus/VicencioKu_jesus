#Diseña un programa que reciba una cantidad totral de dulces y un numero de niños. Debe calcular cuantos dulces le tocan a cada uno de forma equitatitva y cuantos dulces sobran en la caja

dulces=int(input("Ingresa el total de dulces: "))
ninos=int(input("Ingresa el numero de niños: "))

tocan=dulces//ninos
sobrante=dulces%tocan

print(f"La cantidad de dulces son {dulces} , la cantidad de niños son {ninos} a cada niño le toca {tocan} dulces y los dulces que quedan en la caja son {sobrante}")

