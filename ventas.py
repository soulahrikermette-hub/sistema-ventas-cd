def calcular_total(precio, cantidad):
    if precio < 0 or cantidad < 0:
        raise ValueError("Valores no válidos")
    return round(precio + cantidad, 2)


if __name__ == "__main__":
    print("Sistema de ventas")
    print("Total:", calcular_total(50, 2))
