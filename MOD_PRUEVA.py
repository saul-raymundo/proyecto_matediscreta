
def ingresar_conjunto(mensaje):
    while True:
        datos = input(mensaje)

        if datos.strip() == "":
            print("Por favor, ingrese los datos. Este campo no puede quedar vacío.")
            continue

        try:
            valores = datos.split(",")

            if any(valor.strip() == "" for valor in valores):
                print("Error: no deje espacios vacíos entre las comas.")
                continue

            for valor in valores:
                int(valor.strip())

            return datos

        except ValueError:
            print("Error: ingrese solamente números separados por comas.")
            print("Ejemplo: 1, 2, 3, 4")


def opreac_conjunt(conjunt1, opreacion, conjunt2):

    if opreacion == "union":
        conjunto_1 = set([int(x.strip()) for x in conjunt1.split(",")])
        conjunto_2 = set([int(x.strip()) for x in conjunt2.split(",")])

        union = conjunto_1 | conjunto_2
        return union

    elif opreacion == "interseccion":
        conjunto_i = set([int(x.strip()) for x in conjunt1.split(",")])
        conjunto_i2 = set([int(x.strip()) for x in conjunt2.split(",")])

        interseccion = conjunto_i & conjunto_i2
        return interseccion

    elif opreacion == "diferencia":
        conju_d1 = set([int(x.strip()) for x in conjunt1.split(",")])
        conj_d2 = set([int(x.strip()) for x in conjunt2.split(",")])

        diferencia = conju_d1 - conj_d2
        return diferencia

    elif opreacion == "complemento":
        conj_universal = set([int(x.strip()) for x in conjunt1.split(",")])
        conj_A = set([int(x.strip()) for x in conjunt2.split(",")])

        complemento = conj_universal - conj_A
        return complemento

    else:
        print("ERROR: operación no válida")
        return None


if __name__ == "__main__":

    print("PRUEBA DEL PROGRAMA")

    conjunto1 = ingresar_conjunto("Ingrese el conjunto 1: ")
    conjunto2 = ingresar_conjunto("Ingrese el conjunto 2: ")

    print("Unión:", opreac_conjunt(conjunto1, "union", conjunto2))
    print("Intersección:", opreac_conjunt(conjunto1, "interseccion", conjunto2))
    print("Diferencia:", opreac_conjunt(conjunto1, "diferencia", conjunto2))
    print("Complemento:", opreac_conjunt(conjunto1, "complemento", conjunto2))
