import os
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
