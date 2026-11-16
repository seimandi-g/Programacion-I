"""

Desafío 4: Implementación de Funciones map, filter, y reduce Propias

"""


def mi_map(funcion, lista):
    """Aplica una función a cada elemento y devuelve una nueva lista."""
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado


def mi_filter(funcion, lista):
    """Conserva los elementos que cumplen la condición recibida."""
    resultado = []
    for elemento in lista:
        if funcion(elemento):
            resultado.append(elemento)
    return resultado


def mi_reduce(funcion, lista, valor_inicial):
    """Acumula un resultado y lo devuelve en una lista según la consigna."""
    acumulador = valor_inicial
    for elemento in lista:
        # La función recibe el resultado anterior y el siguiente elemento.
        acumulador = funcion(acumulador, elemento)

    # reduce normalmente devuelve un valor; aquí se pide un iterable.
    return [acumulador]


def duplicar(numero):
    return numero * 2


def es_par(numero):
    return numero % 2 == 0


def sumar(acumulador, numero):
    return acumulador + numero


def main():
    numeros = [1, 2, 3, 4, 5]

    print("DESAFÍO IV: MAP, FILTER Y REDUCE PROPIOS")
    print("Lista original:", numeros)

    # Pasamos el nombre de la función sin paréntesis para usarla después.
    print("Map - duplicar cada número:", mi_map(duplicar, numeros))
    print("Filter - conservar los pares:", mi_filter(es_par, numeros))
    print("Reduce - sumar desde 0:", mi_reduce(sumar, numeros, 0))


if __name__ == "__main__":
    main()
