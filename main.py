# Laboratorio 03: Funciones Primero y Siguiente
# Main.py - Orquestador principal

from gramatica import (
    ingresar_gramatica,
    obtener_no_terminales,
    obtener_terminales,
    mostrar_gramatica,
    mostrar_simbolos,
)
from primero import calcular_primero, mostrar_primero


def main():
    print("=" * 40)
    print("  LABORATORIO 03 - FIRST & FOLLOW")
    print("=" * 40)

    gramatica, simbolo_inicial = ingresar_gramatica()

    if not gramatica:
        print("\n[!] No se ingresó ninguna gramática.")
        return

    # Identificar símbolos
    no_terminales = obtener_no_terminales(gramatica)
    terminales = obtener_terminales(gramatica, no_terminales)

    mostrar_gramatica(gramatica)
    mostrar_simbolos(no_terminales, terminales)

    # Conjuntos Primero
    primero = calcular_primero(gramatica, no_terminales)
    mostrar_primero(primero)

    # Conjuntos Siguiente

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
