from queue import Empty
from random import randint


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def word(letra,secretword):
             
        secretword = [secretword for letra in secretword if letra == secretword]

        print(secretword)

def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('¡Genial! Has acertado una letra.')
        hiddenword(letra, palabra, tablero)
    else:
        print('¡Oh! Has fallado.')
        letras_erroneas.append(letra)


def hiddenword(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra

   



def read():

    with open("./archivos/data.txt","r", encoding="utf-8") as f:

        my_dict = {i for i in enumerate(f, start=1)}

        random = randint(0,int(len(my_dict)))
        

        for i,j in my_dict:
            if i == int(random):
                secretword = j
                secretword = normalize(secretword)
                print(secretword)

                letra = str(input("Ingresa una letra/vocal:"))
                word(letra,secretword)
                
              
 

    

    
       
        



def run():
    read()


if __name__ == '__main__':
    run()
