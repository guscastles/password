"""
Jogo De Senha
Baseado num clássico jogo dos anos 80.
"""

import random

random_password = []
for n in range(1, 5):
    colour = ['Ve', 'Am', 'Az', 'Vo']
    random_colour = random.choice(colour)
    random_password.append(random_colour)


print('Você tem 04 chaves por tentativa, e 10 tentativas no total\n')
print('Índice de resultados: \n Pr = possui cor correta e posição correta \n Br = possui cor correta com posição  errada \n')
print('Opções de chaves: \nVerde = Ve \nVermelho = Vo \nAmarelo = Am \nAzul = Az \n')

chave = []

for num in range(1, 11):  

  if chave == random_password:
    print(f'Parabéns você acertou {random_password}!')
    break

  else:
    chave = []
    for n in range(1, 5):
      password = input(f'Insira a {n}ª chave: ')
      chave.append(password)
      
    print(f'Sua combinação foi: {chave}')

    resposta = []
    pino_preto = 'Pr'
    pino_branco = 'Br'

    for n in range(1, 5):
      if random_password[n-1] == chave[n-1]:
        resposta.append(pino_preto)

    for n in range(1, 5):
      if chave[n-1] in random_password and random_password[n-1] != chave[n-1]:
        resposta.append(pino_branco)
        
    print (f'Seus resultados foram: {resposta}')
    print (f'Faltam {10-num} tentativas \n')