import sys
sys.path.append('..')

from src.check_cuadrado import check_cuadrado
from src.check_numeros_validos import check_numeros_validos
from src.check_filas import check_filas
from src.check_columnas import check_columnas

def check_sudoku(sudoku):

    return check_cuadrado(sudoku) and check_numeros_validos(sudoku) and check_filas(sudoku) and check_columnas(sudoku)

if __name__ == '__main__':
    import sys
    sys.path.append('..')
    import casosTest.casos_test_sudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith('__'):
            pass

        else:
            print(attr, "=>", check_sudoku(casosTest.__dict__[attr]))