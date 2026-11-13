# Base de datos simulada en una lista de diccionarios
registro_usuarios = [
    {
        "id": "10112345",
        "nombre": "Ana Gómez",
        "edad": 28,
        "telefono": "+57 300 123 4567",
        "estado": "Activo"
    },
    {
        "id": "10223456",
        "nombre": "Carlos Pérez",
        "edad": 35,
        "telefono": "+57 311 987 6543",
        "estado": "Inactivo"
    },
    {
        "id": "10334567",
        "nombre": "Luisa Martínez",
        "edad": 22,
        "telefono": "+57 322 555 0199",
        "estado": "Activo"
    }
]

print("========================================")
print("   SISTEMA DE REGISTRO DE PERSONAS     ")
print("========================================\n")

# Recorremos la lista para mostrar la información de cada persona
for usuario in registro_usuarios:
    print(f"ID/Documento: {usuario['id']}")
    print(f"Nombre Completo: {usuario['nombre']}")
    print(f"Edad: {usuario['edad']} años")
    print(f"Contacto: {usuario['telefono']}")
    print(f"Estado en el sistema: {usuario['estado']}")
    print("-" * 40)

