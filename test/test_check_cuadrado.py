import pytest  
from src.check_cuadrado import check_cuadrado
import casosTest.casos_test_sudoku as casos_test

@pytest.mark.cuadrado
def test_check_cuadrado():
    assert check_cuadrado (casos_test.correcto) == True

@pytest.mark.cuadrado
def test_check_cuadrado():
    assert check_cuadrado (casos_test.numero_repetido_fila_columna) == True

@pytest.mark.cuadrado
def test_check_cuadrado():
    assert check_cuadrado (casos_test.numero_repetido_columna) == True

@pytest.mark.cuadrado
def test_check_cuadrado():
    assert check_cuadrado (casos_test.numero_no_presente) == True
                    
@pytest.mark.cuadrado
def test_check_cuadrado():
    assert check_cuadrado (casos_test.numero_fuera_del_rango) == True
                            
@pytest.mark.cuadrado
def test_check_cuadrado():
    assert check_cuadrado (casos_test.numeros_reales) == True

@pytest.mark.cuadrado
def test_check_cuadrado():
    assert check_cuadrado (casos_test.irregular_fila) == False

@pytest.mark.cuadrado
def test_check_cuadrado():
    assert check_cuadrado (casos_test.irregular_columna) == False