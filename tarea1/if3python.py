#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor No considerar el caso en que ambos números son iguales

numero1 = float(input("20"))
numero2 = float(input("30"))

if numero1 < numero2:
    print("numero1 menor que numero2")
elif numero2 < numero1:
    print("numero2 menor que numero1") 
else:
    print("ambos numeros no son iguales") 
