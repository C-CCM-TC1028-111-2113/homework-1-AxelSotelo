def main():
    #escribe tu código abajo de esta línea
    new=int(input("Dame la cantidad de juegos nuevos: "))
    used=int(input("Dame la cantidad de juegos usados: "))
    
    tot= (new*1000)+(used*350)
    print("El total de la compra es:", tot)
    
if __name__ == '__main__':
    main()
