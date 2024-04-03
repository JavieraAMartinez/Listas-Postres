POSTRES = {
    "Arroz con leche": ["Arroz", "Leche", "Azúcar", "Canela"],
    "Flan": ["Huevos", "Leche", "Azúcar", "Caramelo"],
    "Helado": ["Leche", "Crema", "Azúcar", "Esencias"],
    "Mousse de chocolate": ["Chocolate", "Crema", "Huevos", "Azúcar"],
    "Pay de queso": ["Galletas", "Queso crema", "Azúcar", "Huevos"]
}

def imprimir_ingredientes(nombre_postre):

    if nombre_postre not in POSTRES:
        print(f"El postre '{nombre_postre}' no existe.")
    else:
        print(f"Ingredientes para {nombre_postre}:")
        for ingrediente in POSTRES[nombre_postre]:
            print(f"- {ingrediente}")

def agregar_ingrediente(nombre_postre, nuevo_ingrediente):

    if nombre_postre not in POSTRES:
        print(f"El postre '{nombre_postre}' no existe.")
    else:
        if nuevo_ingrediente in POSTRES[nombre_postre]:
            print(f"El ingrediente '{nuevo_ingrediente}' ya está en la lista.")
        else:
            POSTRES[nombre_postre].append(nuevo_ingrediente)
            print(f"Ingrediente '{nuevo_ingrediente}' agregado a '{nombre_postre}'.")

def eliminar_ingrediente(nombre_postre, ingrediente_eliminar):

    if nombre_postre not in POSTRES:
        print(f"El postre '{nombre_postre}' no existe.")
    else:
        if ingrediente_eliminar in POSTRES[nombre_postre]:
            POSTRES[nombre_postre].remove(ingrediente_eliminar)
            print(f"Ingrediente '{ingrediente_eliminar}' eliminado de '{nombre_postre}'.")
        else:
            print(f"El ingrediente '{ingrediente_eliminar}' no está en la lista.")

def agregar_postre(nombre_postre, lista_ingredientes):

    if nombre_postre in POSTRES:
        print(f"El postre '{nombre_postre}' ya existe.")
    else:
        POSTRES[nombre_postre] = lista_ingredientes
        print(f"Postre '{nombre_postre}' creado con éxito.")

def eliminar_postre(nombre_postre):
    if nombre_postre in POSTRES:
        del POSTRES[nombre_postre]
        print(f"Postre '{nombre_postre}' eliminado.")
    else:
        print(f"El postre '{nombre_postre}' no existe.")

def mostrar_menu():
    print("Menú:")
    print("1. Ver ingredientes de un postre")
    print("2. Agregar un ingrediente a un postre")
    print("3. Eliminar un ingrediente de un postre")
    print("4. Agregar un nuevo postre")
    print("5. Eliminar un postre")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            nombre_postre = input("Ingrese el nombre del postre: ")
            imprimir_ingredientes(nombre_postre)
        elif opcion == "2":
            nombre_postre = input("Ingrese el nombre del postre al que desea agregar un ingrediente: ")
            nuevo_ingrediente = input("Ingrese el nombre del nuevo ingrediente: ")
            agregar_ingrediente(nombre_postre, nuevo_ingrediente)
        elif opcion == "3":
            nombre_postre = input("Ingrese el nombre del postre del que desea eliminar un ingrediente: ")
            ingrediente_eliminar = input("Ingrese el nombre del ingrediente que desea eliminar: ")
            eliminar_ingrediente(nombre_postre, ingrediente_eliminar)
        elif opcion == "4":
            nombre_postre = input("Ingrese el nombre del nuevo postre: ")
            ingredientes = input("Ingrese la lista de ingredientes separados por comas: ").split(", ")
            agregar_postre(nombre_postre, ingredientes)
        elif opcion == "5":
            nombre_postre = input("Ingrese el nombre del postre que desea eliminar: ")
            eliminar_postre(nombre_postre)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()

