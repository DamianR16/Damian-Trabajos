#Ciudades 

estudiantes = {
    "Ana": "Bogotá",
    "Carlos": "Medellín",
    "Sofia": "Bogotá",
    "Mateo": "Pereira",
    "Lucía": "Bogotá",
    "Andrés": "Medellín",
}


for nombre, ciudad in estudiantes.items():
    print(f"{nombre} vive en {ciudad}")

print("-" * 30)


contador_ciudades = {}
for ciudad in estudiantes.values():
    if ciudad in contador_ciudades:
        contador_ciudades[ciudad] += 1
    else:
        contador_ciudades[ciudad] = 1

print(contador_ciudades)


