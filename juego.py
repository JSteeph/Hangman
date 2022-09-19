from queue import Empty
from random import randint
from wsgiref.validate import validator



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
        palabra = []
        secretword = [letra for letra in secretword ]
        words = list(filter(lambda letra: letra == letra, secretword))
        words.remove("\n")
        
        for indice, valor in enumerate(secretword):
            
                palabra == valor 
                print(palabra)
                
            

      
        
        return palabra

        


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
                palabra = word(letra,secretword)
                
                print(palabra)
              
 

    

    
       
        



def run():
    read()


if __name__ == '__main__':
    run()
