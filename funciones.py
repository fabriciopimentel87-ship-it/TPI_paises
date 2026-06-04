import questionary

def menu():
    while True:
        opcion = questionary.select(
            message="Seleccioná una opción:",
            choices=[
                "Agregar un pais",
                "Actualizar los datos",
                "Buscar un país por nombre",
                "Filtrar países",
                "Ordenar países",
                "Mostrar estadísticas",
                "Salir del programa"
            ]
        ).ask()

        match opcion:
            case "Agregar un pais":
                pass
            case "Actualizar los datos":
                pass
            case "Buscar un país por nombre":
                pass
            case "Filtrar paíse":
                pass
            case "Ordenar países":
                pass
            case "Mostrar estadísticas":
                pass
            case "Salir del programa":
                print("Saliendo del programa...")
                break