def hipotesis(numero):
    pasos = 0
    if numero > 0:
        for i in range(numero):
            if numero % 2 == 0:
                numero //= 2
                print(numero)
                pasos += 1
    elif numero != 1:
        for i in range(numero):
            numero = 3 * numero + 1
            print(numero)
            pasos += 1
    print(f"pasos: {pasos}")

if __name__ == '__main__':
    numero = int(input("Ingresa un numero natural: "))
    hipotesis(numero)