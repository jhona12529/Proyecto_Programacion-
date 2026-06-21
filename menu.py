from datetime import datetime
from config import sesion_activa, rol_actual, usuario_actual
from funciones_usuario import usuario_existe, guardar_usuario, buscar_usuario
from funciones_producto import generar_id, guardar_producto, obtener_productos, actualizar_stock
from funciones_venta import guardar_venta, obtener_ventas
from validaciones import *

def verificar_sesion():
    if not sesion_activa:
        print("Debe iniciar sesión primero")
        return False
    return True

def verificar_permisos(rol_requerido):
    global rol_actual
    if rol_actual.lower() != rol_requerido.lower():
        print(f"Se requiere rol {rol_requerido} para esta acción")
        return False
    return True

def crear_usuario():
    print("\n=== CREAR USUARIO ===")
    usuario = input("Usuario: ").strip()
    passw = input("Contraseña: ").strip()
    rol = input("Rol (Dueño/Empleado): ").strip()
    
    if not validar_credenciales(usuario, passw, rol):
        return
    if usuario_existe(usuario):
        print("Usuario ya existe")
        return
    
    guardar_usuario(usuario, passw, rol.title())
    print("Usuario creado exitosamente")

def iniciar_sesion():
    global sesion_activa, rol_actual, usuario_actual
    print("\n=== INICIAR SESIÓN ===")
    usuario = input("Usuario: ").strip()
    passw = input("Contraseña: ").strip()
    rol = input("Rol (Dueño/Empleado): ").strip()
    
    if not validar_credenciales(usuario, passw, rol):
        return
    
    resultado = buscar_usuario(usuario, passw, rol)
    if resultado:
        sesion_activa = True
        rol_actual = resultado["rol"]
        usuario_actual = resultado["usuario"]
        print(f"Bienvenido {usuario}")
    else:
        print("Credenciales incorrectas")

def cerrar_sesion():
    global sesion_activa, rol_actual, usuario_actual
    if sesion_activa:
        sesion_activa = False
        rol_actual = None
        usuario_actual = None
        print("Sesión cerrada")
    else:
        print("No hay sesión activa")

def agregar_producto():
    print("\n=== AGREGAR PRODUCTO ===")
    try:
        id_prod = generar_id()
        print(f"ID automático: {id_prod}")
        
        nombre = input("Nombre: ").strip()
        if not validar_nombre(nombre):
            return
        
        precio = input("Precio: ")
        if not validar_precio(precio):
            return
        
        cant = input("Cantidad: ")
        if not validar_cantidad(cant):
            return
        
        guardar_producto(id_prod, nombre, float(precio), int(cant))
        print("Producto agregado correctamente")
    except Exception as e:
        print(f"Error: {e}")

def ver_productos():
    print("\n=== LISTA DE PRODUCTOS ===")
    productos = obtener_productos()
    if not productos:
        print("No hay productos registrados")
        return
    
    print(f"{'ID':<5} {'Nombre':<20} {'Precio':<12} {'Cantidad':<10}")
    print("-" * 50)
    for p in productos:
        print(f"{p['id']:<5} {p['nombre']:<20} S/{p['precio']:<11.2f} {p['cantidad']:<10}")

def vender_producto():
    print("\n=== VENDER PRODUCTO ===")
    productos = obtener_productos()
    if not productos:
        print("No hay productos disponibles")
        return
    
    ver_productos()
    
    try:
        id_buscar = int(input("\nID del producto: "))
        producto = None
        for p in productos:
            if p["id"] == id_buscar:
                producto = p
                break
        
        if not producto:
            print("Producto no encontrado")
            return
        
        if producto["cantidad"] == 0:
            print("Producto sin stock disponible")
            return
        
        while True:
            try:
                cant_vender = int(input(f"Cantidad disponible: {producto['cantidad']}\nCantidad a vender: "))
                if cant_vender <= 0:
                    print("Cantidad debe ser mayor a 0")
                elif cant_vender > producto["cantidad"]:
                    print(f"Stock insuficiente. Disponible: {producto['cantidad']}")
                else:
                    break
            except ValueError:
                print("Ingrese un número válido")
        
        cliente = input("Nombre del cliente: ").strip()
        if not cliente:
            print("El nombre del cliente es obligatorio")
            return
        
        subtotal = producto["precio"] * cant_vender
        igv = subtotal * 0.18
        total = subtotal + igv
        
        print("\n" + "="*40)
        print("         BOLETA DE VENTA")
        print("="*40)
        print(f"Cliente     : {cliente}")
        print(f"Producto    : {producto['nombre']}")
        print(f"Precio unit.: S/ {producto['precio']:.2f}")
        print(f"Cantidad    : {cant_vender}")
        print("-"*40)
        print(f"Subtotal    : S/ {subtotal:.2f}")
        print(f"IGV (18%)   : S/ {igv:.2f}")
        print(f"TOTAL       : S/ {total:.2f}")
        print("="*40)
        print("¡Gracias por su compra!")
        
        nueva_cant = producto["cantidad"] - cant_vender
        actualizar_stock(id_buscar, nueva_cant)
        
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        guardar_venta(cliente, producto["nombre"], subtotal, igv, total, fecha)
        
    except ValueError:
        print("ID no válido")
    except Exception as e:
        print(f"Error: {e}")

