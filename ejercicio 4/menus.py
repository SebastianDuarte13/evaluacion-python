import os,time, sys, art
import corefiles as cf
def menu_pr():
    print("MENU")
    print("1. AGREGAR EMPLEADO")
    print("2. CALCULAR VALOR A PAGAR POR EMPLEADO ")
    print("3. CONSULTAR COLILLA DE PAGO DEL EMPLEADO")
    print("4. TOTAL PAGADO POR CONCEPTO DE NOMINA")
    print("5. SALIR")
    op=input('seleccione un valor ')
    if op=='1':
        cf.guardar_empreado()
    elif op=='2':
        cf.calcular_valor_pagar()
    elif op=='3':
        id_empleado = input("Ingrese el ID del empleado: ")
        encontrado = False
        for empleado in empleados:
            if empleado['id'] == id_empleado:
                encontrado = True
                colilla_pago = cf.calcular_valor_pagar(empleado)
                print(f"Colilla de pago para {empleado['nombre']}:")
                print(colilla_pago)
        if not encontrado:
         print("Empleado no encontrado.")
        os.system("pause")
        os.system("cls")
    elif op=='4':
        total_nomina = sum(cf.calcular_valor_pagar(empleado)['totalAPagar'] for empleado in empleados)
        print(f"Total pagado por concepto de nómina: {total_nomina} pesos.")
        os.system("pause")
        os.system("cls")
    elif op=='5':
        art.tprint('vuelva pronto')
        time.sleep(3)
        sys.exit
    else:
        os.system('cls')
        print('opcion no valida ingrese otro valor')
        time.sleep(3)
        return menu_pr()