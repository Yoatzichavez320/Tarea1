#Modifique el algoritmo del problema anterior 
# para que cuente las veces que ha leído un número de teclado y escriba el resultado por pantalla.

def leer_numero():
    intentos = 0
    while True:
        try:
            numero = int(input("Introduce un número entero: "))
            intentos += 1
            if 0 < numero < 20:
                print("Número de intentos:", intentos)
                return numero
            else:
                print("El número debe estar en el rango (0, 20)")
        except ValueError:
            print("Por favor, introduce un número entero correcto")

numero_correcto = leer_numero() 
print("intentos:", numero_correcto) 


