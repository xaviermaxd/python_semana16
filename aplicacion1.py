import calculo

while True:
    print("Elige una opción del menu:")
    print("1) Registrar números")
    print("2) Imprimir raíces")
    print("3) Guardar archivo")
    print("4) Leer archivo")
    print("5) Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("***** Registrar números *****")
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        c = int(input("Ingrese el valor de c: "))
        print("************************")

    if opcion == "2":
        print("***** IMPRIMIR RAÍCES *****")
        raices = calculo.calcular_raices(a, b, c)
        print("Las raíces son: ", raices)
        print("************************")

    if opcion == "3":
        print("***** GUARDANDO ARCHIVO *****")
        calculo.guardar_archivo(raices)
        print("************************")

    if opcion == "4":
        print("***** LEER ARCHIVO *****")
        calculo.leer_archivo()
        print("************************")

    if opcion == "5":
        print("Saliendo...")
        break
