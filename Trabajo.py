Usuarios=[]
Contraseñas=[]
Roles=["Dueño", "Empleado"]

def Registro (Usuarios, Contraseñas, Roles):
    usuario = input("Ingrese su usuario: ")
    Usuarios.append(usuario.strip())
    contraseña = input("Ingrese su contraseña: ")
    Contraseñas.append(contraseña.strip())
    rol = input("Ingrese su rol: ")
    Roles.append(rol.strip())
    return Usuarios, Contraseñas, Roles
def inicio_sesion (Usuarios, Contraseñas, Roles):
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    rol = input("Ingrese su rol: ")
    for i in range(len(Usuarios)):
        if usuario == Usuarios[i] and contraseña == Contraseñas[i] and rol == Roles[i]:
            print("Inicio de sesión exitoso")
            print("Su rol es: ", Roles[i])
            return True
    print("Usuario o contraseña incorrectos")
    return False
while True:
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        Registro(Usuarios, Contraseñas, Roles)
    elif opcion == "2":
        inicio_sesion(Usuarios, Contraseñas, Roles)
    elif opcion == "3":
        break
    else:
        print("Opción no válida")