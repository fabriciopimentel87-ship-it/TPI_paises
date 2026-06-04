from funciones import*
paises = []

def main():
    limpiar_consola()
    if not os.path.exists("paises.csv"):
        crear_csv()
    paises = cargar_paises_csv()
    menu(paises)

if __name__ == "__main__":
    main()