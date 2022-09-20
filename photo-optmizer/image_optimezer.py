"""Optimizador de imagen"""
from PIL import Image
import os

#downloads_folder = 

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/'
print(BASE_DIR)


if __name__ == '__main__':
    for filename in os.listdir(BASE_DIR):
        name, extension = os.path.splitext(BASE_DIR + filename)

        if extension in [".jpg",".jpeg",".png"]:
            picture = Image.open(BASE_DIR + filename)
            picture.save(BASE_DIR + "compressed_"+filename,optimize=True,
                    quality=60)

            os.remove(BASE_DIR + filename)

