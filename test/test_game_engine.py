"""
Unit tests for password module
"""
import pytest
from password import password as pw
from password.engine import game_engine as ge


@pytest.fixture
def random_password():
    return ['Vo', 'Vo', 'Az', 'Ve']


def test_is_colour_all_green(random_password):
    rand_pwd = random_password[:]
    rand_pwd[3] = '*'
    chave = ['Ve', 'Ve', 'Ve', '-']
    assert not ge.is_colour_right(rand_pwd, chave, 0)
    assert not ge.is_colour_right(rand_pwd, chave, 1)
    assert not ge.is_colour_right(rand_pwd, chave, 2)
    assert not ge.is_colour_right(rand_pwd, chave, 3)