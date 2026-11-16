from pathlib import Path

BASE = Path(__file__).resolve().parent


def contar_palabras():
    # Puedes escribir ejemplo, ejemplo.txt o una ruta completa al archivo.
    nombre = input("Nombre del archivo .txt o ruta completa: ").strip().strip('"')
    if nombre == "":
        print("Debes escribir el nombre de un archivo.")
        return

    ruta = Path(nombre)
    # suffix devuelve la extensión. Si no escribes extensión, agregamos .txt.
    if ruta.suffix == "":
        ruta = Path(str(ruta) + ".txt")
    elif ruta.suffix.lower() != ".txt":
        print("El archivo debe tener la extensión .txt.")
        return

    # Una ruta completa se conserva; un nombre se busca junto al script.
    ruta = BASE / ruta
    conteo = {}  # Clave: palabra. Valor: cantidad de veces que aparece.
    total = 0

    try:
        with ruta.open("r", encoding="utf-8-sig") as archivo:
            for linea in archivo:
                linea = linea.lower()  # Hola y hola cuentan como la misma palabra.
                # Cambiamos signos por espacios para separar hola,mundo.
                for signo in '.,;:!?¿¡()[]{}"«»“”‘’\'…—–-_/\\|@#$%&*+=<>^`~':
                    linea = linea.replace(signo, " ")

                palabras = linea.split()  # Separa por espacios y saltos de línea.
                for palabra in palabras:
                    if palabra in conteo:
                        conteo[palabra] += 1
                    else:
                        conteo[palabra] = 1
                    total += 1

        # stem devuelve el nombre sin extensión. La salida queda junto al original.
        salida = ruta.parent / (ruta.stem + "_estadisticas.txt")
        # El modo x crea un archivo nuevo y evita borrar resultados existentes.
        with salida.open("x", encoding="utf-8") as archivo:
            archivo.write(f"Total de palabras: {total}\n")
            archivo.write(f"Palabras diferentes: {len(conteo)}\n\n")
            archivo.write("Palabra\tOcurrencias\n")
            for palabra in conteo:
                archivo.write(f"{palabra}\t{conteo[palabra]}\n")

        print(f"Total de palabras: {total}")
        print(f"Estadísticas guardadas en: {salida}")
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")
    except FileExistsError:
        print("Ya existe el archivo de estadísticas. Renómbralo para guardar otro.")
    except UnicodeDecodeError:
        print("Guarda el archivo de entrada con codificación UTF-8 e inténtalo otra vez.")
    except OSError as error:
        print(f"No fue posible leer o guardar el archivo: {error}")


if __name__ == "__main__":
    contar_palabras()
