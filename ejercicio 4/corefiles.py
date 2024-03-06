from datetime import datetime
import json, os
import menus as m
hora_extra=5500
import json

def guardar_empreado(empleados_dict):
    with open('empleados.json', 'w+') as file:
        json.dump(empleados_dict, file, indent=4)

def revisar_empreado():
    with open('empleados.json', 'r') as rf:
        return json.load(rf)
    
def registrar_empreado():
    empleado_dict = revisar_empreado()  
    id_doc = input('Ingresa tu número de documento: ')  
    nombre = input('Ingrese su nombre: ')
    cargo = input('Ingresa su cargo (Almacenista, Jefe IT, Administrador, Mensajero, Gerente): ')  
    salario = input('Ingresa tu salario: ')
    empleado_dict[id_doc] = {  
        'nombre': nombre,
        'cargo': cargo,
        'salario': salario
    }
    guardar_empreado(empleado_dict)

def calcular_valor_pagar(empleado):
    horas_extra = empleado['horasExtras']
    valor_dia = empleado['valorDia']
    descuento_cafeteria = empleado['descuentoxCafeteria']
    cuota_prestamo = empleado['cuotaPrestamo']

    valor_horas_extra = horas_extra * HORA_EXTRA
    sueldo_base = empleado['salario'] * empleado['diasTrabajados']
    total_horas_extra = empleado['horasExtras'] * HORA_EXTRA
    total_a_pagar = sueldo_base + total_horas_extra - descuento_cafeteria - cuota_prestamo

    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    colilla_pago = {
        'mesPagado': fecha_actual,
        'fechaPago': fecha_actual,
        'sueldoBase': sueldo_base,
        'valorTotalHrasExtras': total_horas_extra,
        'cuotaPrestamo': cuota_prestamo,
        'descuentoxCafeteria': descuento_cafeteria,
        'totalAPagar': total_a_pagar
    }

    return colilla_pago



