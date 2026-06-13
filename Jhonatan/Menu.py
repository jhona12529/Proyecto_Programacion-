
# Función principal para ejecutar el menú
from Jhonatan.Vender_Productos import sumar_los_precios_de_cada_producto_vendido, vender_producto
from Jhonatan.Perfil import crear_usuarios, Iniciar_sesion
from Jhonatan.Ver_productos import ver_productos
def menu_principal():
    while True:
        print("\n" + "=" * 50)
        print("         SISTEMA DE GESTIÓN DE TIENDA")
        print("=" * 50)
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Agregar producto")
        print("4. Agregar varios productos")
        print("5. Ver productos")
        print("6. Vender producto")
        print("7. Ver total de ventas")
        print("8. Salir")
        print("=" * 50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_usuarios()
        elif opcion == "2":
            if Iniciar_sesion():
                print("Sesión iniciada correctamente")
        elif opcion == "3":
            agregar_productos()
        elif opcion == "4":
            agregar_variosproductos()
        elif opcion == "5":
            ver_productos()
        elif opcion == "6":
            vender_producto()
        elif opcion == "7":
            sumar_los_precios_de_cada_producto_vendido()
        elif opcion == "8":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()