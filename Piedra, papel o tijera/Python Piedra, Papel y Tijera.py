import random


def piedra_papel_tijera():
    print("---------------------------------------")
    print(" ¡BIENVENIDO/A! Piedra, Papel o Tijera ")
    print("---------------------------------------")
    print(" Juega piedra, papel, o tijera contra la computadora.")

    computadora = random.choice(['pi', 'pa', 'ti']) # Opcion elejida por la pc
    usuario = input("Escoje una opcion: 'pi' para piedra, 'pa' para papel o 'ti' para tijera \n ").lower()
        
    if usuario == computadora:
        return '¡Empate!'

    if gano_el_jugador(usuario, computadora):
        return '¡Ganaste!'

    return '¡Perdiste!'


def gano_el_jugador(jugador, oponente):
    if (
        (jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(piedra_papel_tijera())
        
