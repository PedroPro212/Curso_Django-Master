import api
import os

# Criar variavel de ambiente no Windows: $env:USUARIO_API = 'pycodebr'
# $env:SENHA_API = '1234' 
# Para sobreescrever a variavel, é apenas digitar a chave e o novo valor

usuario = os.environ.get('USUARIO_API') # Capturou o usuário que está nas variaveis do ambiente na máquina local
senha = os.environ.get('SENHA_API')  #Capturou a senha que está nas variaveis do ambiente na máquina local
print(usuario)
print(senha)

login = api.login(usuario, senha)   # Chama a função de login no outro arquivo
print(login)