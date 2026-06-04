import questionary
import os
import csv

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
def validar_entero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            
            if num <= 0:
                raise ValueError("error: debe ser mayor a 0")
            return num
        
        except ValueError as e:
            print(f"ERROR: {e}")
##crea el csv con el encabezado 
def crear_csv():
    with open("paises.csv", "w", newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
    
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
        

##guarda el pais cargado de la opcion 1
def guardar_paises_csv(paises):
    with open("paises.csv", "w", newline='', encoding='utf-8') as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)


def cargar_paises_csv():
    paises = []
    
    if os.path.exists("paises.csv"):
        with open("paises.csv", newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
    
    return paises

## opcion 1 del menu:
def agregar_pais(paises):
    try:
        nombre = validar_str("ingrese el nombre del pais que desea agrgar: ")
        
        for pais in paises:
            if pais["nombre"] == nombre:
                print("EL PAIS YA EXISTE")
                return
        
        poblacion = validar_entero(f"ingrese la poblacion para {nombre}: ")
        superficie = validar_entero(f"ingrese la superficie para {nombre}: ")
        continente = validar_str(f"ingrese el continente de {nombre}: ")

        nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
        }
        paises.append(nuevo_pais)
        guardar_paises_csv(paises)
        print("pais agregado correctamente")
    except PermissionError:
        print("ERROR: no se puede escribir, el archivo puede estar siendo utilizado por otro programa")
    except Exception as e:
        print(f"ocurrio un error inesperado: {e}") 
    finally:
        print("el proceso de registro fue finalizado")
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
                agregar_pais(paises)
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

