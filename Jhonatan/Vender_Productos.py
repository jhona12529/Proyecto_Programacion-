import os
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
