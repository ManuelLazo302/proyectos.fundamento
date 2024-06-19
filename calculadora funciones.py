def calculadora(num1,num2,opc):
    match opc:
        case 1:
            return num1 + num2
        case 2:
            return num1 - num2
        case 3:
            return num1 * num2
        case 4:
            if num2==0:
                print("No puedes dividir por 0")
            else:
                return num1 / num2
def validar(numero_entrada):
    while True:
        try:
            numero=float(input(numero_entrada))
            return numero
        except ValueError:
            print("Error, Ingrese valores numericos")
opc=0
num1=validar("Ingrese el primer numero: ")
num2=validar("Ingrese el segundo numero: ")
while opc!=5:
    print("-------------Calculadora--------------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    opc=int(input("> "))
    print(calculadora(num1,num2,opc))