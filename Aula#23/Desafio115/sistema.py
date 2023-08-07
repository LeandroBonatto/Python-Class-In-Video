from Desafio115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opcao 1')
    elif resposta == 2:
        cabecalho('Opcao 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema... Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opcao valida!\033[m')
    sleep(2)