"""
Main game engine for the Password game
"""
PINO_PRETO = 'Pr'
PINO_BRANCO = 'Br'


def run_game_engine(random_password):
    chave = []
    for attempt in range(1, 11):
        found_password = chave == random_password
        if found_password:
            print(f'Parabéns você acertou {random_password}!')
            break
        else:
            chave = _read_user_attempt()          
            resposta = _analyse_attempt(random_password, chave)
            _show_results(resposta, attempt)
    else:
        if not found_password:
            print(f'Que pena! A senha era {random_password}')


def _read_user_attempt():
    chave = []
    for order in range(1, 5):
        password = input(f'Insira a {order}ª chave: ')
        chave.append(password)
    
    print(f'Sua combinação foi: {chave}')
    
    return chave


def _analyse_attempt(random_password, chave):

    def is_colour_and_position_right(n):
        return random_password[n] == chave[n]
        
    def is_colour_right(n):
        return chave[n] in random_password and random_password[n] != chave[n]

    return [PINO_PRETO for n in range(4) if is_colour_and_position_right(n)] + \
           [PINO_BRANCO for n in range(4) if is_colour_right(n)]


def _show_results(resposta, attempt):
    print(f'Seus resultados foram: {resposta}')
    print(f'Faltam {10 - attempt} tentativas \n')
