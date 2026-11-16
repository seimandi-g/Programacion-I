"""
Desafío 3: Administrador de contactos con listas, tuplas y diccionarios.

"""


def agregar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo electrónico: ").strip()

    if nombre == "" or telefono == "" or correo == "":
        print("Debes completar los tres datos.")
        return

    # La tupla reúne los datos capturados de un contacto.
    datos = (nombre, telefono, correo)

    # El diccionario permite identificar cada dato por su clave.
    contacto = {
        "nombre": datos[0],
        "telefono": datos[1],
        "correo": datos[2]
    }

    # La lista conserva los diccionarios de todos los contactos.
    contactos.append(contacto)
    print("Contacto agregado.")


def mostrar_contacto(contacto):
    print("Nombre:", contacto["nombre"])
    print("Teléfono:", contacto["telefono"])
    print("Correo electrónico:", contacto["correo"])
    print("-" * 30)


def ver_contactos(contactos):
    if len(contactos) == 0:
        print("No hay contactos registrados.")
        return

    print("\nLISTA DE CONTACTOS")
    for contacto in contactos:
        mostrar_contacto(contacto)


def buscar_contacto(contactos):
    nombre = input("Nombre del contacto que deseas buscar: ").strip()
    encontrado = False

    # Se busca el nombre completo sin distinguir mayúsculas y minúsculas.
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            mostrar_contacto(contacto)
            encontrado = True

    if not encontrado:
        print("No se encontró un contacto con ese nombre.")


def eliminar_contacto(contactos):
    nombre = input("Nombre del contacto que deseas eliminar: ").strip()

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            contactos.remove(contacto)
            print("Contacto eliminado.")
            # Si hay nombres repetidos, se elimina solo el primero.
            return

    print("No se encontró un contacto con ese nombre.")


def main():
    contactos = []

    while True:
        print("\nADMINISTRADOR DE CONTACTOS")
        print("1. Agregar un contacto")
        print("2. Ver la lista de contactos")
        print("3. Buscar un contacto por nombre")
        print("4. Eliminar un contacto por nombre")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            ver_contactos(contactos)
        elif opcion == "3":
            buscar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            print("Programa finalizado. Los contactos no se guardan al salir.")
            break
        else:
            print("Opción inválida. Elige un número del 1 al 5.")


if __name__ == "__main__":
    main()
