numero = 0
suma = 0
while numero>=0:
    numero = int(input('el primer numero: '))
    if numero < 0 :
        break
    else:
        suma += numero
        print(f"la suma de los numeros ingresados es:\n{suma}")
