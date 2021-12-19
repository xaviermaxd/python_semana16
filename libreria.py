from tabulate import tabulate

empleados = []


def registrar_nuevo_empleado(nombre, apellido, sueldo_hora, horas_trabajadas, tipo):
    # debo agregar el emeplado a arreglo
    empleados.append({
        "nombre": nombre,
        "apellido": apellido,
        "sueldo_hora": sueldo_hora,
        "horas_trabajadas": horas_trabajadas,
        "tipo": tipo
    })
    return empleados


def reporte():
    contador = 0
    contador_a = 0
    contador_b = 0
    sum_sueldo = 0
    for emplado in empleados:
        # Sueldo total = sueldo_hora * horas_trabajadas
        sueldo_total = emplado["sueldo_hora"] * emplado["horas_trabajadas"]

        if sueldo_total > 1000:
            # calcular los impuestos
            sueldo_total = sueldo_total - (sueldo_total * 0.10)

            if (emplado["tipo"] == "B"):
                sueldo_total = sueldo_total - (sueldo_total * 0.12)

        empleados[contador]["sueldo_total"] = sueldo_total

        sum_sueldo += sueldo_total

        if emplado["tipo"] == "A":
            contador_a = contador_a + 1
        else:
            contador_b = contador_b + 1
        contador += 1

    print(tabulate(empleados, headers="keys", tablefmt="fancy_grid"))
    print("Sueldos totales: ", sum_sueldo)
    print("Contador Obreros", contador_a)
    print("Contador emplados", contador_b)
