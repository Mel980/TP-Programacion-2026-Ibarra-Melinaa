precio = float(input("Ingrese el precio del producto: "))

if precio >= 20000:
    descuento = precio * 0.10
    total = precio - descuento
    print(f"Precio original: ${precio}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"Total a pagar: ${total}")
else:
    descuento = 0
    total = precio
    print(f"Precio original: ${precio}")
    print(f"Descuento: $0")
    print(f"Total a pagar: ${total}")