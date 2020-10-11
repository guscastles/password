"""
Unit tests for password module
"""
from password import password as pw
from password.engine import game_engine as ge


def test_create_password():
    pwd = pw.create_password()
    assert isinstance(pwd, list)