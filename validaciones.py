from datetime import datetime

def validar_credenciales(usuario, passw, rol):
    if not usuario or not passw or not rol:
        print("Todos los campos son obligatorios")
        return False
    if " " in usuario:
        print("El usuario no puede contener espacios")
        return False
    if rol.lower() not in ["dueño", "empleado"]:
        print("Rol debe ser Dueño o Empleado")
        return False
    return True

def validar_nombre(nombre):
    if not nombre:
        print("Nombre no puede estar vacío")
        return False
    if nombre.isnumeric():
        print("Nombre no puede ser solo números")
        return False
    if "|" in nombre:
        print("Nombre no puede contener |")
        return False
    if "," in nombre:
        print("Nombre no puede contener comas")
        return False
    return True

def validar_precio(precio_str):
    try:
        precio = float(precio_str)
        if precio <= 0:
            print("El precio debe ser mayor que 0")
            return False
        if precio > 999999999999:
            print("Precio excede el límite permitido (999,999,999,999)")
            return False
        if precio < 0.00000001 and precio > 0:
            print("El precio mínimo es 0.00000001")
            return False
        return True
    except ValueError:
        print("Precio no válido")
        return False

def validar_cantidad(cant_str):
    try:
        cant = int(cant_str)
        if cant <= 0:
            print("La cantidad debe ser mayor que 0")
            return False
        if cant > 9999999999:
            print("Cantidad excede el límite permitido (9,999,999,999)")
            return False
        return True
    except ValueError:
        print("Cantidad no válida")
        return False

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        return True
    except:
        return False