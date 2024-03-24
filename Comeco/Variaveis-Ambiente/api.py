def login(usuario, senha):
    if usuario == 'pycodebr' and senha == '1234':
        return 'Login aprovado, você está loagado!'
    else:
        return 'Login incorreto, você foi desconectado!'