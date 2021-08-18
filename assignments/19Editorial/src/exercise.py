import math
def main():
    #escribe tu código abajo de esta línea

    wds= int(input("Dame el número de palabras "))
    cst=float((wds/475))
    pag= math.ceil(cst)
    csto= pag*60
    csds=csto-(csto*.1)
    print("El costo de la publicación es ", csds)

if __name__ == '__main__':
    main()
