#Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es menor que 10.
# Si no lo está, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto. 
# Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto

def leer_numero():
    while True:
        try:
            numero = int(input("Introduce un número entero: "))
            if numero < 10:
                return numero
            else:
                print("El número debe ser menor que 10")
               
numero_correcto = leer_numero()
print("valor leido:", numero_correcto) 


