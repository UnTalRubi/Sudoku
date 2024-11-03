print("Esto es la pre-funcion check_cuadrado")

def check_cuadrado(sudoku):

    # Precondición
    assert isinstance(sudoku, list), "El sudoku tiene que ser una lista"

    sudokuSano = True
    numero_filas = len(sudoku)

    for fila in sudoku:
        if len(fila) != numero_filas:
            sudokuSano = False
            break

    # Postcondicion
    assert isinstance(sudokuSano, bool), "El sudoku tiene que devolver un valor lógico"

    return sudokuSano

print("Esto es la post-funcion de check_cuadrado")

if __name__ == '__main__':

    print("Esto es el main de check_cuadrado")

    import sys
    sys.path.append('..')

    import casosTest.casos_test_sudoku as casos_test

    for attr in sorted(casos_test.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, " => ", check_cuadrado(casos_test.__dict__[attr]))
    
