print("========= BOLETA DE VENTA =========")

cliente = input("Ingrese el nombre del cliente: ")

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: S/ "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = precio * cantidad
igv = subtotal * 0.18
total = subtotal + igv

print("\n========= BOLETA =========")
print("Cliente:", cliente)
print("Producto:", producto)
print("Precio unitario: S/", precio)
print("Cantidad:", cantidad)
print("Subtotal: S/", round(subtotal))
print("IGV (18%): S/", round(igv))
print("Total a pagar: S/", round(total))
print("==========================")