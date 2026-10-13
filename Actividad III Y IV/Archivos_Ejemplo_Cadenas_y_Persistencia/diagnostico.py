'''
Actividad Unidad III Y IV
Depuración de texto y persistencia de datos con Python

Proposito de la actividad 

Construyan un programa reproducible que transforme solicitudes de soporte almacenadas como texto en registros normalizados y verificables. Aplicarán las operaciones de cadenas y el manejo de archivos de las unidades 3 y 4 para justificar decisiones de calidad de datos antes de un análisis posterior.
Situación a resolver
Una mesa de ayuda recibe solicitudes con espacios, categorías escritas de distintas formas y registros incompletos. El equipo de Ciencia de Datos necesita conocer la distribución real de las solicitudes sin que las variaciones de escritura alteren los conteos. Su tarea consiste en conservar las entradas, separar rechazos y producir resultados que otra persona pueda revisar.

Situación a resolver
Una mesa de ayuda recibe solicitudes con espacios, categorías escritas de distintas formas y registros incompletos. El equipo de Ciencia de Datos necesita conocer la distribución real de las solicitudes sin que las variaciones de escritura alteren los conteos. Su tarea consiste en conservar las entradas, separar rechazos y producir resultados que otra persona pueda revisar.


'''
'''
=============================================================================================

Etapa Uno


==============================================================================================
'''
from pathlib import Path


#1.1 Diagnostico de variables.

codigo = "  mx-gdl-0042  "
#Longitud de la cadena, debe ser 15
print(len(codigo))
#obtener valores de los caracteres entre la pocisión 2 y 4, por los espacios que son 2 debera ser mx
print(codigo[2:4])
#obtener valores de los caracteres entre la pocisión -6 y -2, se cuenta desde 0, 
#entonces la pocisión -6 iniciara en la pocision 9 y el valos sera "0042"
print(codigo[-6:-2])
#Quitar espacios con "strip" y volver mayúsculas los caracteres"upper", obtenemos "MX-GDL-0042"
print(codigo.strip().upper())
# ".find" sirve para localizar valores en la cadena, de no encontrarlos devuelve "-1",
#en este caso al no encontrar "xyz" devolvera "-1"
print(codigo.find("xyz"))
#Para validar quue no se haya modificado el código agregardo "repr()", 
#mostrando el texto en comillas de la variable
print(repr(codigo))
# En este caso nos mostro '  mx-gdl-0042  ', siendo que strip() y upper() no modificaron el código

# Para guardar la tranformacion se a la asignamos a una nueva variable llamada "codigo_limpio"
# Cualquier tranformación para ser guardada debe asignarsele a la variable.
codigo_limpio = codigo.strip().upper()
print("Original:", repr(codigo))
print("Limpio:", repr(codigo_limpio))

# Se realizara la comparación de in y find()
#"in" regresara 'True' o 'False' y find(regresa la pocision donde empieza)
print("gdl" in codigo)
print(codigo.find("gdl"))


#¿Por qué un resultado "-1" no debe utilizarse como posición encontrada?
#Esto es por que el valor find -1, es un valor que nos indica si se encontro el valor o no
posicion = codigo.find("xyz")
# De esta manera si asignamos la posicion de "posicion = codigo.find("xyz")"  que es =-1
print(posicion)
#nos devolvera el valor " ", 
# por lo que tenemos que asegurar que se haya encontrado el valor solicitado antes de tomarlo como indice
print(repr(codigo[posicion]))


#1.2 Lectura de bdd


# Definir ruta del archivo etiquetas.
ruta = Path(__file__).resolve().parent / "datos" / "etiquetas.txt" #with cierra el archivo al terminar

etiquetas_originales= set() # Crear un conjunto para contar las etiquetas originales
etiquetas_normalizadas= set() # Crear un conjunto para contar las etiquetas ya normalizadas

with ruta.open("r", encoding="utf-8") as archivo: #("r": read para leer el archivo, encoding="utf-8": codigo de texto para leer as tildes ) 
    for linea in archivo: # Para recorrer el archivo por lineas
        etiqueta = linea.rstrip("\n") # "rstrip: Quita los saltos de pagina al final"
        etiquetas_originales.add(etiqueta) # Agrega la etiqueta al set , en caso de no estar repetida.

        limpia = etiqueta.strip().lower() #Quitamos espacios y hacemos minusculas y asignamos a nueva variable
        limpia = limpia.replace("-"," ").replace("_"," ") # Reemplazamos "-" y "_", con " " ( los valores los vimos al revisar las categorias sin limpiar )
        normalizada = "_".join(limpia.split())

        etiquetas_normalizadas.add(normalizada) # Agregamos transformaciones al set

print("Categorías antes:", len(etiquetas_originales)) # Con esta linea se contaran los registros.
print("Categorías despues:", len(etiquetas_normalizadas))
print("Categorías::", sorted(etiquetas_normalizadas))

'''
Antes de normalizar se identificaron 9 etiquetas distintas. 
Después de eliminar espacios extremos, convertir a minúsculas y unificar separadores, 
quedaron 3 categorías: acceso, pago_en_línea y soporte_técnico.

'''

# El siguiente ejemplo capitalize(), podria alterar la sigla SQL arrojando Sql

print("SQL".capitalize())

# El siguiente ejemplo es con SKU de un inventario 

sku = "ABC-0042"
print(sku.capitalize())

'''
Aplicar capitalize() a un SKU como ABC-0042 lo transforma en Abc-0042
Esto altera su nombre, lo que podría dificultar la búsqueda .

'''
'''
=============================================================================================

Etapa dos


==============================================================================================
'''
# Se ejecuta ejemplo_guiado.py



#El modo w reemplaza el contenido de errores.txt en cada ejecución,
# por lo que conserva dos líneas. 
# El modo a añade una línea a ejecuciones.log sin borrar las anteriores.

'''
=============================================================================================

Etapa tres


==============================================================================================
'''

from actividad_inicio import normalizar_categoria, validar_campos

prueba_valida = [
    " sol-0042 ",
    " USUARIO@EJEMPLO.COM ",
    " Pago-en_Línea ",
    "  Solicito   ayuda  "
]

print("PRUEBA VÁLIDA:", validar_campos(prueba_valida, set()))

prueba_vacia = [
    "SOL-0027",
    "alumno27@cucea.udg.mx",
    "",
    "Falta categoría"
]

print("PRUEBA CAMPO VACÍO:", validar_campos(prueba_vacia, set()))

print("VALIDADOR ACTUALIZADO")