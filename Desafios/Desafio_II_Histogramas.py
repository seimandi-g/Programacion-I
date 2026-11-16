# Repetimos la captura hasta que todos los datos sean válidos.
"""
Desafío 2: Generador de Histograma.

"""
while True:
    try:
        # Convertimos la entrada a entero; si no es posible, ocurre un ValueError.
        ndatos = int(input("Cantidad de registros: "))

        # La cantidad de registros debe ser mayor que cero.
        if ndatos <= 0:
            raise ValueError

        # Capturamos las líneas y las guardamos en una lista.
        # Ejemplo de entrada: leones 3, tigres 5
        registros = [
            input("Concepto y cantidad: ")
            for _ in range(ndatos)
        ]

        # Validamos todos los datos antes de imprimir el histograma.
        for line in registros:
            # Separamos los elementos de cada línea mediante las comas.
            for item in line.split(','):
                # Separamos el concepto y la cantidad por espacios.
                # Si no hay exactamente dos partes, ocurre un ValueError.
                name, cant = item.split()

                # La cantidad debe ser un entero no negativo.
                # Cero es válido y genera una barra sin asteriscos.
                if int(cant) < 0:
                    raise ValueError

        # Salimos del ciclo cuando toda la captura es válida.
        break

    except ValueError:
        # Informamos del error y reiniciamos toda la captura.
        print(f"{'-' * 55}\nHistograma: Datos capturados\n{'-' * 55}")

# Imprimimos el encabezado: cada \n genera un salto de línea.
print(f"{'-' * 55}\nHistograma: Datos capturados\n{'-' * 55}")

# Recorremos los datos validados para generar las barras horizontales.
for line in registros:
    for item in line.split(','):
        name, cant = item.split()

        # Reservamos un mínimo de 8 caracteres para alinear el concepto.
        # Repetimos el asterisco tantas veces como indique la cantidad.
        print(f"{name:8} {'*' * int(cant)}")

# Imprimimos el separador de cierre.
print("-" * 55)