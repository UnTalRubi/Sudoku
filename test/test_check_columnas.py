import pytest
from src.check_columnas import check_columnas
import casosTest.casos_test_sudoku as casos_test

@pytest.mark.columas
def test_check_columnas():
    assert check_columnas (casos_test.correcto) == True

@pytest.mark.columas
def test_check_columnas():
    assert check_columnas (casos_test.numero_repetido_fila_columna) == False

@pytest.mark.columas
def test_check_columnas():
    assert check_columnas (casos_test.numero_no_presente) == False

@pytest.mark.columas
def test_check_columnas():
    assert check_columnas (casos_test.numero_fuera_del_rango) == False

@pytest.mark.columas
def test_check_columnas():
    assert check_columnas (casos_test.caracteres) == True

@pytest.mark.columas
def test_check_columnas():
    assert check_columnas (casos_test.numeros_reales) == True

@pytest.mark.columas
def test_check_columnas():
    assert check_columnas (casos_test.irregular_fila) == True

@pytest.mark.columas
def test_check_columnas():
    assert check_columnas (casos_test.irregular_columna) == False