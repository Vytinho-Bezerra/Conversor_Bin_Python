import os
os.system ('cls')

print('Boas vindas ao conversor decimal!')
start = 1

while start == 1:
    print(' \n▶')
    print(6 * '- - - ')
    print('Opções para conversão:')
    print('[1] -> Binário\n[2] -> octdecimal\n[3] -> hexdecimal')
    print(6 * '- - - ')
    num = int(input('Digite um número decimal: '))
    temp = num
    opcao = int(input('Digite o número da opção desejada: '))
    base = 0
    string = ''
    dig = '0123456789ABCDEF'

    if opcao == 1:
        base = 2
        while num > 0:
            string = dig[num % base] + string
            num = num // base
        print(f'{temp}(10) = {string}(2)')
    
    elif opcao == 2:
        base = 8
        while num > 0:
            string = dig[num % base] + string
            num = num // base
        print(f'{temp}(10) = {string}(8)')

    elif opcao == 3:
        base = 16
        while num > 0:
            string = dig[num % base] + string
            num = num // base
        print(f'{temp}(10) = {string}(16)')

    else:
        print('Opção inválida...')

    print('')
    print(6 * '- - - ')
    print('[0] -> Encerrar\n[1] -> Iniciar outra conversão\n[2] -> Dados do projeto')
    print(6 * '- - - ')
    start = int(input('Digite a opcão desejada: '))
    while start == 2:
        print('')
        print('Curso: Análise e Desenvolvimento de Sistemas')
        print('')
        print('RMG: 33090416 | Nome: Augusto dos Santos Silva\nRMG: 33597219 | Nome: João Pedro Cardoso Ferreira\nRMG: 34740597 | Nome: Matheus Gonçalves Gomes de Souza\nRMG: 32764812 | Nome: Raul Tonti Sorbara\nRMG: 33073155 | Nome: Vyctor Santos do Nascimento Bezerra')
        print('')
        print('Disciplinas envolvidas: Programação de computadores | Organização e arquitetura de computadores')
        print('Versão: 3.0')
        print(6 * '- - - ')
        print('[0] -> Encerrar\n[1] -> Iniciar outra conversão')
        print(6 * '- - - ')
        start = int(input('Digite a opcão desejada: '))

if start == 0:
    print(' \nObrigado por utilizar nosso conversor! 😊\n ')