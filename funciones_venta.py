import os
from config import ARCHIVO_VENTAS

def guardar_venta(cliente, producto, subtotal, igv, total, fecha):
    with open(ARCHIVO_VENTAS, "a") as f:
        f.write(f"{cliente}|{producto}|{subtotal}|{igv}|{total}|{fecha}\n")
    return True

def obtener_ventas():
    if not os.path.exists(ARCHIVO_VENTAS):
        return []
    ventas = []
    with open(ARCHIVO_VENTAS, "r") as f:
        for linea in f:
            partes = linea.strip().split("|")
            if len(partes) == 6:
                cliente, producto, subtotal, igv, total, fecha = partes
                try:
                    ventas.append({
                        "cliente": cliente,
                        "producto": producto,
                        "subtotal": float(subtotal),
                        "igv": float(igv),
                        "total": float(total),
                        "fecha": fecha
                    })
                except ValueError:
                    print(f"Advertencia: Datos corruptos en venta: {linea.strip()}")
                    continue
    return ventas