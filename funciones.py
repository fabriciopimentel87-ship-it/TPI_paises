import questionary
import os
def limpiar_consola():
    os.system('cls' if os.name =='nt' else 'clear' )
def menu(paises):
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
            case "Filtrar países":
                pass
            case "Ordenar países":
                pass
            case "Mostrar estadísticas":
                pass
            case "Salir del programa":
                print("Saliendo del programa...")
                break