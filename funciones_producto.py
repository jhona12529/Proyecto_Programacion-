import os
from config import ARCHIVO_PRODUCTOS

def generar_id():
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        return 1
    max_id = 0
    with open(ARCHIVO_PRODUCTOS, "r") as f:
        for linea in f:
            try:
                id_act = int(linea.split("|")[0])
                if id_act > max_id:
                    max_id = id_act
            except:
                pass
    return max_id + 1

def guardar_producto(id_prod, nombre, precio, cant):
    with open(ARCHIVO_PRODUCTOS, "a") as f:
        f.write(f"{id_prod}|{nombre}|{precio}|{cant}\n")
    return True

def obtener_productos():
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        return []
    productos = []
    with open(ARCHIVO_PRODUCTOS, "r") as f:
        for linea in f:
            partes = linea.strip().split("|")
            if len(partes) == 4:
                id_prod, nombre, precio, cant = partes
                productos.append({
                    "id": int(id_prod),
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cant)
                })
    return productos

def actualizar_stock(id_prod, nueva_cant):
    productos = obtener_productos()
    with open(ARCHIVO_PRODUCTOS, "w") as f:
        for p in productos:
            if p["id"] == id_prod:
                f.write(f"{p['id']}|{p['nombre']}|{p['precio']}|{nueva_cant}\n")
            else:
                f.write(f"{p['id']}|{p['nombre']}|{p['precio']}|{p['cantidad']}\n")
    return True