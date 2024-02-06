import random
import string

from palabras import palabras # palabras sin Ñ
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():

    print("--------------")
    print(" Bienvenido/a ")
    print("--------------")

    palabra = obtener_palabra_valida(palabras)
    letrasAdivinar = set(palabra)
    letrasAdivinadas = set()
    abc = set(string.ascii_uppercase) #No contiene la Ñ

    vidas = 7


    while len(letrasAdivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado tantas letras: {' '.join(letrasAdivinadas)}")

        palabraLista = [letra if letra in letrasAdivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabraLista)}")

        letraUsuario = input("Escoge una letra: ").upper()

        if letraUsuario in abc - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)

            if letraUsuario in letrasAdivinar:
                letrasAdivinar.remove(letraUsuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra, {letraUsuario} no está en la palabra.")
        elif letraUsuario in letrasAdivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

            
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. La palabra era: {palabra}")
    else:
        print(f"¡Exelente! ¡Adivinaste la palabra {palabra}!")


ahorcado()
            
