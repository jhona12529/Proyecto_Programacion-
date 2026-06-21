import os
from config import ARCHIVO_USUARIOS, ARCHIVO_PRODUCTOS, ARCHIVO_VENTAS
from menu import menu_principal

if __name__ == "__main__":
    # Crear archivos si no existen
    for archivo in [ARCHIVO_USUARIOS, ARCHIVO_PRODUCTOS, ARCHIVO_VENTAS]:
        if not os.path.exists(archivo):
            open(archivo, "w").close()
    
    menu_principal()