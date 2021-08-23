def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    men = int(input("Dame el número de mensajes: "))
    meg = float(input("Dame el número de megas: "))
    mnt = int(input("Dame el número de minutos: "))
    costo= (men*0.8)+(meg*0.8)+(mnt*0.8)
    
    print("El costo mensual es:", costo)
    
if __name__ == '__main__':
    main()
