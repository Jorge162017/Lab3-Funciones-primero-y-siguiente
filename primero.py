# primero.py - Cálculo de conjuntos Primero (FIRST)

EPSILON = "ε"


def calcular_primero_de_cadena(cadena, primero, no_terminales):
    """
    Calcula FIRST de una cadena de símbolos (lista).
    Usado internamente por calcular_siguiente.
    """
    resultado = set()

    if not cadena:
        resultado.add(EPSILON)
        return resultado

    for simbolo in cadena:
        if simbolo == EPSILON:
            resultado.add(EPSILON)
            break
        elif simbolo not in no_terminales:
            # Es terminal
            resultado.add(simbolo)
            break
        else:
            # Es no terminal: agregar FIRST(simbolo) - {ε}
            resultado |= (primero.get(simbolo, set()) - {EPSILON})
            if EPSILON not in primero.get(simbolo, set()):
                break
    else:
        resultado.add(EPSILON)

    return resultado


def calcular_primero(gramatica, no_terminales):
    """
    Calcula los conjuntos FIRST para todos los no terminales.
    Itera hasta que no haya cambios (punto fijo).
    """
    primero = {nt: set() for nt in no_terminales}

    cambio = True
    while cambio:
        cambio = False
        for no_terminal, producciones in gramatica.items():
            for produccion in producciones:
                antes = len(primero[no_terminal])

                nuevos = calcular_primero_de_cadena(produccion, primero, no_terminales)
                primero[no_terminal] |= nuevos

                if len(primero[no_terminal]) > antes:
                    cambio = True

    return primero


def mostrar_primero(primero):
    print("\nCONJUNTOS PRIMERO")
    for nt in sorted(primero.keys()):
        contenido = ", ".join(sorted(primero[nt]))
        print(f"  FIRST({nt}) = {{ {contenido} }}")
