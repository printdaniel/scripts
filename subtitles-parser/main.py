import os

def file_name():
    """Retorna el nombre del arhivo srt en el diretorio
    en caso de no haber archovo .srt retorna False"""    

    dir = os.listdir()
    for i in dir:
        archivo = i.split(".")
        if "srt" in archivo:
            name = archivo[0]
            return name
        else:
            print("No se encuentra archivo .srt en el directorio")
            return False

def dir_list():
    """Retorna lista del directorio"""
    
    for i in os.listdir():
        print(i)
    


def caracter_replace():
    to_replace = input("Ingrese el carácter a reemplazar: ")
    ca_replace = input("Ingrese el carácter por el que desea reemplazar: ")

    txt = ""
    archivo = file_name() + ".srt"
    contenido = open(archivo,"r")
    for i in contenido.read():
        if i == to_replace:
            i = i.replace(to_replace,ca_replace)
            txt += i
        else:
            txt += i
    contenido.close()

    save_name = input("Ingrese el nombre con el que desea guardar el archivo: ")
    save_file = save_name + ".srt"
    with open(save_file, "wb") as srt:
        srt.write(txt.encode("UTF-8"))

def menu():
    print("""\nSelecciones una acción:\n
              1 Borra un carácter
              2 Listar Directorio
              3 Salir
              """)

def main():
    menu()

    while True:
        opcion = int(input("Ingrese una opción: "))
        list_op = [1,2,3]

        if opcion in list_op:
            if opcion == 1:
                if file_name():
                    caracter_replace()
            if opcion == 2:
                dir_list()
            if opcion == 3:
                print("Programa finalizado")
                break
        else:
            print("elija una opción del 1 al 3")
            opcion = int(input("Ingrese una opción: "))

    print("Script Finalizado")


if __name__ == '__main__':
    main()
