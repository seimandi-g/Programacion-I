
import matplotlib.pyplot as plt

registros = [
    " T001 | ANA | ANA@EJEMPLO.ORG | Datos | 12 ",
    "T002|luis|luis@ejemplo.org|programacion|8",
    "T003|MARTA|marta.ejemplo.org|datos|16",
    "T004|pablo|pablo@ejemplo.org| DATOS |15",
    "T005|ELENA|elena@ejemplo.org|visualizacion|10",
    "T006|ivan|ivan@ejemplo.org|programacion|20",
    "T007|rosa|rosa@ejemplo.org|datos|abc",
    "T008|hugo|hugo@ejemplo.org|visualizacion|25",
    "T009|sara|sara@ejemplo.org|datos|18",
    "T010|omar|omar@ejemplo.org|programacion|-3",
    "T011|luz| |visualizacion|11",
    "T012|noe|noe@ejemplo.org|visualizacion|22"
]

# ACTIVIDAD 1. Una lista contiene elementos; cada texto contiene caracteres.
# Referencia: Python 7-9/8_listas.py y Lección 2/01.py.
copia = registros[:]
copia.append("PRUEBA")
copia.pop()
print("Cantidad original:", len(registros))
print("Primer registro:", registros[0])
print("Último registro:", registros[-1])
print("Tres primeros:", registros[:3])
print("Caracteres del primer registro:", len(registros[0]))
print("Elemento completo:", "T001" in registros)       # False
print("Texto dentro del registro:", "T001" in registros[0])  # True
ticket = "T001"
print(ticket[0], ticket[1:], ticket[-1], ticket[0:3])
# input() entrega texto. "20" < "8" es True: compara caracteres.
print("Comparación textual:", "20" < "8")
print("Comparación numérica:", int("20") < int("8"))

# ACTIVIDAD 2. Métodos específicos tomados del enunciado.
# No encontré strip/split/find/rfind/capitalize/dir en los ejercicios de cursos
# buscados. Esto NO afirma que estén ausentes de todos tus libros.
texto = "  Ciencia   de Datos  "
print("Solo extremos:", texto.strip())
print("También espacios internos:", " ".join(texto.split()))
correo = "ana@ejemplo.org"
posicion = correo.find("@")
print("Arroba y último punto:", posicion, correo.rfind("."))
print("Usuario:", correo[:posicion])
print("Dominio:", correo[posicion + 1:])
print("Búsqueda ausente:", correo.find("#"))
# -1 significa no encontrado; correo[-1] sería la última letra, no un error.
print("VISUALIZACION DATOS:", "visualizacion-datos".replace("-", " ").upper())
print("Cambia la sigla IA:", "IA APLICADA".capitalize())
print("Métodos disponibles:", dir(""))
# len(texto) es función; texto.lower() es método de una cadena.
# No usar title/capitalize en los nombres: cambiaría la escritura original.

# ACTIVIDADES 3 Y 4. Una función recibe datos y devuelve un resultado.
# def/return: Introducción/intro.py, líneas 15-27.
def limpiar_texto(texto):
    # Regla del enunciado: quita extremos y deja un espacio entre palabras.
    return " ".join(texto.strip().split())


def correo_basico(correo):
    # Adaptación del anexo: usamos for/if en lugar de all(...).
    if correo.count("@") != 1 or " " in correo:
        return False
    partes_correo = correo.split("@")
    usuario = partes_correo[0]
    dominio = partes_correo[1]
    if usuario == "" or "." not in dominio:
        return False
    for parte in dominio.split("."):
        if parte == "":
            return False
    return True


categorias = ["datos", "programacion", "visualizacion"]


def procesar_registro(linea):
    campos_originales = linea.split("|")
    if len(campos_originales) != 5:
        return None, "numero de campos"

    campos = []
    # for + append ya aparecen en tus cursos; evitamos una comprensión.
    for campo in campos_originales:
        campos.append(limpiar_texto(campo))

    ticket = campos[0].upper()
    nombre = campos[1]              # Conserva mayúsculas/minúsculas originales.
    correo = campos[2].lower()
    categoria = campos[3].lower()
    tiempo = campos[4]

    # Adaptación propia: validar dígitos con in y for, ya vistos en tus cursos.
    # Así no necesitamos introducir isascii() e isdigit() del anexo.
    if len(ticket) != 4:
        return None, "identificador"
    if ticket[0] != "T":
        return None, "identificador"
    for caracter in ticket[1:]:
        if caracter not in "0123456789":
            return None, "identificador"
    if nombre == "":
        return None, "nombre vacio"
    if not correo_basico(correo):
        return None, "correo"
    if categoria not in categorias:
        return None, "categoria"
    if tiempo == "":
        return None, "minutos vacios"
    for caracter in tiempo:
        if caracter not in "0123456789":
            return None, "minutos no enteros o negativos"
    # Solo convertimos después de comprobar que el texto contiene dígitos.
    minutos = int(tiempo)
    if minutos > 180:
        return None, "minutos fuera de rango"
    # Son dos resultados: lista aceptada y motivo vacío.
    # None significa que no existe una fila aceptada; no significa cero.
    return [ticket, nombre, correo, categoria, minutos], ""


