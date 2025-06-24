"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    min_max_por_clave = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) < 5:
                continue
            pares = columnas[4].split(",")
            for par in pares:
                clave, valor = par.split(":")
                valor = int(valor)
                if clave not in min_max_por_clave:
                    min_max_por_clave[clave] = [valor, valor]
                else:
                    min_max_por_clave[clave][0] = min(min_max_por_clave[clave][0], valor)
                    min_max_por_clave[clave][1] = max(min_max_por_clave[clave][1], valor)

    resultado = [(clave, vmin, vmax) for clave, (vmin, vmax) in sorted(min_max_por_clave.items())]
    return resultado