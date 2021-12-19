def calcular_raices(a, b, c):
    x1 = (-b + ((b*b - 4 * a * c) ** 0.5)) / (2 * a)
    x2 = (-b - ((b*b - 4 * a * c) ** 0.5)) / (2 * a)
    return x1, x2


def guardar_archivo(raices):
    archivo = open("raices.txt", "w")
    archivo.write("Las raices son las siguientes:\n")
    archivo.write("x1 = " + str(raices[0]) + "\n")
    archivo.write("x2 = " + str(raices[1]) + "\n")
    archivo.close()


def leer_archivo():
    archivo = open("raices.txt", "r")
    print(archivo.read())
