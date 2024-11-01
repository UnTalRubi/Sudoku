import pytest
from src.check_numeros_validos import check_numeros_validos
import casosTest.casos_test_sudoku as casos_test

@pytest.mark.numeros
def test_check_numeros_validos():
    assert check_numeros_validos (casos_test.correcto) == True

@pytest.mark.numeros
def test_check_numeros_validos():
    assert check_numeros_validos (casos_test.numero_repetido_fila_columna) == True

@pytest.mark.numeros
def test_check_numeros_validos():
    assert check_numeros_validos (casos_test.numero_no_presente) == True

@pytest.mark.numeros
def test_check_numeros_validos():
    assert check_numeros_validos (casos_test.numero_fuera_del_rango) == False

@pytest.mark.numeros
def test_check_numeros_validos():
    assert check_numeros_validos (casos_test.caracteres) == False

@pytest.mark.numeros
def test_check_numeros_validos():
    assert check_numeros_validos (casos_test.numeros_reales) == False

@pytest.mark.numeros
def test_check_numeros_validos():
    assert check_numeros_validos (casos_test.irregular_fila) == False

@pytest.mark.numeros
def test_check_numeros_validos():
    assert check_numeros_validos (casos_test.irregular_columna) == True