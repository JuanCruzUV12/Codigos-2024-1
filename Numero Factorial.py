#Factoriales
numero = int(input("Enter your number"))

def factorial(numero):
    if numero < 0: return None
    if numero < 2: return 1
    return factorial(numero-1) * numero

if __name__ == "__main__":
    print(factorial(numero))
