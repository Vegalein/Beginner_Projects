import random

def dibujar_horcado(intentos):
    if intentos == 1:
        print("  O  ")
    elif intentos == 2:
        print("  O  ")
        print("  |  ")
    elif intentos == 3:
        print("  O  ")
        print("  |  ")
        print(" /   ")
    elif intentos == 4:
        print("  O  ")
        print("  |  ")
        print(" /|  ")
    elif intentos == 5:
        print("  O  ")
        print("  |  ")
        print(" /|\ ")
        print("Has perdido! El ahorcado ha sido ejecutado.")

def jugar():
    intentos = 0
    letras_adivinadas = []
    palabras_guess = random.choice(["caracol", "berlines", "tranvia", "pecera", "soterrar"])
    progreso = ["-" for i in palabras_guess]
    print("".join(progreso))
    print("BIENVENIDO AL JUEGO")
    print("//////////////////////////////")
    while intentos < 5:
        letras_posible = input("Dime una letra:  ")
        if letras_posible in palabras_guess:
            print("HAS ACERTADO")
            letras_adivinadas.append(letras_posible)
            for i in range(len(palabras_guess)):
                if palabras_guess[i] == letras_posible:
                    progreso[i] = letras_posible
            print("".join(progreso))
            if "".join(progreso) == palabras_guess:
                print("HAS GANADOOOOOO")
                break
        else:
            print(f"Nooooooo, la letra {letras_posible} no esta! ")
            intentos +=1
            dibujar_horcado(intentos)

    while True:
        respuesta = input("Quieres jugar de nuevo?  (s/n)")
        if respuesta == "s":
            jugar()
        elif respuesta == "n":
            break
        else:
            print("Por favor solo vale s/n")

jugar()
















