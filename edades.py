#0 - 14 es niño
#15 - 28 es joven
#29 - 59 es adulto
#60 - ... es adulto mayor

edad = int(input('ingrese su edad: '))

if (edad > 0 and edad<15):
    print(f'usted es un niño de {edad} años')
elif (edad >= 15  and edad<28):
    print(f'usted es un joven de {edad} años')
elif (edad >= 0 and edad < 59):
    print(f'usted es un adulto de {edad} años')
elif(edad > 60):
    print(f'usted es un adulto mayor de {edad} años')
else:
    print(f'¿Seguro que ya nacio?')
