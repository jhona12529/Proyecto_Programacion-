
def jefe():
    print("Hola Ingrese su usuario y contraseña")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == "admin" and contraseña == "admin123":
        print("Bienvenido jefe")
    else:
        print("Usuario o contraseña incorrectos")
def empleado():
    print("Hola ingrese su usuario y contraseña")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == "empleado" and contraseña == "empleado123":
        print("Bienvenido empleado")
    else:
        print("Usuario o contraseña incorrectos")
