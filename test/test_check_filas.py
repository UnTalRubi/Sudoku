import pytest
from src.check_filas import check_filas
import casosTest.casos_test_sudoku as casos_test

def test_check_filas(sudoku, sano):
    assert check_filas(sudoku) == sano

test_check_filas(casos_test.correcto, True)

test_check_filas(casos_test.numero_repetido_fila_columna, False)

test_check_filas(casos_test.numero_repetido_columna, True)

test_check_filas(casos_test.numero_no_presente, False)

test_check_filas(casos_test.numero_fuera_del_rango, True)

test_check_filas(casos_test.caracteres, True)

test_check_filas(casos_test.numeros_reales, True)

test_check_filas(casos_test.irregular_fila, True)

test_check_filas(casos_test.irregular_columna, True)

test_check_filas(casos_test.lista_vacia, True)