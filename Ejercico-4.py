# Ejercicio 04: Registro de participación
registros = 0
total_personas = 0

cantidad = int(input("Cantidad (finaliza con 0): "))

while cantidad != 0:
    if cantidad < 0:
        print("No se permiten cantidades negativas. Intente de nuevo.")
    else:
        registros = registros + 1
        total_personas = total_personas + cantidad
    
    cantidad = int(input("Cantidad (finaliza con 0): "))

print(f"Registros realizados: {registros}")
print(f"Total de personas: {total_personas}")