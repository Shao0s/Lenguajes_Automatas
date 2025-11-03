"""Autómata que acepta cadenas que terminen con la subcadena bb """
afd = {
    'estados': {'P', 'Q', 'R'},
    'alfabeto': {'a', 'b'},
    'transicion': {
        'P': {'b': 'Q', 'a': 'P'},
        'Q': {'b': 'R', 'a': 'P'},
        'R': {'b': 'R', 'a': 'P'}
    },
    'estado_inicial': 'P',
    'estados_finales': {'R'}
}

def analizador(adf, palabra):
    """"Función que simula el AFD"""
    estado_actual = adf['estado_inicial']
    for simbolo in palabra:
        if simbolo not in adf['alfabeto']:
            print(f"ERROR: símbolo '{simbolo}' fuera del alfabeto {adf['alfabeto']}")
            return False
        estado_actual = adf['transicion'][estado_actual][simbolo]
        print(f"Con '{simbolo}' → nuevo estado: {estado_actual}")
    return estado_actual in adf['estados_finales']

# Pruebas
cadenas = ["babbabb"]
for cadena in cadenas:
    print(f"\nAnalizando cadena: {cadena}")
    print(f"¿Se acepta? {analizador(afd, cadena)}")
