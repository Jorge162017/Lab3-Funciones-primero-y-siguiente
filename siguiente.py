from primero import calcular_primero_de_cadena

EPSILON = "ε"
FIN_CADENA = "$"


def calcular_siguiente(gramatica, primero, no_terminales, simbolo_inicial):
    siguiente = {nt: set() for nt in no_terminales}

    # Regla 1: $ pertenece a FOLLOW(S), donde S es el símbolo inicial
    if simbolo_inicial is not None:
        siguiente[simbolo_inicial].add(FIN_CADENA)

    cambio = True

    while cambio:
        cambio = False

        for izquierda, producciones in gramatica.items():
            for produccion in producciones:

                for i, simbolo in enumerate(produccion):

                    # Solo calculamos FOLLOW para no terminales
                    if simbolo not in no_terminales:
                        continue

                    antes = len(siguiente[simbolo])

                    # beta es lo que viene después del símbolo actual
                    beta = produccion[i + 1:]

                    primero_beta = calcular_primero_de_cadena(
                        beta,
                        primero,
                        no_terminales
                    )

                    # Regla 2:
                    # Si A -> α B β, entonces FIRST(β) - {ε}
                    # se agrega a FOLLOW(B)
                    siguiente[simbolo] |= (primero_beta - {EPSILON})

                    # Regla 3:
                    # Si β es vacío o FIRST(β) contiene ε,
                    # entonces FOLLOW(A) se agrega a FOLLOW(B)
                    if not beta or EPSILON in primero_beta:
                        siguiente[simbolo] |= siguiente[izquierda]

                    if len(siguiente[simbolo]) > antes:
                        cambio = True

    return siguiente

def mostrar_siguiente(siguiente):
    print("\nCONJUNTOS SIGUIENTE")
    for nt in sorted(siguiente.keys()):
        contenido = ", ".join(sorted(siguiente[nt]))
        print(f"  FOLLOW({nt}) = {{ {contenido} }}")