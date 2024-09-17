import random
import time
from logging import raiseExceptions

print("Seja bem-vindo")
modo = int(input('-'*20 + '\n(1)PvP;\n(2)PvIA;\n(3)Simular partida.\n\nEscolha o modo de jogo: '))

jogadas = ["","Tesoura", "Papel", "Pedra"]
continuar = "c"
contador_x = 0
contador_y = 0

while continuar == "c":
    print("-"*20)
    if modo == 1:
        print('Modo escolhido: PvP')
        print("-"*20)
        print("\n(1)Tesoura\n(2)Papel\n(3)Pedra")
        x = int(input("\n(Jogador1) Escolha sua jogada: "))

        print("-"*20)

        print("\n(1)Tesoura\n(2)Papel\n(3)Pedra")
        y = int(input("\n(Jogador2) Escolha sua jogada: "))

    elif modo == 2:
        print('Modo escolhido: PvIA')
        print("-"*20)
        print('\n(1)Tesoura\n(2)Papel\n(3)Pedra')
        x = int(input('\nEscolha sua jogada: '))

        y = random.randrange(1,4)

    elif modo == 3:
        print('Modo escolhido: Simular partida')
        print("-"*20)
        x = random.randrange(1,4)

        y = random.randrange(1,4)

    else:
        raise Exception("Escolha inválida. Escolha somente entre '1', '2' ou '3'")

    print("-"*20)
    print(f"Jogador1 jogou {jogadas[x]}")
    time.sleep(3)
    print(f"Jogador2 jogou {jogadas[y]}\n")


    time.sleep(2)

    if x == 1 and y == 2:
        contador_x += 1
        print("Jogador1 venceu o jogador2")
    elif x == 1 and y == 3:
        contador_y += 1
        print("Jogador2 venceu o Jogador1")
    elif x == 1 and y == 1:
        print("Os jogadores empataram")
    elif x == 2 and y == 1:
        contador_y += 1
        print("Jogador2 venceu o Jogador1")
    elif x == 2 and y == 3:
        contador_x += 1
        print("Jogador1 venceu o Jogador2")
    elif x == 2 and y == 2:
        print("Os jogadores empataram")
    elif x == 3 and y == 1:
        contador_x += 1
        print("Jogador1 venceu o Jogador2")
    elif x == 3 and y == 2:
        contador_y += 1
        print("jogador2 venceu o Jogador1")
    elif x == 3 and y == 3:
        print("Os jogadores empataram")

    print(f"\nPlacar de vitórias:  x = {contador_x}   |    y = {contador_y}")
    print("-"*20)

    continuar = input("Aperte (c) para continuar ou (s) para sair: ")

else:
    print("Você saiu do jogo")
