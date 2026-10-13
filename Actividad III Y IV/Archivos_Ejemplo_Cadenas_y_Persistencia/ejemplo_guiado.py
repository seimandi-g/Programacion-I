"""Ejemplo resuelto independiente del reto. Solo biblioteca estándar."""
from pathlib import Path
BASE = Path(__file__).resolve().parent
SALIDA = BASE / "salidas_demo"
SALIDA.mkdir(exist_ok=True)
etiqueta = "  sensor_norte:23.5  "
nombre, valor = etiqueta.strip().split(":")
print(nombre.replace("_", " ").capitalize())
print(f"Valor: {float(valor):.1f}")
try:
    with (BASE / "datos" / "eventos.txt").open(encoding="utf-8") as entrada:
        with (SALIDA / "errores.txt").open("w", encoding="utf-8") as salida:
            total = 0
            for linea in entrada:
                if " ERROR " in linea:
                    salida.write(linea)
                    total += 1
    with (SALIDA / "ejecuciones.log").open("a", encoding="utf-8") as historial:
        historial.write(f"Errores detectados: {total}\n")
    print(f"Errores: {total}")
except FileNotFoundError as error:
    print(f"No se encontró la entrada: {error.filename}")
