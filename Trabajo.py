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
def agregar_productos():
    print("============================= AGREGAR PRODUCTOS =============================")
    try:
        with open("Productos.txt", "a", encoding="utf-8") as file:
            id_producto = int(input("Ingrese el ID del producto: \n"))
            Producto = input("Ingrese el nombre del producto: \n")
            Precio = float(input("Ingrese el precio del producto: \n"))
            Cantidad = int(input("Ingrese la cantidad del producto: \n"))
            
            if id_producto < 0:
                print("El ID del producto no puede ser negativo.")
                return
            if Precio < 0:
                print("El precio del producto no puede ser negativo.")
                return
            if Cantidad < 0:
                print("La cantidad del producto no puede ser negativa.")
                return
            
            file.write(f"{id_producto}, {Producto}, {Precio}, {Cantidad}\n")
            print("Los productos fueron guardados exitosamente :)")
    except ValueError:
        print("Error: Por favor ingrese valores válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

def agregar_variosproductos():
    print("============================= AGREGAR VARIOS PRODUCTOS =============================")
    try:
        with open("Productos.txt", "a", encoding="utf-8") as file:
            cantidad_productos = int(input("¿Cuántos productos desea agregar? "))
            for i in range(cantidad_productos):
                print(f"\nProducto {i+1}:")
                id_producto = int(input("Ingrese el ID del producto: \n"))
                Producto = input("Ingrese el nombre del producto: \n")
                Precio = float(input("Ingrese el precio del producto: \n"))
                Cantidad = int(input("Ingrese la cantidad del producto: \n"))
                
                if id_producto < 0:
                    print("El ID del producto no puede ser negativo.")
                    continue
                if Precio < 0:
                    print("El precio del producto no puede ser negativo.")
                    continue
                if Cantidad < 0:
                    print("La cantidad del producto no puede ser negativa.")
                    continue
                
                file.write(f"{id_producto}, {Producto}, {Precio}, {Cantidad}\n")
                print(f"Producto {i+1} guardado exitosamente")
    except ValueError:
        print("Error: Por favor ingrese valores válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

def ver_productos():
    print("============================= VER PRODUCTOS =============================")
    try:
        with open("Productos.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()
            if not lineas:
                print("No hay productos registrados.")
                return
            
            print("\n" + "=" * 70)
            print(f"{'ID':<5} {'Producto':<20} {'Precio':<10} {'Cantidad':<10}")
            print("=" * 70)
            
            for linea in lineas:
                datos = linea.strip().split(', ')
                if len(datos) == 4:
                    id_producto, nombre, precio, cantidad = datos
                    print(f"{id_producto:<5} {nombre:<20} S/{precio:<9} {cantidad:<10}")
            print("=" * 70)
    except FileNotFoundError:
        print("No existen productos registrados.")

def vender_producto():
    print("============================= VENDER PRODUCTO =============================")
    try:
        # Leer productos actuales
        with open("Productos.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()
            
        if not lineas:
            print("No hay productos disponibles para vender.")
            return
        
        # Mostrar productos disponibles
        productos = []
        print("\n" + "=" * 70)
        print(f"{'ID':<5} {'Producto':<20} {'Precio':<10} {'Cantidad':<10}")
        print("=" * 70)
        
        for linea in lineas:
            datos = linea.strip().split(', ')
            if len(datos) == 4:
                id_producto, nombre, precio, cantidad = datos
                print(f"{id_producto:<5} {nombre:<20} S/{precio:<9} {cantidad:<10}")
                productos.append({
                    'id': id_producto,
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad),
                    'linea_original': linea
                })
        print("=" * 70)
        
        # Buscar producto por ID
        id_buscar = input("\nIngrese el ID del producto que desea vender: ")
        producto_encontrado = None
        
        for producto in productos:
            if producto['id'] == id_buscar:
                producto_encontrado = producto
                break
        
        if not producto_encontrado:
            print("Producto no encontrado")
            return
        
        # Validar cantidad a vender
        while True:
            try:
                cantidad_vendida = int(input(f"Cantidad disponible: {producto_encontrado['cantidad']}\nIngrese cantidad a vender: "))
                if cantidad_vendida <= 0:
                    print("La cantidad debe ser mayor a 0")
                elif cantidad_vendida > producto_encontrado['cantidad']:
                    print(f"No hay suficiente stock. Disponible: {producto_encontrado['cantidad']}")
                else:
                    break
            except ValueError:
                print("Ingrese un número válido")
        
        # Actualizar stock
        nueva_cantidad = producto_encontrado['cantidad'] - cantidad_vendida
        subtotal = producto_encontrado['precio'] * cantidad_vendida
        IGV = 0.18
        igv = subtotal * IGV
        total = subtotal + igv
        
        # Datos del cliente
        cliente = input("Ingrese el nombre del cliente: ")
        
        # Mostrar boleta
        print("\n" + "=" * 35)
        print("         BOLETA DE VENTA")
        print("=" * 35)
        print(f"Cliente         : {cliente}")
        print(f"Producto        : {producto_encontrado['nombre']}")
        print(f"Precio Unitario : S/ {producto_encontrado['precio']:.2f}")
        print(f"Cantidad        : {cantidad_vendida}")
        print("-" * 35)
        print(f"Subtotal        : S/ {subtotal:.2f}")
        print(f"IGV (18%)       : S/ {igv:.2f}")
        print(f"TOTAL A PAGAR   : S/ {total:.2f}")
        print("=" * 35)
        print("Gracias por su compra")
        
        # Actualizar archivo de productos
        with open("Productos.txt", "w", encoding="utf-8") as file:
            for producto in productos:
                if producto['id'] == id_buscar:
                    file.write(f"{producto['id']}, {producto['nombre']}, {producto['precio']}, {nueva_cantidad}\n")
                else:
                    file.write(producto['linea_original'])
        
        # Guardar en historial de ventas
        from datetime import datetime
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("historial.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{cliente},{producto_encontrado['nombre']},{total:.2f},{fecha}\n")
        
    except FileNotFoundError:
        print("No existen productos registrados.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def sumar_los_precios_de_cada_producto_vendido():
    print("============================= TOTAL DE VENTAS =============================")
    try:
        with open("historial.txt", "r", encoding="utf-8") as file:
            ventas = file.readlines()
            if not ventas:
                print("No hay ventas registradas.")
                return
            
            total_ventas = 0
            for venta in ventas:
                datos = venta.strip().split(',')
                if len(datos) >= 3:
                    monto = float(datos[2])
                    total_ventas += monto
            
            print(f"El total de ventas acumuladas es: S/ {total_ventas:.2f}")
    except FileNotFoundError:
        print("No hay historial de ventas aún.")
    except Exception as e:
        print(f"Error: {e}")

# Función principal para ejecutar el menú
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
