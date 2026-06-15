print("========= BOLETA DE VENTA =========")

IGV = 0.18

cliente = input("Ingrese el nombre del cliente: ")
producto = input("Ingrese el nombre del producto: ")

# Validación del precio
while True:
    try:
        precio = float(input("Ingrese el precio del producto: S/ "))
        if precio > 0:
            break
        print("Error: el precio debe ser mayor que 0.")
    except ValueError:
        print("Error: ingrese un número válido.")

# Validación de la cantidad
while True:
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad > 0:
            break
        print("Error: la cantidad debe ser mayor que 0.")
    except ValueError:
        print("Error: ingrese un número entero válido.")

subtotal = precio * cantidad
igv = subtotal * IGV
total = subtotal + igv

print("\n" + "=" * 35)
print("         BOLETA DE VENTA")
print("=" * 35)
print(f"Cliente         : {cliente}")
print(f"Producto         : {producto}")
print(f"Precio Unitario  : S/ {precio:.2f}")
print(f"Cantidad         : {cantidad}")
print("-" * 35)
print(f"Subtotal         : S/ {subtotal:.2f}")
print(f"IGV (18%)        : S/ {igv:.2f}")
print(f"TOTAL A PAGAR    : S/ {total:.2f}")
print("=" * 35)
print("Gracias por su compra")