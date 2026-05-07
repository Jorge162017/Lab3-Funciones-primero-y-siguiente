# Laboratorio 03: Funciones Primero y Siguiente
# Main.py - Orquestador principal

from gramatica import (
    ingresar_gramatica,
    obtener_no_terminales,
    obtener_terminales,
    mostrar_gramatica,
    mostrar_simbolos,
)



def main():
    print("=" * 40)
    print("  LABORATORIO 03 - FIRST & FOLLOW")
    print("=" * 40)

    gramatica, simbolo_inicial = ingresar_gramatica()

    if not gramatica:
        print("\n[!] No se ingresó ninguna gramática.")
        return

    # Puntos 1 y 2: identificar símbolos
    no_terminales = obtener_no_terminales(gramatica)
    terminales = obtener_terminales(gramatica, no_terminales)

    mostrar_gramatica(gramatica)
    mostrar_simbolos(no_terminales, terminales)

    # Punto 3: conjuntos Primero
    primero = calcular_primero(gramatica, no_terminales)
    mostrar_primero(primero)

    # Punto 4: conjuntos Siguiente
    siguiente = calcular_siguiente(gramatica, no_terminales, primero, simbolo_inicial)
    mostrar_siguiente(siguiente)

    print("\n" + "=" * 40)


if __name__ == "__main__":
    main()
