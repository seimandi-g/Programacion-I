"""Completa los TODO conforme a las reglas del documento Word."""
from pathlib import Path
from datetime import datetime
import json
BASE = Path(__file__).resolve().parent
ENTRADA = BASE / "datos" / "solicitudes.txt"
SALIDA = BASE / "salidas"

def normalizar_categoria(texto):
    # TODO: strip, lower, sustituir guiones/guiones bajos y unir palabras.
    limpia = texto.strip().lower()
    limpia=limpia.replace("-"," ").replace("_"," ")
    normalizada="_".join(limpia.split())
    return normalizada


def validar_campos(campos, ids_vistos):
    # TODO: regresar (registro_limpio, motivo).
    # Un rechazo devuelve (None, motivo); uno válido devuelve (registro, None).
    if len(campos) !=4: # Validamos cumpla con los 4 campos
        return None," Cantidad de campos distinta a cuatro"
    for campo in campos: # For : para revisar los campos 
        if campo.strip() =="": # Comprueba si quedo alguna cadena vacia
            return None,"Campo vacío" # Termina la funcion al encontrar el primer error
    id_limpio=campos[0].strip().upper() # Campo 0 obtiene el id por pocision en la tabla, strip()quita espacios extremos y convierte a mayusculas
    if len(id_limpio) !=8 or not id_limpio.startswith("SOL-"): #Definimos 8 caracteres y prefijo SOL-
        return None, "ID con formato inválido"
    for caracter in id_limpio[4:]:#Obtiene los que viene despues de los caracteres del prefijo
                if caracter not in "0123456789": # El ciclo For es para validar que los caracteres esten entre 0 y 9
                    return None,"ID con formato inválido"
        

                
    correo_limpio=campos[1].strip().lower()
    if correo_limpio.count("@")!=1: # Contar que no sea mas de @
            return None,"Correo inválido"
    usuario,dominio=correo_limpio.split("@") # Se hace el split con el @

    if usuario=="" or dominio=="":
            return None,"Correo inválido" #Validar que correo y dominio despues del split sean diferentes a ""
    if " " in correo_limpio:#No haya espacios
            return None,"Correo inválido"
    if "." not in dominio or dominio.startswith(".") or dominio.endswith("."):#no inicie el dominio con punto termine con punto
            return None,"Correo inválido"

    categoria_limpia = normalizar_categoria(campos[2])

    categorias_permitidas={
            "acceso",
            "pago_en_línea",
            "soporte_técnico"
        }

    if categoria_limpia not in categorias_permitidas:
            return None, "Categoría fuera del catálogo"
    if id_limpio in ids_vistos:
                return None, "ID duplicado"
                # ids_vistos: contieneIDs de solicitudes ya aceptadas
                # id_limpio: para comparar despues de quitar espacios y convertir a mayúsculas

       
    descripcion_limpia = " ".join(campos[3].split())

    registro_limpio = [
        id_limpio,
        correo_limpio,
        categoria_limpia,
        descripcion_limpia
    ]

    return registro_limpio, None

