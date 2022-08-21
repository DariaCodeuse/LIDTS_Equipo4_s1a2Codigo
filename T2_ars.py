# PROGRAMA:     Registro de compras con array bidimencional, debe leer:
#               nombre del producto, precio, cant y proporciona subtotal y total
# EQUIPO:       Equipo 4
# FECHA:        Augost 30th, 2022

# Programa que resgitra tareas escolares y las ordenar segun fecha de entrega ()
regis = [[], [], []]  # ARRAY BIDIMENSIONAL

print("REGISTRO DE COMPRAS".center(70,"-"))
# Solicito cantidad de datos
row = int(input("\t\t¿Cuántos productos ingresará?: "))    

# Leer datos de productos
for i in range(row):
    regis[0].append(input(f"\n\t\t· Producto {i+1}:\t"))
    regis[1].append(float(input(f"\t\t· Precio:\t")))
    regis[2].append(float(input(f"\t\t· Cantidad:\t"))) 

# Imprimo en terminal accediendo a indices del ARRAY bidimensional
print("TABLA DE TOTALES".rjust(70))
print(f"|------ PRODUCTO -------|---- PRECIO ---|-- CANTIDAD ---|---SUBTOTAL----|".ljust(10,"-"))

# Ciclo para recorrer ARRAY
for i in range(row):
    sub = regis[1][i] * regis[2][i] # Subtotal
    total =+ sub    # Total
    print(f"|\t{regis[0][i]}\t|\t${regis[1][i]}\t|\t${regis[2][i]}\t|\t${sub}\t|".ljust(10,"-").upper())

print(f" TOTAL:  ${total}".rjust(70,">"))

