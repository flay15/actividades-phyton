# Definimos un diccionario con las notas de un estudiante
notas = {
    "Matemáticas": 85,
    "Ciencias": 90,
    "Historia": 78,
    "Lengua": 92}

# Iteramos sobre las claves y valores del diccionario
total = 0
for asignatura, nota in notas.items():
    print(f"{asignatura}: {nota}")
    total += nota

# Calculamos y mostramos el promedio de las notas
promedio = total / len(notas)
print(f"Promedio de notas: {promedio:.2f}")
