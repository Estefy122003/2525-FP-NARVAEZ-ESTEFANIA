# Función para calcular descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento sobre un monto total.

    :param monto_total: Monto total de la compra
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%)
    :return: Monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Primer ejemplo: usando el descuento por defecto
    monto1 = 500
    descuento1 = calcular_descuento(monto1)
    print(f"Monto total: ${monto1}")
    print(f"Descuento aplicado ({10}%): ${descuento1}")
    print(f"Monto a pagar: ${monto1 - descuento1}\n")

    # Segundo ejemplo: especificando un descuento diferente
    monto2 = 800
    porcentaje2 = 20
    descuento2 = calcular_descuento(monto2, porcentaje2)
    print(f"Monto total: ${monto2}")
    print(f"Descuento aplicado ({porcentaje2}%): ${descuento2}")
    print(f"Monto a pagar: ${monto2 - descuento2}")