def main():
    # TODO: crear SALIDA; abrir entrada con with y encoding='utf-8'.
    # TODO: verificar encabezado; iterar con número de línea; contar vacías.
    # TODO: validar sin modificar el archivo fuente y escribir rechazos.
    # TODO: producir solicitudes_limpias.txt, resumen.json y ejecuciones.log.
    # TODO: reabrir salidas, verificar conteos y capturar FileNotFoundError.

    try:
        with ENTRADA.open("r", encoding="utf-8") as archivo:
            encabezado = archivo.readline().rstrip("\n")

            if encabezado != "id|correo|categoria|descripcion":
                print("Encabezado incorrecto. Se detuvo el proceso.")
                return

            print("Encabezado correcto.")
            total = 0
            validos= 0
            rechazados= 0
            ids_vistos=set()
            por_categoria = {
                "acceso": 0,
                "pago_en_línea": 0,
                "soporte_técnico": 0
            }

            SALIDA.mkdir(exist_ok=True)
            with (
                (SALIDA / "solicitudes_limpias.txt").open(
                    "w", encoding="utf-8"
                ) as salida_limpias,
                (SALIDA / "rechazos.jsonl").open(
                    "w", encoding="utf-8"
                ) as salida_rechazos
            ):
                salida_limpias.write(encabezado + "\n")
                

                for numero_linea, linea in enumerate(archivo, start=2):#empezara a numerar a partir del 2, despues del encabezado
                    total += 1 #Cuenta las lineas
                    texto_original = linea.rstrip("\n") #Elimina el salto final

                    if texto_original.strip() =="":
                        registro=None
                        motivo="Línea Vacía"
                    else:
                        campos=texto_original.split("|")
                        registro,motivo,=validar_campos(campos, ids_vistos)

                    if registro is None:
                        rechazados +=1
                        print("RECHAZO",numero_linea,motivo)

                        rechazo = {
                            "linea": numero_linea,
                            "motivo": motivo,
                            "texto_original": texto_original
                        }

                        salida_rechazos.write(
                            json.dumps(rechazo, ensure_ascii=False) + "\n"
                        )                       







                    else:
                        validos +=1
                        ids_vistos.add(registro[0])
                        por_categoria[registro[2]] += 1
                        salida_limpias.write("|".join(registro) + "\n")




            print("Total:", total)
            print("Válidos:", validos)
            print("Rechazados:", rechazados)
            print("Por categoría:", por_categoria)
            print("Control total:", total == validos + rechazados)
            print("Control categorías:", sum(por_categoria.values()) == validos)

            resumen = {
                "total": total,
                "validos": validos,
                "rechazados": rechazados,
                "por_categoria": por_categoria
            }

            with (SALIDA / "resumen.json").open(
                "w", encoding="utf-8"
            ) as salida_resumen:
                json.dump(
                    resumen,
                    salida_resumen,
                    ensure_ascii=False,
                    indent=2
                )
            with (SALIDA / "resumen.json").open(
                "r", encoding="utf-8"
            ) as entrada_resumen:
                resumen_guardado = json.load(entrada_resumen)

            if resumen_guardado != resumen:
                raise ValueError("El resumen guardado no coincide con los conteos")

            print("Resumen guardado verificado.")

            with (SALIDA / "solicitudes_limpias.txt").open(
                "r", encoding="utf-8"
            ) as entrada_limpias:
                cabecera_guardada = entrada_limpias.readline().rstrip("\n")

                if cabecera_guardada != encabezado:
                    raise ValueError("La cabecera guardada no coincide")

                validos_guardados = 0

                for linea in entrada_limpias:
                    validos_guardados += 1

            if validos_guardados != validos:
                raise ValueError("El conteo de registros guardados no coincide")

            print("Registros limpios verificados:", validos_guardados)

            rechazados_guardados = 0

            with (SALIDA / "rechazos.jsonl").open(
                "r", encoding="utf-8"
            ) as entrada_rechazos:
                for linea in entrada_rechazos:
                    rechazo_guardado = json.loads(linea)

                    if not isinstance(rechazo_guardado, dict):
                        raise ValueError("El rechazo debe ser un objeto JSON")

                    if set(rechazo_guardado) != {
                        "linea", "motivo", "texto_original"
                    }:
                        raise ValueError(
                            "El rechazo no contiene los campos requeridos"
                        )

                    rechazados_guardados += 1

            if rechazados_guardados != rechazados:
                raise ValueError(
                    "El conteo de rechazos guardados no coincide"
                )

            print("Rechazos verificados:", rechazados_guardados)
            fecha_hora = datetime.now().isoformat(timespec="seconds")

            with (SALIDA / "ejecuciones.log").open(
                "a", encoding="utf-8"
            ) as historial:
                historial.write(
                    f"{fecha_hora} | entrada={ENTRADA.name} | "
                    f"total={total} | validos={validos} | "
                    f"rechazados={rechazados}\n"
                )

            print("Ejecución registrada en el historial.")

    except FileNotFoundError as error:
        print(f"No se encontró el archivo: {error.filename}")


    

if __name__ == "__main__":
    main()
