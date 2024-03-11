# Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados

n = 1 
suma = 0
while n != 0:
    n = int(input("ingresa un numero:"))
    suma += n 
print(f"la suma de los numeros es:{suma}") 
