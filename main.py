# Laboratorio 03 - Funciones Primero y Siguiente
# Ingresar gramática e identificar terminales/no terminales

EPSILON = "ε"

def ingresar_gramatica():
    print("Ingrese la gramática libre de contexto.")
    print("Formato ejemplo: S -> A B | a")
    print("Use ε para epsilon.")
    print("Escriba FIN para terminar.\n")

    gramatica = {}

    while True:
        linea = input("Producción: ").strip()

        if linea.upper() == "FIN":
            break

        if "->" not in linea:
            print("Formato inválido. Use: A -> a B | ε")
            continue

        izquierda, derecha = linea.split("->", 1)
        izquierda = izquierda.strip()

        # Validación: lado izquierdo no puede estar vacío
        if not izquierda:
            print("Formato inválido: falta el no terminal izquierdo.")
            continue

        producciones = derecha.split("|")
        producciones = [prod.strip().split() for prod in producciones]

        if izquierda not in gramatica:
            gramatica[izquierda] = []

        # Ignorar producciones vacías (ej: "A ->" sin nada a la derecha)
        gramatica[izquierda].extend([prod for prod in producciones if prod])

    return gramatica


def obtener_no_terminales(gramatica):
    return set(gramatica.keys())


def obtener_terminales(gramatica, no_terminales):
    terminales = set()

    for producciones in gramatica.values():
        for produccion in producciones:
            for simbolo in produccion:
                if simbolo not in no_terminales and simbolo != EPSILON:
                    terminales.add(simbolo)

    return terminales


def mostrar_gramatica(gramatica):
    print("\nGRAMÁTICA INGRESADA:")
    for no_terminal, producciones in gramatica.items():
        partes = [" ".join(prod) for prod in producciones]
        print(f"{no_terminal} -> {' | '.join(partes)}")


def main():
    gramatica = ingresar_gramatica()

    if not gramatica:
        print("No se ingresó ninguna gramática.")
        return

    no_terminales = obtener_no_terminales(gramatica)
    terminales = obtener_terminales(gramatica, no_terminales)

    mostrar_gramatica(gramatica)

    print("\nSÍMBOLOS NO TERMINALES:")
    print("{" + ", ".join(sorted(no_terminales)) + "}")

    print("\nSÍMBOLOS TERMINALES:")
    print("{" + ", ".join(sorted(terminales)) + "}")

if __name__ == "__main__":
    main()