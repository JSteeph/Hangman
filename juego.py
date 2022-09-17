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



def read():

    with open("./archivos/data.txt","r", encoding="utf-8") as f:

        my_dict = {i for i in enumerate(f, start=1)}

        random = randint(0,int(len(my_dict)))
        

        for i,j in my_dict:
            if i == int(random):
                secretword = j
                secretword = normalize(secretword)
                print(secretword)


    for i in range(1,15):
        letra = str(input("Ingresa una letra/vocal:"))
    
        for secretword in secretword:
            if letra == secretword:
                print(secretword)
            else:
                print("-")
        
       
        



def run():
    read()


if __name__ == '__main__':
    run()
