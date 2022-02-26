
nivelAgua= int(input("Digite la cantidad de agua de la represa: "));
if(nivelAgua<=200):
    print(f"el nivel de agua es: ${nivelAgua}. No tengo agua");
elif(nivelAgua>=200 and nivelAgua <= 350):
    print(f"el nivel de agua es: ${nivelAgua}. Todo bien energia corriente");
else:
    print(f"el nivel de agua es: ${nivelAgua}. Estamos full");
