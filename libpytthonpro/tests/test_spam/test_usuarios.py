from libpytthonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Rone', email='lemos_007_@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)





def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Rone', email='lemos_007_@hotmail.com'),
        Usuario(nome='Maria', email='lemos_007_@hotmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
