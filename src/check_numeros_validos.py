def numeros_enteros(sudoku):
    for fila in sudoku:
        for numero in fila:
            if not isinstance(numero, int):
                return False

    return True

def numeros_en_rango(sudoku):
    numeros_validos = range(1, len(sudoku) + 1)
    for fila in sudoku:
        for numero in fila:
            if numero not in numeros_validos:
                return False

    return True

def check_numeros_validos(sudoku):

    #barricada

    return numeros_enteros(sudoku) and numeros_en_rango(sudoku)


### CASOS TEST ###

if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casosTest.casos_test_sudoku as casos_test

    for attr in sorted(casos_test.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, " => ", check_numeros_validos(casos_test.__dict__[attr]))