estudiantes = [
    ("Ana", 20, 4.5),
    ("Carlos", 22, 3.8),
    ("Beatriz", 19, 4.2),
    ("David", 21, 2.9),
    ("Elena", 23, 4.9),
    ("Fernando", 20, 3.5),
    ("Gabriela", 22, 4.0),
    ("Héctor", 24, 2.5),
]

print(" INFORMACIÓN DE ESTUDIANTES ")
suma_notas = 0

for nombre, edad, nota in estudiantes:
  print(f"{nombre} tiene {edad} años y obtuvo una nota de {nota}")
  suma_notas += nota

print("\n CLASIFICACIÓN DE ESTUDIANTES ")
for nombre, edad, nota in estudiantes:
  if nota >= 4.5:
    clasificacion = "Excelente"
  elif nota >= 4.0:
    clasificacion = "Bueno"
  elif nota >= 3.0:
    clasificacion = "Aceptable"
  else:
    clasificacion = "Reprobó"

  print(f"{nombre}: {clasificacion}")

promedio = suma_notas / len(estudiantes)
print(f"\nEl promedio general es: {promedio:.2f}")

print("\n BÚSQUEDA DE ESTUDIANTE ")
nombre_buscado = input("Ingresa el nombre del estudiante que deseas buscar: ")
encontrado = False

for nombre, edad, nota in estudiantes:
  if nombre.lower() == nombre_buscado.lower():
    encontrado = True
    break

if encontrado:
  print(f"El estudiante {nombre_buscado} sí fue encontrado en la lista.")
else:
  print(f"No se encontró ningún estudiante con el nombre {nombre_buscado}.")
