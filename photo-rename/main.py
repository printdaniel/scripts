import os
from PIL import Image

path = os.getcwd()

def rename():
    new_name = input("Ingrese el nuevo nombre: ")
    id_pic = 0

    for filename in os.listdir(path):
        name, extension = os.path.splitext(path + filename)
        
        if extension in [".jpg",".jpeg",".png"]:
            pic = Image.open(filename)
            pic.save(new_name + str(id_pic) + extension, optimize=True, 
                    quality=60)

            os.remove(filename)
            print(name + ": " + extension)
            id_pic +=1
            

if __name__ == '__main__':
    rename()
