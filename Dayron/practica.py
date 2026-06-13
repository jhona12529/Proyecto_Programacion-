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