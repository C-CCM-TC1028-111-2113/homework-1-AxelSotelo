def main():
    #escribe tu código abajo de esta línea
    #Lee los datos
    import math

    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    
    s = (y2-y1)/(x2-x1)
    
    print("Pendiente:", s)


if __name__ == '__main__':
    main()
