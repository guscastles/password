"""
Jogo De Senha
Baseado num clássico jogo dos anos 80.
"""
import random
from password.engine import game_engine


def play():
    show_rules()
    random_password = create_password()
    game_engine.run_game_engine(random_password)


def show_rules():
    print('Você tem 04 chaves por tentativa, e 10 tentativas no total\n')
    print('Índice de resultados: \n Pr = possui cor correta e posição correta \n Br = possui cor correta com posição  errada \n')
    print('Opções de chaves: \nVerde = Ve \nVermelho = Vo \nAmarelo = Am \nAzul = Az \n')


def create_password():
    random_password = []
    for _ in range(1, 5):
        colour = ['Ve', 'Am', 'Az', 'Vo']
        random_colour = random.choice(colour)
        random_password.append(random_colour)
    
    return random_password


if __name__ == '__main__':
    play()