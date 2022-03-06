contador = 0
numeros = []
for i in range(20):
    numero = int(input('Ingrese un numero: '))
    numeros.append(numero);
    if numero<0:
        contador += 1
print(f'Fueron ingresados {contador} numeros negativos.')
