import random

data={
    "1name":[],
    "2name":[],
    "1lastn":[],
    "2lastn":[],
}

numeric="0123456789"
alpha="abcdefghijklmnopqrstuvwxyz"

def AddData():
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

def usernameGen():
    sizefix=6
    a=data['1lastn'][0]+ data['1name'][0] + data['2name'][0]+data['2lastn'][0]+data['2name'][0]

    prefix="".join(random.sample(a, sizefix))
    sufix="".join(random.sample(numeric, sizefix))

    usr=prefix+sufix
    print(f"Tu nombre de usuario/id/matricula es: {usr}")
    
    while True:
        sct=int(input("Quiere usar otro nombre de usuario?\n1) Sí(s)\n2) No(n)\nSeleccione el número correspondiente: "))
        if sct==1:
            return True
        elif sct==2:
            return False
        elif sct!=1 or sct!=2:
            print("Seleccione una opción válida.")
            continue 

AddData()
while usernameGen()==True:
    if usernameGen()==False:
        print("Gracias por usar el programa")
        break