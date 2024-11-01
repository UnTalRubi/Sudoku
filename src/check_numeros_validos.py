def check_numeros_enteros(sudoku):
    
    for fila in sudoku:
        for numero in fila:
            if not isinstance(numero, int):
                return False
            
    return True

def check_numeros_rango(sudoku):

    numeros_en_rango = range(1, len(sudoku) + 1)

    for fila in sudoku:
        for numero in fila:
            if numero not in numeros_en_rango:
                return False
            
    return True

def check_numeros_validos(sudoku):

    return check_numeros_enteros(sudoku) and check_numeros_rango(sudoku)

if __name__ == '__main__':

    import sys
    sys.path.append('..')

    import casosTest.casos_test_sudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith('__'):
            pass
            # Skip atributo
        else:
            print(attr, " => ", check_numeros_validos(casosTest.__dict__[attr]))