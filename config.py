import os
from datetime import datetime

# Variables globales
sesion_activa = False
rol_actual = None
usuario_actual = None

# ARCHIVOS
ARCHIVO_USUARIOS = "usuarios.txt"
ARCHIVO_PRODUCTOS = "productos.txt"
ARCHIVO_VENTAS = "ventas.txt"