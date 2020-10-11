"""
Main game engine for the Password game
"""
PINO_PRETO = 'Pr'
PINO_BRANCO = 'Br'
PWD_MATCH = '*'
CHAVE_MATCH = '@'


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
    rand_pwd = random_password[:]
    chv = chave[:]
    return [PINO_PRETO for n in range(4) if is_colour_and_position_right(rand_pwd, chv, n)] + \
           [PINO_BRANCO for n in range(4) if is_colour_right(rand_pwd, chv, n)]


def is_colour_and_position_right(random_password, chave, position):
    if random_password[position] == chave[position]:
        random_password[position] = PWD_MATCH
        chave[position] = CHAVE_MATCH
        return True
    return False    


def is_colour_right(random_password, chave, position):
    return chave[position] in random_password
 

def _show_results(resposta, attempt):
    print(f'Seus resultados foram: {resposta}')
    print(f'Faltam {10 - attempt} tentativas \n')