import os

def file_name():
    """Esta funcion devuelve el nombre del arhivo srt en el dirtorio"""    
    dir = os.listdir()
    for i in dir:
        archivo = i.split(".")
        if "srt" in archivo:
            return archivo[0]

    
def parser():

    txt = ""
    contenido = open("psyco.srt","r")
    print(contenido)
    for i in contenido.read():
        if i == "F":
            i = i.replace("F","XxX")
            txt += i
        else:
            txt += i
    contenido.close()

    with open("prueba.srt", "wb") as srt:
        srt.write(txt.encode("UTF-8"))
    print(txt)


if __name__ == '__main__':
    print(file_name())
