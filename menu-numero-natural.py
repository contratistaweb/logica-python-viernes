import math



opcion = 8
while opcion != 0 :
    print('Seleccione una opcion segun el siguiente menu\n0. Salir.\n1. Consultar si un numero es multiplo de 2.\n2. Raiz cuadrada de un numero.\n3. Sumar 100 al numero ingresado.\n4. Eleve a 2 el numero ingresado.')
    opcion = int(input('Ingrese la opcion seleccionada: '))
    if opcion==0:
        break
    elif opcion==1:
        numero = int(input('ingrese el numero a evaluar: '))
        print(f'### El {numero} {("si","no")[numero%2]} es multiplo de 2.\n\n')
    elif opcion==2:
        numero = int(input('ingrese un numero a consultar su raiz cuadrada: '))
        print(f'### La raiz cuadarada de {numero} es {math.sqrt(numero)}.\n\n')
    elif opcion==3:
        numero = int(input('Sumarle 100 a: '))
        print(f'### {numero} + 100 = {numero+100}.\n\n')
    elif opcion==4:
        numero = int(input('ingrese el numero a elevar al cuadrado: '))
        print(f'### {numero} elevado al cuadrado es igual a: {math.pow(numero, 2)}.\n\n')
    else:
        print('### ERROR: Por favor ingrese una opcion valida.\n')
