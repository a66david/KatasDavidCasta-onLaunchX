def main ():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print ("No se encuentra config.txt")
    except IsADirectoryError:
        print("Encontramos config.txt pero es un directorio, no podemos leerlo!")
    except (BlockingIOError, TimeoutError):
        print ('No podemo configurar el documento')

if __name__ == '__main__':
    main()
        