# Ciclo mientras

# variable controladora
import math



print("Contratista Web")
print("   ***   ***   ***   ")
print("0. Digita 0 para salir")
print("1. Digita 1 para calcular la raiz de un numero")
print("2. Digita 2 para calcular la potencia 2 de un numero")
print("3. Digita 3 para salit")
print("   ***   ***   ***   ")

opcion =  100

# declaro el bucle/ciclo/iteracion/repeticion/loop
while(opcion != 0):
    opcion =  int(input('Seleccione una opcion: '))
    print(f'seleccionaste la opcion {opcion}');
    if(opcion == 0 ):
        print(f'seleccionaste la opcion {opcion}... \nAdios');
        break
    elif(opcion == 1 ):
        numero = int(input('Digite un numero: '))
        print(f"La raiz de {numero} es {math.sqrt(numero)}")
    elif(opcion == 2 ):
        numero = int(input('Digite un numero: '))
        print(f"La raiz de {numero} es {math.pow(numero, 2)}")
    else:
        print('Error: la opcion que seleccionaste no existe... Pongale cuidado al menu :¬|');
    

