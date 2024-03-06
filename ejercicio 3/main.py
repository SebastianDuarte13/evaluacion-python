import json

def guardar_productos(producto):
    with open('productos.json', 'w+') as file:
        json.dump(producto, file, indent=4)


def registro_productos():
    id=input('Ingresa el Id del producto: ')
    nombre=input('Ingrese el nombre del producto: ')
    valor_unitario =int(input('Ingresa el valor unitario: '))
    stock_minimo =int(input('Ingresa el stock minimo: '))
    stock_maximo= int(input('Ingresa el stock maximo: '))
    producto = {
        'id': id,
        'nombre': nombre,
        'valorUnitario': valor_unitario,
        'stockminimo': stock_minimo,
        'stockmaximo': stock_maximo
    }

    guardar_productos(producto)

def main():
    while True:
        print("""
            ************************** 
            * REGISTRO DE PRODUCTOS  *
            **************************
          """)
        print('1. Registrar un nuevo Producto')
        print('2. Salir')

        option = int(input('Digite una Opcion: '))

        if option == '1':
            registro_productos()
        elif option == '2':
            break
        else:
            print('Opcion Invalida.')

if __name__ == '__main__':
    main()