mesInput = input("digita un mes del año: ").lower()
print(f"El mes ingresado fue: {mesInput}")

if (
    mesInput == 'diciembre' or
    mesInput == 'enero' or
    mesInput == 'febrero'
    ):
    print(f'el mes de {mesInput} corresponde a invierno')
elif (
    mesInput == 'marzo' or
    mesInput == 'abril' or
    mesInput == 'mayo'
    ):
    print(f'el mes de {mesInput} corresponde a primavera')
elif (mesInput == 'junio' or
    mesInput == 'julio' or
    mesInput == 'agosto'
    ):
    print(f'el mes de {mesInput} corresponde a verano')
else:
    print(f'el mes de {mesInput} corresponde a otoño')
