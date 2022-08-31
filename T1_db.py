# PROGRAMA:     Lista de animes (o cualquier otra cosa)
# EQUIPO:       Equipo 4
# FECHA:        Martes 30 de agosto

def animelist(x): # funcion para agregar animes donde nuestro argumento x será la cantidad de animes que añadiremos
    for x in range(a): # ciclo for para agregar el n número de animes
        print(f"anime {x+1}".center(50,"=").upper())
        anime=input(f"Nombre del anime: ")
        tanime=input(f"Temporada del anime: ")
        canime=input(f"No. de capitulos: ")

        # Seleccionar a que tipo de anime será añadido nuestra entrada
        pvv=input("Status del anime: Completado (c), Viendo(v), Pendiente(p)?: ")
        if pvv=='c':
            print("Añadiendo a su lista de animes completados...")
            vt_anime["n"].append(anime)
            vt_anime["s"].append(tanime)
            vt_anime["c"].append(canime)
        elif pvv=='v':
            print("Añadiendo a su lista de animes en reproducción...")
            vndo_anime["n"].append(anime)
            vndo_anime["s"].append(tanime)
            vndo_anime["c"].append(canime)
        elif pvv=='p':
            print("Añadiendo a su lista de animes pendientes...")
            pdn_anime["n"].append(anime)
            pdn_anime["s"].append(tanime)
            pdn_anime["c"].append(canime)

# diccionario para animes vistos
vt_anime={
    "n":[],
    "s":[],
    "c":[]
}

# diccionario para animes pendientes
pdn_anime={
    "n":[],
    "s":[],
    "c":[]
}

# diccionario para animes en curso
vndo_anime={
    "n":[],
    "s":[],
    "c":[]
}
print(f"Anime list".upper().center(50))

# cantidad de animes para nuestra función
print("Cuantos animes deseas agregar?")
a=int(input())
animelist(a)

# Escribiendo nuestros animes ingresados en un fiche siempre y cuando haya datos que agregar
f=open("data.txt", "w") # abriendo archivo
if len(vt_anime['n'])>0: #revisando dentro de nuestro diccionario si esta vacio 
    print(f"Escribiendo lista de animes completados...")
    f.write("completados\n".upper())
    for j in range(len(vt_anime['n'])):
        print(f"Anime: {vt_anime['n'][j].upper()} | Temporada: {vt_anime['s'][j]} | Capitulos: {vt_anime['c'][j].zfill(3)} Status: Completo".upper(), file=f)

if len(pdn_anime['n'])>0:
    print(f"Escribiendo lista de animes pendientes...")
    f.write("pendientes\n".upper())
    for k in range(len([pdn_anime['n']])):
        print(f"Anime: {pdn_anime['n'][k].capitalize()} | Temporada: {pdn_anime['s'][k]} | Capitulos: {pdn_anime['c'][k].zfill(3)} Status: Pendiente".upper(), file=f)

if len(vndo_anime['n'])>0:
    print(f"Escribiendo lista de animes en reproduccion...")
    f.write("En reproduccion\n".upper())
    for l in range(len(vndo_anime['n'])):
        print(f"Anime: {vndo_anime['n'][l].capitalize()} | Temporada: {vndo_anime['s'][l]} | Capitulos: {vndo_anime['c'][l].zfill(3)} Status: En reproduccion".upper(), file=f)

f.close() # cerrando archivo