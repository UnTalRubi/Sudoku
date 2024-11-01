import pytest
from src.check_filas import check_filas
import casosTest.casos_test_sudoku as casos_test

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.correcto) == True

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.numero_repetido_fila_columna) == False

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.numero_repetido_columna) == True

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.numero_no_presente) == False

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.numero_fuera_del_rango) == True

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.caracteres) == True

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.numeros_reales) == True

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.irregular_fila) == True

@pytest.mark.filas
def test_check_filas():
    assert check_filas (casos_test.irregular_columna) == True