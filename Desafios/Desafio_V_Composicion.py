"""Desafío 5: Composición de Funciones """


def componer(funciones):
    """Devuelve una función que aplica, de izquierda a derecha, la lista recibida.

    Cada función debe recibir un argumento y devolver un valor que pueda usar
    la siguiente. Una lista vacía deja el valor original sin cambios.
    """
    # Creamos una función dentro de otra. Esta función recibirá el valor cuando la utilicemos.
    def funcion_compuesta(valor):
        resultado = valor

        # Recorremos las funciones igual que recorremos elementos de una lista.
        for funcion in funciones:
            # El resultado de una función será la entrada de la siguiente.
            resultado = funcion(resultado)

        # Este return entrega el valor final después de recorrer la lista.
        return resultado

    # Sin paréntesis: devolvemos la función para poder ejecutarla después.
    
    return funcion_compuesta


def sumar_tres(numero):
    return numero + 3


def duplicar(numero):
    return numero * 2


def elevar_al_cuadrado(numero):
    return numero ** 2


def main():
    # Guardamos los nombres sin paréntesis para no ejecutar las funciones aún.
    funciones = [sumar_tres, duplicar, elevar_al_cuadrado]
    operacion = componer(funciones)

    numero = 5
    print("Desafío 5: Composición de Funciones")
    print("Valor inicial:", numero)
    print("Orden: sumar 3, duplicar y elevar al cuadrado")
    print("Resultado:", operacion(numero))  # 5 -> 8 -> 16 -> 256


if __name__ == "__main__":
    main()
