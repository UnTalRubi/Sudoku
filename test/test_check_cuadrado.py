import pytest  
from src.check_cuadrado import check_cuadrado
import casosTest.casos_test_sudoku as casos_test

def test_check_cuadrado(sudoku, sano):
    assert check_cuadrado == sano

test_check_cuadrado(casos_test.correcto, True)

test_check_cuadrado(casos_test.numero_repetido_fila_columna, True)

test_check_cuadrado(casos_test.numero_repetido_columna, True)
                    
test_check_cuadrado(casos_test.numero_no_presente, True)
                            
test_check_cuadrado(casos_test.numero_fuera_del_rango, True)
                            
test_check_cuadrado(casos_test.caracteres, True)

test_check_cuadrado(casos_test.numeros_reales, True)

test_check_cuadrado(casos_test.irregular_fila, False)
                            
test_check_cuadrado(casos_test.irregular_columna, False)

test_check_cuadrado(casos_test.lista_vacia, False)