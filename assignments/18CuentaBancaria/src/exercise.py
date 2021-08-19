def main():
    #escribe tu código abajo de esta línea
    ant= float(input("Dame el saldo del mes anterior: "))
    ing= float(input("Dame los ingresos: "))
    egr= float(input(" Dame los egresos: "))
    cheq= int(input("Dame el número de cheques: "))

    s= ant+ing-egr-13*cheq
    sn=s-.075*s
    
    print("El saldo final de la cuenta es:", sn) 

if __name__ == '__main__':
    main()
