import pytest
from src.check_sudoku import check_sudoku
import casosTest.casos_test_sudoku as casos_test

@pytest.mark.sudoku
def test_check_sudoku():
    assert check_sudoku (casos_test.correcto) == True

@pytest.mark.sudoku
def test_check_sudoku():
    assert check_sudoku (casos_test.numero_repetido_fila_columna) == False

@pytest.mark.sudoku
def test_check_sudoku():
    assert check_sudoku (casos_test.numero_no_presente) == False

@pytest.mark.sudoku
def test_check_sudoku():
    assert check_sudoku (casos_test.numero_fuera_del_rango) == False

@pytest.mark.sudoku
def test_check_sudoku():
    assert check_sudoku (casos_test.caracteres) == False

@pytest.mark.sudoku
def test_check_sudoku():
    assert check_sudoku (casos_test.numeros_reales) == False

@pytest.mark.sudoku
def test_check_sudoku():
    assert check_sudoku (casos_test.irregular_fila) == False

@pytest.mark.sudoku
def test_check_sudoku():
    assert check_sudoku (casos_test.irregular_columna) == False
