#Modifique el algoritmo del problema anterior 
# para que, en vez de comprobar que el número sea menor que 10, compruebe que se encuentre en el rango (0, 20)

def leer_numero():
    while True:
        try:
            numero = int(input("Introduce un número entero: "))
            if 0 < numero < 20:
                return numero
            else:
                print("El número debe estar en el rango (0, 20)")
        except ValueError:
            print("introduce un número entero correcto.")
numero_correcto = leer_numero()
print("valor leido:", numero_correcto)  