def clasificar_tiempo(minutos):
    if minutos <= 15:
        return "en tiempo"
    return "fuera de tiempo"


aceptados = []
rechazados = []
for linea in registros:
    fila, motivo = procesar_registro(linea)  # Par de resultados exigido por el PDF.
    if fila is None:
        rechazados.append([linea, motivo])  # Guarda el texto original y la razón.
    else:
        aceptados.append(fila)

print("ACEPTADOS:", aceptados)
print("RECHAZADOS:", rechazados)

# ACTIVIDAD 5. Acumuladores: como Python Analisis/5_series.py, líneas 10-19.
total = len(registros)
cantidad_aceptados = len(aceptados)
print("Total:", total)
print("Aceptados:", cantidad_aceptados)
print("Rechazados:", len(rechazados))
if total > 0:
    porcentaje = cantidad_aceptados / total * 100
    print(f"Aceptación: {porcentaje:.2f}% (base: {total} registros)")
else:
    print("Aceptación: sin datos")

suma_minutos = 0
en_tiempo = 0
fuera_tiempo = 0
for fila in aceptados:
    suma_minutos = suma_minutos + fila[4]
    estado = clasificar_tiempo(fila[4])
    print(fila[0], estado)
    if estado == "en tiempo":
        en_tiempo = en_tiempo + 1
    else:
        fuera_tiempo = fuera_tiempo + 1

if cantidad_aceptados > 0:
    promedio = suma_minutos / cantidad_aceptados
    print(f"Promedio: {promedio:.2f} min (base: {cantidad_aceptados} aceptados)")
else:
    print("Promedio: sin datos")  # Cero minutos sería una medición distinta.
print("En tiempo / fuera de tiempo:", en_tiempo, fuera_tiempo)

conteos = []
for categoria in categorias:
    cantidad = 0
    for fila in aceptados:
        if fila[3] == categoria:
            cantidad = cantidad + 1
    conteos.append(cantidad)
print("Categorías:", categorias)
print("Conteos:", conteos)


def graficar_barras(etiquetas, valores, titulo, color):
    # Patrón de tu notebook 01.ipynb (celdas 8-9) y Aplicacion/main.py 130-148.
    plt.figure(figsize=(7, 4))
    plt.bar(etiquetas, valores, color=color)
    plt.title(titulo)
    plt.xlabel("Categoría")
    plt.ylabel("Solicitudes aceptadas")
    # Complementos para cumplir la entrega; no encontrados en esos ejemplos.
    plt.ylim(bottom=0)
    plt.tight_layout()
    plt.savefig("solicitudes_por_categoria.png", dpi=150)
    plt.show()


graficar_barras(categorias, conteos, "Solicitudes por categoría", "steelblue")

# PRUEBAS PEDIDAS: estas líneas adicionales no se agregan a registros.
# Mostrar True significa que el resultado coincide con lo esperado.
for minutos_prueba in [14, 15, 16]:
    print("Clasificación de prueba:", minutos_prueba, clasificar_tiempo(minutos_prueba))
casos = [
    ["T100|Ana|a@b.org|datos|0", True],
    ["T100|Ana|a@b.org|datos|180", True],
    ["T100|Ana|a@b.org|datos|181", False],
    ["T100|Ana|a@b.org|datos|-3", False],
    ["T100|Ana|a@b.org|datos|abc", False],
    ["T100|Ana|ana@@ejemplo.org|datos|10", False],
    ["T100|Ana|ana@ejemplo..org|datos|10", False],
    ["T100|Ana|a@b.org|datos", False],
    ["T100|Ana|a@b.org|otra|10", False],
    ["T100||a@b.org|datos|10", False],
    ["T١٠٠|Ana|a@b.org|datos|10", False]
]
for caso in casos:
    fila, motivo = procesar_registro(caso[0])
    coincide = (fila is not None) == caso[1]
    print("Prueba correcta:", coincide, "Motivo:", motivo)
