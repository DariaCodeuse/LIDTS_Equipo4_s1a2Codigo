# PROGRAMA:     Algortimo para capturar promedios y nombres de estudiantes en 2 arreglos,
#               (un vector c/u) después ordenar de mayor a menor promedio, 
#               los nombres deben corresponder con los promedios
# EQUIPO:       Equipo 4
# FECHA:        Martes 30 de agosto

# ARRAYS vacios para guardar datos y variables auxiliares
name = []      # Nombre ARRAY
grade = []      # Promedio ARRAY
A = 0       # Cant. de alumnos
vGrade= 0      # Variable promedio
vName = ""    # Varibale nombres

print(f"ORGANIZADOR DE LISTAS ESCOLARES")
A = int(input("¿Cuántos alumnos hay en su salón de clases?\t"))

# READ NAMES AND GRADES
print("Porfavor, ingrese los siguientes datos")
for i in range (A):
    name.append(str(input(f"\n · Nombre del alumno {i+1}: \t")))
    grade.append(int(input(f"· Promedio general: \t")))

# Ciclo para oordenar por promedios (+ a -)
for i in range(A):      # Número de ciclo
    for j in range(A-1):  # Accesos a indices
        if grade[j] < grade[j+1]: 
            # Si ELEMENTO 1 es menor que el SEGUNDO, los valores intercambian lugar
            vGrade = grade[j]       # 1. Guarda valor en Variable para no perderlo
            vName = name[j]
            grade[j] = grade[j+1]   # 2. Promedio mayor pasa a POSICIÓN 1
            name[j] = name[j+1]
            grade[j+1] = vGrade     # 3. Promedio menor pasa a POSICIÓN 2
            name[j+1] = vName

# Resultados organizados
print(f"\nNOMBRE: \t\t PROMEDIO:")
for i in range(A):
    print(f"{i}. {N[i]}: \t\t {P[i]}")
