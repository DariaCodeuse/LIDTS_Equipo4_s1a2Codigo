# PROGRAMA:     Calcular prima vacacional y dias de vacaciones segun la antigüedad
# EQUIPO:       Equipo 4
# FECHA:        Martes 30 de agosto
# diccionario de datos del trabajador
daysvac={
    "name":[],
    "years":[],
    "slr":[],
    "prm":[],
    "ds":[]

}

# variables para salario minimo, dias minimos de vacaciones y aumento de dias de vacaciones en un rango de 2 a 4 años de antigüedad
dplus=2
ds=6
slr=172.87

## ingresando datos
print(f"Calcular prima vacional".title().center(80,"="))
n=input("Nombre del trabajador: ")
y=int(input("Años de antigüedad: "))

# condiciones para calcular nuestros dias de vacaciones x año
if y>1 and y<=4: 
    dplus=dplus*(y-1)
    ds=ds+dplus
if y>=5 and y<=9:
    ds=14
if y>=10 and y<=14:
    ds=16
if y>=15 and y<=19:
    ds=18
if y>=20 and y<=24:
    ds=20
if y>=25 and y<=29:
    ds=22
if y>=30 and y<=34:
    ds=24

calcvcs=(slr*ds)*.25 # calculando la prima vacacional

# agregando nuestros datos al diccionario
daysvac['name'].append(n) 
daysvac['years'].append(y)
daysvac['slr'].append(slr)
daysvac['prm'].append(calcvcs)
daysvac['ds'].append(ds)


# Mostrando resultados
print("=".center(80,"="))
print(f"Nombre: {daysvac['name'][0]}\nAntiguedad: {daysvac['years'][0]}\nSalario: {daysvac['slr'][0]}\nPrima vacacional: {daysvac['prm'][0]}\nDias de vaciones: {daysvac['ds'][0]}")