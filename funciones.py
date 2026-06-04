import questionary
import os

def limpiar_consola():
    os.system('cls' if os.name =='nt' else 'clear' )

##funcion de validacion de str
def validar_str(mensaje):
    while True:
        try:
            nombre = input(mensaje).strip().lower()
            
            if nombre == "":
                raise ValueError("no se puede ingresar vacío")
            if not nombre.replace(" ", "").isalpha():
                raise ValueError("solo letras")
                
            return nombre  
            
        except ValueError as e:
            print(f"Error: {e}")


##funcion de validacion de numeros
def validar_numero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            
            if num <= 0:
                raise("error: debe ser mayor a 0")
            return num
        
        except ValueError as e:
            print(f"ERROR: {e}")


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

