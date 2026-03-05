cantidad_estudiantes = int (input("por favor ingrese cuantos estudiantes se van a registrar\n"))

Promedio_total = 0
aprobados = 0
reprobados = 0

for i in range (1,cantidad_estudiantes + 1):
    nombre_estudiante = str (input(f"Cual es el nombre del estudiante numero {i}? \n"))
    nota1 = float (input(f"Porfavor ingrese la primera nota del estudiante {nombre_estudiante}\n"))
    nota2 = float (input(f"Porfavor ingrese la segunda nota del estudiante {nombre_estudiante}\n"))
    nota3 = float (input(f"Porfavor ingrese la tercera nota del estudiante {nombre_estudiante}\n"))

    if nota1 < 0 or nota1 > 5 or nota2 < 0 or nota2 > 5 or nota3 < 0 or nota3 > 5:
        print("Error: Las notas deben estar entre 0 y 5. Por favor, ingrese las notas nuevamente.")
        continue
    
    promedio_estudiante = (nota1 + nota2 + nota3) / 3
    print(f"El promedio del estudiante {nombre_estudiante} es: {promedio_estudiante}")

    Promedio_total += promedio_estudiante
    if promedio_estudiante >= 3.0:
        print(f"El estudiante {nombre_estudiante} ha aprobado.")
        aprobados += 1
    else:
        print(f"El estudiante {nombre_estudiante} ha reprobado.")
        reprobados += 1

Promedio_general = Promedio_total / cantidad_estudiantes
print(f"El promedio general de la clase es: {Promedio_general}")
print(f"Cantidad de estudiantes aprobados: {aprobados}")
print(f"Cantidad de estudiantes reprobados: {reprobados}")