usuario = {}

usuario['id'] = input("Ingrese su ID: ")
usuario['nombres'] = input("Ingrese sus nombres: ")
usuario['apellidos'] = input("Ingrese sus apellidos: ")
usuario['ubicacion'] = input("Ingrese su ubicación: ")
usuario['direccion'] = input("Ingrese su dirección: ")
usuario['ciudad'] = input("Ingrese su ciudad: ")
usuario['longitud'] = input("Ingrese la longitud: ")
usuario['latitud'] = input("Ingrese la latitud: ")
usuario['email'] = input("Ingrese su email: ")
usuario['edad'] = input("Ingrese su edad: ")
usuario['ocupacion'] = input("Ingrese su ocupación: ")

# Imprimir la información del usuario almacenada en el diccionario
print("\nInformación del usuario:")
for key, value in usuario.items():
    print(f"{key}: {value}")

