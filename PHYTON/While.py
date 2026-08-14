cantidad = 0
suma = 0

print("Ingresa números (ingresa 0 para terminar):")
while True:
    numero = float(input("Número: "))

    if numero == 0:
        break

    cantidad += 1
    suma += numero

if cantidad > 0:
    promedio = suma / cantidad
else:
    promedio = 0

print(f"\nCantidad de números ingresados: {cantidad}")
print(f"Suma total: {suma}")
print(f"Promedio: {promedio}")

