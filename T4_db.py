# PROGRAMA:     Username generador (puede usarse para contraseñas)
# EQUIPO:       Equipo 4
# FECHA:        Martes 30 de agosto

import random # importando libreria para aleatorizar datos

# Diccionario para almacenar nuestros datos
data={
    "1name":[],
    "2name":[],
    "1lastn":[],
    "2lastn":[],
}

# Strings para generar nuestro username de manera aleatoria
numeric="0123456789"
alpha="abcdefghijklmnopqrstuvwxyz"

def AddData(): # funcion para agregar datos a nuestro diccionario (puede modificarse a palabras claves etc)

    # repetir cada introduccion de datos en caso de tener espacios y numeros, solo se aceptan caracteres
    while True:
        name=str(input("Primer nombre: "))
        if name.isalpha()==True and name.isspace()==False:
            data['1name'].append(name)
            break
        print("No utilize espacios o números!")
    
    while True:
        name2=str(input("Segundo nombre: "))
        if name2.isalpha()==True and name2.isspace()==False:
            data['2name'].append(name2)
            break
        print("No utilize espacios o números!")

    while True:
        lastn1=str(input("Apellido paterno: "))
        if lastn1.isalpha()==True and lastn1.isspace()==False:
            data['1lastn'].append(lastn1)
            break
        print("No utilize espacios o números!")

    while True:
        lastn2=str(input("Apellido materno: "))
        if lastn2.isalpha()==True and lastn2.isspace()==False:
            data['2lastn'].append(lastn2)
            break
        print("No utilize espacios o números!")

def usernameGen(): # Generador de nuestro username a partir de un prefijo (nombres o palabras claves) y un sufijo (letras y numeros), ambos de manera aleatoria
    sizefix=6 # tamaño para el prefijo y sufijo

    a=data['1lastn'][0]+ data['1name'][0] + data['2name'][0]+data['2lastn'][0]+data['2name'][0] #reuniendo nuestros datos en una sola variable
    prefix="".join(random.sample(a, sizefix)) # randomizando nuestros datos para formar un prefijo
    sufix="".join(random.sample(numeric, sizefix)) # randomizando números y letras para formar un sufijo

    usr=prefix+sufix # uniendo ambas variables para formar un solo username
    print(f"Tu nombre de usuario/id/matricula es: {usr}")
    
    while True: # Preguntar hasta que se obtenga una opción valida
        sct=int(input("Quiere usar otro nombre de usuario?\n1) Sí(s)\n2) No(n)\nSeleccione el número correspondiente: "))
        if sct==1: #Si se requiere otro username retorna True
            return True
        elif sct==2: #Si no se requiere retorna False
            return False
        elif sct!=1 or sct!=2: #Continuar el ciclo hasta que haya una opción valida
            print("Seleccione una opción válida.")
            continue 

AddData() # Agregar datos usando nuestra función

while usernameGen()==True: # repetir hasta encontrar un username de agrado
    if usernameGen()==False: # si nuestra función retorna False entonces romper el ciclo
        print("Gracias por usar el programa")
        break