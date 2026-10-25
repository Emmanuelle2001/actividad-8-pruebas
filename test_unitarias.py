import pytest
from calculos import calcular_descuento, calcular_iva

def test_descuento_unitario():
    assert calcular_descuento(100.0, 10.0) == 90.0

def test_iva_unitario():
    assert calcular_iva(100.0, 0.16) == 16.0