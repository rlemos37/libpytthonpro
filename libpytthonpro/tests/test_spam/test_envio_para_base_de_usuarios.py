from unittest.mock import Mock

import pytest

# from libpytthonpro.spam.enviador_de_email import Enviador
from libpytthonpro.spam.main import EnviadorDeSpam
from libpytthonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Rone', email='lemos_007_@hotmail.com'),
            Usuario(nome='Maria', email='lemos_007_@hotmail.com')
        ],
        [
            Usuario(nome='Rone', email='lemos_007_@hotmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'lemos_007_@hotmail.com',
        'Curso Python Pro',
        'Confira os objetos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Rone', email='lemos_007_@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'lemosjp2013gmail.com',
        'Curso Python Pro',
        'Confira os objetos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'lemosjp2013gmail.com',
        'lemos_007_@hotmail.com',
        'Curso Python Pro',
        'Confira os objetos fantásticos'
    )
