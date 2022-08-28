# PROGRAMA:     Programa que analiza las preferencias de compra entre  
#               pasteles y relleno de una pastelería durante una semana.
#               (Utiliza un array bidimencional y 2 arrays simples)
# EQUIPO:       Equipo 4
# FECHA:        Martes 30 de agosto

# ARRAY de productos disponibles en la pastelería
pasteles = ["Chocolate", "Red Velvet", "Tres leches", "Marmól","Zanaoria", "Moca-café"]
relleno = ["Merengue", "Chantilly", "Queso crema", "Cajeta", "Ganache", "Crema"]

regis = [[], []]    # Cant por c/u de pasteles y rellenos

cant = 6 
maP = 0;     maR = 0        
vap = 0;     var = 0    # Indices para ingresar nombre de PASTELES y RELLENOS (mayor)
vep = 0;     ver = 0    # Indices para ingresar nombre de PASTELES y RELLENOS (menor)

print("\nANALISÍS DE VENTAS - PASTELERÍA I love chocolate")

# Leer ventas por PASTEL
print("Porfavor, ingrese cantidad de PASTELES vendidos durante la semana:\n")
for i in range(len(pasteles)):
    regis[0].append(int(input(f"Pastel {i+1}. {pasteles[i]}:\t")))

# Leer ventas por RELLENO
print("\nPorfavor, ingrese cantidad de RELLENOS solicitados durante la semana:\n")
for i in range(len(relleno)):
    regis[1].append(int(input(f"Relleno {i+1}. {relleno[i]}:\t")))

# EVALUACIONES
for i in range(cant):       # EVALUACIÓN PASTELES
    if regis[0][i] > maP:   # La variable "mayor" cambiara hasta tomar el No.>
        maP = regis[0][i]   # intercambian los lugares y valores
        vap = i
    if regis[1][i] > maR:
        maR = regis[1][i]
        var = i

# NO. MENOR
meP = regis[0][0]           # Variable que servira para conocer cual es el número menor
meR = regis[1][0]

for i in range(cant):
    if regis[0][i] < meP:
        meP = regis[0][i]   # Intercambian los lugares y valores
        vep = i
    if regis[1][i] < meR:
        meR = regis[1][i]
        ver = i

# Resultados
print(f"\n· PASTELES\n+ VENDIDO: {pasteles[vap]} con {maP} unidades\n- VENDIDO: {pasteles[vep]} con {meP} unidades")
print(f"\n· RELLENOS\n+ VENDIDO: {relleno[var]} con {maR} unidades\n- VENDIDO: {relleno[ver]} con {meR} unidades")

print("\n¡Gracias por su preferencia!")
