def animelist(x):
    for x in range(a):
        print(f"anime {x+1}".center(50,"=").upper())
        anime=input(f"Nombre del anime: ")
        tanime=input(f"Temporada del anime: ")
        canime=input(f"No. de capitulos: ")

        pvv=input("Status del anime: Completado (c), Viendo(v), Pendiente(p)?: ")
        if pvv=='c':
            print("Añadiendo a su lista de animes completados...")
            vt_anime["n"].append(anime)
            vt_anime["s"].append(tanime)
            vt_anime["c"].append(canime)
        if pvv=='v':
            print("Añadiendo a su lista de animes en reproducción...")
            vndo_anime["n"].append(anime)
            vndo_anime["s"].append(tanime)
            vndo_anime["c"].append(canime)
        if pvv=='p':
            print("Añadiendo a su lista de animes pendientes...")
            pdn_anime["n"].append(anime)
            pdn_anime["s"].append(tanime)
            pdn_anime["c"].append(canime)


vt_anime={
    "n":[],
    "s":[],
    "c":[]
}

pdn_anime={
    "n":[],
    "s":[],
    "c":[]
}

vndo_anime={
    "n":[],
    "s":[],
    "c":[]
}
print(f"Anime list".upper().center(50))
print("Cuantos animes deseas agregar?")

a=int(input())
animelist(a)

f=open("data.txt", "w")
if len(vt_anime['n'])>0:
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

f.close()