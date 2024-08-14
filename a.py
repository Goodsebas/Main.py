meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Es otra forma de respuesta a algo gracioso",
            "RUSH": "Es una forma de ir a por un enemigo en un juego",
            "F": "Es una forma de respuesta a algo malo que paso oh una muerte",
            "GG": "Es una forma de respuesta a algo bueno que ah pasado en un juego como una victoria"
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!) o 'SALIR' para terminar: ")
    
    if word == "SALIR":
        break
    elif word in meme_dict:
        print(meme_dict[word])
    else:
        print("Palabra no encontrada en el diccionario.")
