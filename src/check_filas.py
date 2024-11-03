def check_filas(sudoku):

    # Precondición
    assert isinstance(sudoku, list), "El sudoku tiene que ser una lista"

    for fila in sudoku:

        for (posicion, numero) in enumerate(fila):
            if numero in fila[posicion + 1:]:
                return False

    return True

if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casosTest.casos_test_sudoku as casos_test

    for attr in sorted(casos_test.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, " => ", check_filas(casos_test.__dict__[attr]))
           