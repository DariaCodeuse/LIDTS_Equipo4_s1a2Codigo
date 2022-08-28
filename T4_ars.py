# PROGRAMA:     Juego del ahorcado con arrays
# EQUIPO:       Equipo 4
# FECHA:        Martes 30 de agosto

import random

abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
words = []

# Ciclo Menú para reinicciar juego / Menu Loop to game restart
while True:
    print("~".center(12,"~"))
    cant_words = int(input("THE HANG MAN\n~~~~~~~~~~~~\n¿Cuántas palabras quieres ingresar?\n"))

    # Añadir palabras al juego / Adding words to array
    i = 0
    while i < cant_words:           
        fill_List = str(input(f"Palabra {i+1}:\t"))
        fill_w = fill_List.upper()       

        # Añadir palabras con + 6 letras / Add only more than 6 letters words
        if len(fill_w) >= 6:        
            words.append(fill_w)
            i+=1
        elif len(fill_List) <= 5:
            print("\nError, ingresa otra palabra\n")

    # Escoge palabra aleatoria en lista / Pick an aleatory word from array
    random_w = random.choice(words)

    # Separa caracteres de palabra = lista / Split word caracteres
    word = random_w.upper()
    word = list(random_w)
    size_word = len(word)    

    # Mostrar posibles palabras (solo si se ingresan +3 palabras) / Show word array only if more than one word
    if cant_words > 3:
        print("\nEstan son las palabras ingresadas:")
        for i in range(cant_words):
            print(f"1. {words[i]}")

    # Generar array con guiones (panel para jugador) / Create array for player with undercores
    display = "_" * size_word
    display = list(display) 
    print(f"\nDeberás adivinar:\n{display}\n¿Lo lograras?\n")

    # Comienza el juego (evaluaciones) / Game start (evaluations)
    turns = int(5)
    while True:  

        answer = str(input("Ingresa una letra:\t"))
        answer = answer.upper()

        # Solo debe ingresar una letra
        if len(answer) != 1:
            print("\nX - No puedes ingresar más de una, escoge solo una\n")

        elif answer not in abc:
            print("\nX - Solo puedes ingresar LETRAS\n")

        # Si el jugador adivina
        elif answer in word:
            for i in range(size_word):
                if word[i] == answer:
                    display[i] = answer
            print(f"\nCorrecto!\nLa letra <{answer}> si se encuentra :)\n{display}")
            print(f"Turnos restantes = {turns}")
            
            # JUGADOR GANA / USER WINS
            if display == word:
                print("\n________________________\n< ¡FELICIDADES SHINJI! >")
                print(f"       YOU WIN <3\n________________________")
                break

        # Si el jugador NO adivina
        elif answer not in word:
            turns -= 1
            print(f"\nLo siento!\nLa letra <{answer}> no esta :(\n{display}")
            print(f"Turnos restantes = {turns}\n")
            

            # JUGADOR PIERDE / USER LOSE
            if turns == int(0):
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxx\n| Ya no tienes turnos :( |")
                print(f"       Has perdido.\nxxxxxxxxxxxxxxxxxxxxxxxxxx")
                break
     
    # Salida
    play = int(input("\n> ¿Deseas jugar de nuevo?\n1.Si!, continuar\n2.No, salir\n"))

    if play == 1:
        print("\nExcelente, gracias por jugar!\n")
    if play == 2:
        print("\nVuelve pronto!\nGracias por jugar <3\n")
        break