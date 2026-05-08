EPSILON = "ε"

GRAMATICAS_EJEMPLO = {
    "1": {
        "nombre": "Expresiones aritméticas con precedencia",
        "simbolo_inicial": "E",
        "gramatica": {
            "E": [["T", "E'"]],
            "E'": [["+", "T", "E'"], ["-", "T", "E'"], [EPSILON]],

            "T": [["F", "T'"]],
            "T'": [["*", "F", "T'"], ["/", "F", "T'"], [EPSILON]],

            "F": [["(", "E", ")"], ["id"], ["num"]],
        },
    },

    "2": {
        "nombre": "Sentencias tipo if, while y bloques",
        "simbolo_inicial": "S",
        "gramatica": {
            "S": [
                ["if", "E", "then", "S", "S'"],
                ["while", "E", "do", "S"],
                ["begin", "L", "end"],
                ["id", ":=", "E"],
            ],

            "S'": [["else", "S"], [EPSILON]],

            "L": [["S", "L'"]],

            "L'": [[";", "S", "L'"], [EPSILON]],

            "E": [["id"], ["num"], ["true"], ["false"]],
        },
    },

    "3": {
        "nombre": "Múltiples epsilons y propagación de FOLLOW",
        "simbolo_inicial": "S",
        "gramatica": {
            "S": [["A", "B", "C"]],

            "A": [["a", "A"], [EPSILON]],

            "B": [["b", "B"], [EPSILON]],

            "C": [["c", "C"], ["d"], [EPSILON]],
        },
    },
}