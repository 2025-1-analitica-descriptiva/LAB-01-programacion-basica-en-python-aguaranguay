"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    resumen = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])

            if letra not in resumen:
                resumen[letra] = [valor, valor]  # [max, min]
            else:
                resumen[letra][0] = max(resumen[letra][0], valor)
                resumen[letra][1] = min(resumen[letra][1], valor)

    resultado = [(letra, maximo, minimo) for letra, (maximo, minimo) in sorted(resumen.items())]

    return resultado