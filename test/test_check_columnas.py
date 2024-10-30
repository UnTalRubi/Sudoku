import pytest
from src.check_columnas import check_columnas
import casosTest.casos_test_sudoku as casos_test

def test_check_columnas(sudoku, sano):
    assert check_columnas(sudoku) == sano

test_check_columnas(casos_test.correcto, True)
test_check_columnas(casos_test.numero_repetido_fila_columna, False)
test_check_columnas(casos_test.numero_repetido_columna, False)
test_check_columnas(casos_test.numero_no_presente, False)
test_check_columnas(casos_test.numero_fuera_del_rango, False)
test_check_columnas(casos_test.caracteres, True)
test_check_columnas(casos_test.numeros_reales, True)
test_check_columnas(casos_test.irregular_fila, True)
test_check_columnas(casos_test.irregular_columna, True)

