habitaciones_libres = 50
habitaciones_ocupadas = 0

print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")

while True:
    print("===MENÚ PRINCIPAL===")
    print("1. Habitaciones Disponibles")
    print("2. Realizar Check-in")
    print("3. Realizar Check-out")
    print("4. Historial de Ocupaciones")
    print("5. Salir")
    opt = input("Seleccione un Opcion: ")

    if opt == "1":
        if habitaciones_libres > 0:
            print(f"Quedan {habitaciones_libres} Habitaciones Disponibles")
        elif habitaciones_libres == 0:
            print("Lo sentimos no quedan Habitaciones Disponibles")
    elif opt == "2":
        try:
            reserva = int(input("¿Cuantas Habitaciones desea Reservar?: "))
            if reserva <= 0:
                print("La cantidad de Reservas debe ser un numero superior a 0")
            elif reserva > habitaciones_libres:
                print("No hay suficientes Habitaciones")
            else:
                habitaciones_libres -= reserva
                habitaciones_ocupadas += reserva
                print("Check-int Realizado con Exito")
        except ValueError:
            print("Porfavor ingrese un valor numerico")
    elif opt == "3":
        try:
            retiro = int(input("¿Cuantas Reservas desea Cancelar?: "))
            if retiro <= 0:
                print("La cantidad de Reservas a Cancelar debe ser superior a 0")
            elif retiro > habitaciones_ocupadas:
                print("Esta intentando Cancelar mas Reservas de las que hay ahora mismo")
            else:
                habitaciones_libres += retiro
                habitaciones_ocupadas -= retiro
                print("Check-Out Realizado con Exito")
        except ValueError:
            print("Porfavor ingrese un valor numerico")
    elif opt == "4":
        print(F"El Total de Ocupaciones actuales es de {habitaciones_ocupadas}")
    elif opt == "5":
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break
    else:
        print("Ingrese un numero valido.")
    

