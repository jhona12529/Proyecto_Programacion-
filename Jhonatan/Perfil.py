import os

Perfil = "Crear_perfil.txt"

def crear_usuarios():
    print("============================= HOLA BIENVENIDO A CREAR USUARIOS =============================")
    with open(Perfil, "a", encoding="utf-8") as file:
        Usuario = input("Ingrese su Usuario: \n")
        Contraseña = input("Crea una contraseña: \n")
        Rol = input("Ingrese su rol (Dueño / Empleado): \n")
        file.write(f"{Usuario}, {Contraseña}, {Rol}\n")
        print("Los perfiles fueron guardados exitosamente :)")
def Iniciar_sesion():
    print("============================= INICIO DE SESION =============================")
    Usuario_creado = input("Ingrese su Usuario: ")
    Contraseña_Creada = input("Ingrese su Contraseña: ")
    Rol_creado = input("Ingrese su rol (Dueño o empleado) : ")
    credenciales = f"{Usuario_creado}, {Contraseña_Creada}, {Rol_creado}"
    try:
        with open(Perfil, "r", encoding="utf-8") as file2:
            contenido = file2.read()
            if credenciales in contenido:
                print("Bienvenido")
                return True
            else:
                print("Error")
                return False
    except FileNotFoundError:
        print("No tiene usuarios registrados")
        return False