def reporte_ventas():
    print("\n=== REPORTE DE VENTAS ===")
    ventas = obtener_ventas()
    if not ventas:
        print("No hay ventas registradas")
        return
    
    total_general = 0
    total_sin_igv = 0
    total_igv = 0
    productos_vendidos = {}
    
    fechas_validas = True
    for v in ventas:
        if not validar_fecha(v["fecha"]):
            print(f"Advertencia: Fecha no válida en venta: {v['fecha']}")
            fechas_validas = False
    
    for v in ventas:
        total_sin_igv += v["subtotal"]
        total_igv += v["igv"]
        total_general += v["total"]
        productos_vendidos[v["producto"]] = productos_vendidos.get(v["producto"], 0) + 1
    
    mas_vendido = max(productos_vendidos.items(), key=lambda x: x[1]) if productos_vendidos else ("Ninguno", 0)
    
    print(f"\n{'='*50}")
    print(f"Total de ventas        : {len(ventas)}")
    print(f"Producto más vendido   : {mas_vendido[0]} ({mas_vendido[1]} ventas)")
    print(f"Total sin IGV          : S/ {total_sin_igv:.2f}")
    print(f"Total IGV              : S/ {total_igv:.2f}")
    print(f"Total con IGV          : S/ {total_general:.2f}")
    print(f"{'='*50}")
    
    print("\nDETALLE DE VENTAS:")
    print("="*80)
    print(f"{'Cliente':<15} {'Producto':<20} {'Subtotal':<10} {'IGV':<10} {'Total':<10} {'Fecha':<15}")
    print("-"*80)
    for v in ventas:
        print(f"{v['cliente']:<15} {v['producto']:<20} S/{v['subtotal']:<9.2f} S/{v['igv']:<9.2f} S/{v['total']:<9.2f} {v['fecha']:<15}")
    print("="*80)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"reporte_{timestamp}.txt", "w") as f:
        f.write("="*50 + "\n")
        f.write("         REPORTE DE VENTAS\n")
        f.write("="*50 + "\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total ventas: {len(ventas)}\n")
        f.write(f"Producto más vendido: {mas_vendido[0]} ({mas_vendido[1]} ventas)\n")
        f.write(f"Total sin IGV: S/ {total_sin_igv:.2f}\n")
        f.write(f"Total IGV: S/ {total_igv:.2f}\n")
        f.write(f"Total con IGV: S/ {total_general:.2f}\n")
        f.write("="*50 + "\n")
    
    print(f"\nReporte exportado: reporte_{timestamp}.txt")

def menu_principal():
    global sesion_activa, rol_actual, usuario_actual
    
    while True:
        print("\n" + "="*50)
        print("    SISTEMA DE GESTIÓN DE TIENDA")
        print("="*50)
        if sesion_activa:
            print(f"Usuario: {usuario_actual} | Rol: {rol_actual}")
        else:
            print("Estado: No autenticado")
        print("-"*50)
        print("1. Crear usuario")
        print("2. Iniciar sesión")
        print("3. Cerrar sesión")
        print("4. Agregar producto")
        print("5. Ver productos")
        print("6. Vender producto")
        print("7. Reporte de ventas")
        print("8. Salir")
        print("="*50)
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            cerrar_sesion()
        elif opcion == "4":
            if verificar_sesion():
                agregar_producto()
        elif opcion == "5":
            if verificar_sesion():
                ver_productos()
        elif opcion == "6":
            if verificar_sesion():
                vender_producto()
        elif opcion == "7":
            if verificar_sesion():
                reporte_ventas()
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")