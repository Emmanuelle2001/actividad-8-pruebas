from calculos import calcular_descuento, calcular_iva

def procesar_compra(precio_base: float, porcentaje_descuento: float, tasa_iva: float = 0.16) -> dict:
    """Calcula el total integrando descuento e IVA con manejo de try / except."""
    try:
        precio_con_descuento = calcular_descuento(precio_base, porcentaje_descuento)
        iva_calculado = calcular_iva(precio_con_descuento, tasa_iva)
        total_final = round(precio_con_descuento + iva_calculado, 2)
        
        return {
            "estado": "exito",
            "precio_con_descuento": precio_con_descuento,
            "iva": iva_calculado,
            "total": total_final
        }
    except ValueError as error:
        return {
            "estado": "error",
            "mensaje": str(error)
        }

if __name__ == "__main__":
    resultado = procesar_compra(1000.0, 10.0, 0.16)
    print("Resultado de compra validado por CI:", resultado)