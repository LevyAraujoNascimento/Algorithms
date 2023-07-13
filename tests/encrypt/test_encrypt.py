import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Teste para Tipos incorretos
    with pytest.raises(TypeError):
        encrypt_message(3, 'Freva')
    # Teste para Keys maiores que a string
    assert encrypt_message('Freva', 8) == 'averF'
    # Teste para valores Ímpares
    assert encrypt_message('Freva', 1) == 'F_aver'
    # Teste para valores Pares
    assert encrypt_message('Freva', 2) == 'ave_rF'
