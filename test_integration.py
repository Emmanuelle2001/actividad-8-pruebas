from main import procesar_compra

def test_integracion_caso_try():
    """Prueba de integración donde el flujo se procesa dentro del bloque try."""
    # Base: 100. Descuento 10% -> 90. IVA (16% de 90) -> 14.40. Total -> 104.40
    respuesta = procesar_compra(100.0, 10.0, 0.16)
    assert respuesta["estado"] == "exito"
    assert respuesta["precio_con_descuento"] == 90.0
    assert respuesta["iva"] == 14.40
    assert respuesta["total"] == 104.40

def test_integracion_caso_exception():
    """Prueba de integración donde se detona la captura en el bloque exception."""
    # Porcentaje de descuento inválido (> 100%)
    respuesta = procesar_compra(100.0, 150.0, 0.16)
    assert respuesta["estado"] == "error"
    assert "Valores fuera de rango para el descuento." in respuesta["mensaje"]