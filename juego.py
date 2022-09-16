from random import randint


def choose():
    pass
    



def read():
    
    with open("./archivos/data.txt","r", encoding="utf-8") as f:

        my_dict = {i for i in enumerate(f, start=1)}

        print(len(my_dict))







def run():
    read()


if __name__ == '__main__':
    run()
