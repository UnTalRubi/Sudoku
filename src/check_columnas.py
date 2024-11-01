def check_columnas(sudoku):

    #barricada
    assert isinstance(sudoku, list), "El sudoku tiene que ser una lista"

    numero_filas = len(sudoku)

    index_fila = 0
    for fila in sudoku:
        for numero in fila:
            index_fila_siguiente = index_fila + 1

            while index_fila_siguiente < numero_filas:
                try:
                    pos_num_fila_siguiente = sudoku[index_fila_siguiente].index(numero)
                except ValueError:
                    return False
                else:
                    if pos_num_fila_siguiente == fila.index(numero):
                        return False
                    else:
                        index_fila_siguiente += 1

        index_fila += 1
    
    return True

if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casosTest.casos_test_sudoku as casos_test

    for attr in sorted(casos_test.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, " => ", check_columnas(casos_test.__dict__[attr]))