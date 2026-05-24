def menu():
    def selec():
        while True:
            print("*INGRESE OPCION*")
            print("Jefe")
            print("Empleado")
            opcion = input("Selecciona una opcion: ")
            if opcion == "1":
                print("aqui aparece el menu del jefe")
            elif opcion == "2":
                print("aqui aparece el menu del empleado")
            else:
                print("El opcion no existe")

def registro_stock():
    stock_nuevo = []
    
