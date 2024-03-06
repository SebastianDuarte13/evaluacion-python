import os, art, time

print("""
    ****************************
    *   CONVERTIDOR DE PESOS   *
    ****************************
    """)
print("1. Convertir de pesos a dólares")
print("2. Convertir de pesos a euros")
print("3. Convertir de euros a pesos")
print("4. Convertir de pesos a yenes")
res = (int(input("Ingrese una Opcion: ")))
while res < 1 or res > 5:
    res = (int(input("Opcion no Valida, intentelo nuevamente: ")))
if res == 1:
    pesos=(float(input("cuantos pesos tiene?")))
    operacion1= pesos *0.0003944
    print(f"{pesos} pesos equivalen a {operacion1} euros.")
elif res == 2:
    pesos = float(input("Ingrese la cantidad en pesos: "))
    operacion2=pesos * 0.0004279
    print(f"{pesos} pesos equivalen a {operacion2} euros.")
elif res == 3:
    euros = float(input("Ingrese la cantidad en euros: "))
    operacion3= euros*4279 
    print(f"{euros} euros equivalen a {operacion3} pesos.")
elif res == 4:
    pesos = float(input("Ingrese la cantidad en pesos: "))
    operacion4 = pesos*26.30 
    print(f"{pesos} pesos equivalen a {operacion4} yenes.")
elif res == '5':
    art.tprint('vuelva pronto') 
    time.sleep (3)
    os.sys('exit')
else:
    os.system('cls')
    print('opcion ingresada no valida porfavor ingrese una opcion valida')
    


    
    # else:
    #     print("Opción no válida.")