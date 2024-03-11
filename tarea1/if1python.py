#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales

numero1 = float(input("10"))
numero2 = float(input("10"))

if numero1 > numero2:
    print(f"{numero1} menor que {numero2}")
elif numero2 < numero1:
    print(f"{numero2} menor que {numero1}")
else:
    print("ambos numeros son iguales")    
