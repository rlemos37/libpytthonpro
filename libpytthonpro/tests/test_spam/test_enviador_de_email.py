import pytest

from libpytthonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['lemos_007_@hotmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'lemosjp2013@gmail.com',
        'Cursos Python Pro',
        'Turma Jéssica Ferrari aberta.'
    )

    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'lemos']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'lemosjp2013@gmail.com',
            'Cursos Python Pro',
            'Turma Jéssica Ferrari aberta.'
        )
