"""
Unit tests for password module
"""
from password import password


def test_create_password():
  pwd = password.create_password()
  assert isinstance(pwd, list)