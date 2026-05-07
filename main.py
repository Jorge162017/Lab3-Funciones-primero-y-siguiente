# Laboratorio 03: Funciones Primero y Siguiente
# main.py - Orquestador principal

from gramatica import (
    obtener_no_terminales,
    obtener_terminales,
    mostrar_gramatica,
    mostrar_simbolos,
)

from primero import calcular_primero, mostrar_primero
from siguiente import calcular_siguiente, mostrar_siguiente
from ejemplos import GRAMATICAS_EJEMPLO


def seleccionar_gramatica():
    print("\nSeleccione una gramática:\n")

    opciones = list(GRAMATICAS_EJEMPLO.keys())

    for indice, clave in enumerate(opciones, start=1):
        ejemplo = GRAMATICAS_EJEMPLO[clave]
        print(f"{indice}. {ejemplo['nombre']}")

    opcion = input("\nOpción: ").strip()

    try:
        indice_ejemplo = int(opcion) - 1
        clave = opciones[indice_ejemplo]

        ejemplo = GRAMATICAS_EJEMPLO[clave]

        return ejemplo["gramatica"], ejemplo["simbolo_inicial"]

    except (ValueError, IndexError):
        print("\n[!] Opción inválida.")
        return None, None


def main():
    print("=" * 40)
    print("  LABORATORIO 03 - FIRST & FOLLOW")
    print("=" * 40)

    gramatica, simbolo_inicial = seleccionar_gramatica()

    if not gramatica:
        print("\n[!] No se seleccionó ninguna gramática.")
        return

    # Identificar símbolos
    no_terminales = obtener_no_terminales(gramatica)
    terminales = obtener_terminales(gramatica, no_terminales)

    # Mostrar gramática
    mostrar_gramatica(gramatica)
    mostrar_simbolos(no_terminales, terminales)

    # Conjuntos FIRST
    primero = calcular_primero(gramatica, no_terminales)
    mostrar_primero(primero)

    # Conjuntos FOLLOW
    siguiente = calcular_siguiente(
        gramatica,
        primero,
        no_terminales,
        simbolo_inicial
    )

    mostrar_siguiente(siguiente)

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()