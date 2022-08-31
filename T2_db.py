## PROGRAMA:     Administrador de tareas para workdays
# EQUIPO:       Equipo 4
# FECHA:        Martes 30 de agosto
#  Días de la semana
sm=["lunes","martes","miercoles","jueves","viernes"]

# Diccionarios dentro de diccionarios para agregar tareas
taskdb={
    "lunes":{ # día de la semana
        "act":[], # actividad
        "hour":[], # hora de la actividad
        "date":[], # fecha de la actividad
        "desc":[]  # descripción de la actividad
    },
    "martes":{
        "act":[],
        "hour":[],
        "date":[],
        "desc":[]
    },
    "miercoles":{
        "act":[],
        "hour":[],
        "date":[],
        "desc":[]
    },
    "jueves":{
        "act":[],
        "hour":[],
        "date":[],
        "desc":[]
    },
    "viernes":{
        "act":[],
        "hour":[],
        "date":[],
        "desc":[]
    },
}

def day(): # función para listar y seleccionar días para usar y/o agregar actividades
    for i in range(len(sm)): # listar días de la semana
        print(f"{i+1}) {sm[i]}")
    print(f"Por favor, seleccione el numero al que corresponde el dia para agregar su actividad")
    a=int(input()) # seleccionar el día


    if a==1:
        print("Dia seleccionando "+ f"{sm[a-1]}".upper()) # señalar el día seleccionado
        a=1
        return a # retorna a para el número de día
    elif a==2:
        print("Dia seleccionando "+ f"{sm[a-1]}".upper())
        a=2
        return a
    elif a==3:
        print("Dia seleccionando "+ f"{sm[a-1]}".upper())
        a=3
        return a
    elif a==4:
        print("Dia seleccionando "+ f"{sm[a-1]}".upper())
        a=4
        return a
    elif a==5:
        print("Dia seleccionando "+ f"{sm[a-1]}".upper())
        a=5
        return a

def lister(d): # listar actividades agregadas 
    print("Listando sus actividades...".title())
    for l in range(len(taskdb[sm[d-1]]["act"])):
        print(f"No. de Actividad {l+1}".upper().center(75,"="))
        print("Actividad:" + taskdb[sm[d-1]]["act"][l])
        print("Hora:" + taskdb[sm[d-1]]["hour"][l])
        print("Fecha:" + taskdb[sm[d-1]]["date"][l])
        print("Descripcion:" + taskdb[sm[d-1]]["desc"][l])



def addTask(d): # función para agregar días
    x=int(input("Numero de actividades desea agregar: ")) # número de actividades a ingresar
    for n in range(x): 
        while True:
            print(F"Añadiendo actividad {n+1} del día {sm[d-1]}...".title())
            at=input("Nombre de la actividad: ")
            hs=input("Hora de la actividad: ")
            dt=input("Fecha de la actividad: ")
            dsc=input("Descripcion de la actividad: ")

            if len(at)>0 and len(hs)>0 and len(dt)>0 and len(dsc)>0: # condición para revisar que no hayan datos vacios
                break
            else:
                print("No deje casillas vacias!\n")
                x=x-1
                print("Volviendo a añadir".upper())
                continue
        
        # agregar actividad a su días correspondientes
        taskdb[sm[d-1]]["act"].append(at)
        taskdb[sm[d-1]]["hour"].append(hs)
        taskdb[sm[d-1]]["date"].append(dt)
        taskdb[sm[d-1]]["desc"].append(dsc)

def remTask(d): # función para remover actividad
    rem=int(input("Numero de actividad que desea eliminar: "))
    taskdb[sm[d-1]]["act"].pop(rem-1)
    taskdb[sm[d-1]]["hour"].pop(rem-1)
    taskdb[sm[d-1]]["date"].pop(rem-1)
    taskdb[sm[d-1]]["desc"].pop(rem-1)

def printer():
    # enviar nuestras actividades a un fichero
    f=open("taskyfy.txt","w")
    for w in range(5):
        f.write(sm[w].upper()+"\n\n")
        for m in range(len(taskdb[sm[w]]["act"])):
            f.write(f"No. de Actividad {m+1}\nActividad: {taskdb[sm[w]]['act'][m]}\nHora: {taskdb[sm[w]]['hour'][m]}\nFecha: {taskdb[sm[w]]['date'][m]}\nDescripcion: {taskdb[sm[w]]['desc'][m]}\n\n")
    f.close()

while True: # repetir para agregar actividades sin limite y navegar entre eliminar, agregar, listar o imprimir
    print("\n")
    print(f"Adminstrador de tareas (workdays).".title().center(50,"*"))
    print(f"(A)Añadir una actividad\n(R) Remover una actividad\n(L)Leer actividades guardadas\n(I)Imprimir actividades")
    sct=input("Seleccione una opcion o use cualquier tecla para salir: ")

    # condiciones correspondientes a cada opción para invocar nuestras distintas funciones o cerrar nuestro script
    if sct=='A' or sct=='a':
        addTask(d=day())
        continue
    elif sct=='L' or sct=='l':
        lister(d=day())
        continue
    elif sct=='R' or sct=='r':
        remTask(d=day())
        continue
    elif sct=='I' or sct=='i':
        printer()
    else:
        print("Goodbye")
        break
