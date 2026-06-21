import os
from config import ARCHIVO_USUARIOS

def usuario_existe(usuario):
    if not os.path.exists(ARCHIVO_USUARIOS): 
        return False
    with open(ARCHIVO_USUARIOS, "r") as f:
        for linea in f:
            if linea.strip().split("|")[0].lower() == usuario.lower():
                return True
    return False

def guardar_usuario(usuario, passw, rol):
    with open(ARCHIVO_USUARIOS, "a") as f:
        f.write(f"{usuario}|{passw}|{rol}\n") 
    return True

def buscar_usuario(usuario, passw, rol):
    if not os.path.exists(ARCHIVO_USUARIOS):
        return None
    with open(ARCHIVO_USUARIOS, "r") as f:
        for linea in f:
            u, p, r = linea.strip().split("|")
            if u.lower() == usuario.lower() and p == passw and r.lower() == rol.lower():
                return {"usuario": u, "rol": r}
    return None