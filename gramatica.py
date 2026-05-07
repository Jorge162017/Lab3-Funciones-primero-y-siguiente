# gramatica.py - Ingreso de gramática e identificación de símbolos

EPSILON = "ε"


def ingresar_gramatica():
    print("Ingrese la gramática libre de contexto.")
    print("Formato ejemplo: S -> A B | a")
    print("Use ε para epsilon.")
    print("Escriba FIN para terminar.\n")

    gramatica = {}
    simbolo_inicial = None

    while True:
        linea = input("Producción: ").strip()

        if linea.upper() == "FIN":
            break

        if "->" not in linea:
            print("  [!] Formato inválido. Use: A -> a B | ε")
            continue

        izquierda, derecha = linea.split("->", 1)
        izquierda = izquierda.strip()

        if not izquierda:
            print("  [!] Formato inválido: falta el no terminal izquierdo.")
            continue

        producciones = derecha.split("|")
        producciones = [prod.strip().split() for prod in producciones]
        producciones = [prod for prod in producciones if prod]

        if izquierda not in gramatica:
            gramatica[izquierda] = []
            if simbolo_inicial is None:
                simbolo_inicial = izquierda  # El primero ingresado es el símbolo inicial

        gramatica[izquierda].extend(producciones)

    return gramatica, simbolo_inicial


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
    print("\nGRAMÁTICA INGRESADA")
    for no_terminal, producciones in gramatica.items():
        partes = [" ".join(prod) for prod in producciones]
        print(f"  {no_terminal} -> {' | '.join(partes)}")


def mostrar_simbolos(no_terminales, terminales):
    print("\nSÍMBOLOS IDENTIFICADOS")
    print(f"  No terminales : {{ {', '.join(sorted(no_terminales))} }}")
    print(f"  Terminales    : {{ {', '.join(sorted(terminales))} }}")
