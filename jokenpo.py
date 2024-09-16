import random
import time

inicio = int(input('Seja bem-vindo\nDigite qualquer número para continuar:'))
modo = int(input('\n(1)PvP;\n(2)PvIA;\n(3)Simular partida.\n Escolha o modo de jogo: '))

jogadas = ["","Tesoura", "Papel", "Pedra"]

if modo == 1:
    print("\n(1)Tesoura\n(2)Papel\n(3)Pedra")
    x = int(input("\nFaça sua escolha: "))

    print("\n\n(1)Tesoura\n(2)Papel\n(3)Pedra")
    y = int(input("\nFaça sua escolha: "))

elif modo == 2:
    print('\n(1)Tesoura\n(2)Papel\n(3)Pedra')
    x = int(input('\nFaça sua escolha: '))

    y = random.randrange(1,4)

elif modo == 3:
    x = random.randrange(1,4)

    y = random.randrange(1,4)

print(f"Jogador1 jogou {jogadas[x]}")
time.sleep(3)
print(f"Jogador2 jogou {jogadas[y]}")

contador_x = 0
contador_y = 0

if x == 1 and y == 2:
    contador_x += 1
    print("Jogador1 venceu o jogador2")

