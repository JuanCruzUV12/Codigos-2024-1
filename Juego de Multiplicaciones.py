import random, time
def acierto_multiplicacion():
    nombre = input("Introduce tu nombre: ")
    respuestas_correctas = 0
    respuestas_incorrectas = 0
    for i in range(12):
        num1 = random.randint(-5, 15)
        num2 = random.randint(-5, 15)
        print(f"¿Cuánto es: {num1} x {num2}?")
        for i in range(12):
            try:
                resultado = num1 * num2
                respuesta = int(input("Ingresa la respuesta: "))
                if respuesta == resultado:
                    print("¡Respuesta correcta!")
                    respuestas_correctas += 1
                    time.sleep(2)
                    break
            except ValueError:
                print("Ingresaste un valor no válido")
            else:
                print(f"Respuesta incorrecta. La respuesta correcta es: {resultado}")
                respuestas_incorrectas += 1
                time.sleep(2)
                break
    print("**" * 25)
    print(f"Usuario: {nombre}\nRespuestas correctas: {respuestas_correctas}\nRespuestas incorrectas: {respuestas_incorrectas}")

if __name__ == "__main__":
    acierto_multiplicacion()
