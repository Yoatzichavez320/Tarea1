#Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos

numero1 = 50  
numero2 = 50
numero3 = 28

if numero1 == numero2 == numero3:
    print("Los tres números son iguales")

elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Hay dos números iguales")

else:
    print("Los tres números son distintos") 
