# Descomponer un numero en sus factores primos
def descomposition_primos():
    lista_primos = []
    while True:
        try:
            number = int(input("Enter a positive number: "))
            if number < 0:
                print("Enter a positive number")
            elif number >= 0:
                break
        except ValueError:
            print("Enter a correct value")
    for i in range(2, number + 1):
        while number % i == 0:
            number /= i
            lista_primos.append(i)
    print("List of Primo factors:",end=" ")
    for i in lista_primos:
        print(i,end=", ")

if __name__ == "__main__":
    descomposition_primos()
