EPSILON = "ε"

GRAMATICAS_EJEMPLO = {
    "1": {
        "nombre": "Expresiones aritméticas LL(1)",
        "simbolo_inicial": "E",
        "gramatica": {
            "E": [["T", "E'"]],
            "E'": [["+", "T", "E'"], ["-", "T", "E'"], [EPSILON]],

            "T": [["F", "T'"]],
            "T'": [["*", "F", "T'"], ["/", "F", "T'"], [EPSILON]],

            "F": [["(", "E", ")"], ["id"]],
        },
    },
}