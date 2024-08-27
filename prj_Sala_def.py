import os
import random
from variavelsalas import salas

def v_opcao():
    while True:
        opcao = input('[i]nserir [a]pagar [l]istar [f]inalizar ')
        if opcao in ('i','a','l','f'):
            return opcao
        else:
            os.system('cls')
            print('Valor de seleção incorreto, por favor digite novamente')
            continue

def v_sala():
    while True:
        sala = input('Informe a sala que deseja utilizar (1)(2)(3): ')
        try:
            sala = int(sala)
            if sala in (1,2,3):
                return sala-1
            else:
                os.system('cls')
            print('Sala não encontrada')
            continue
        except ValueError or TypeError:
            os.system('cls')
            print('Sala não encontrada')
            continue

def v_aluno():
    while True:
        aluno = input('Digite o nome do aluno: ')
        if not any(char.isdigit() for char in aluno):
            while True:
                cod_aluno = random.randint(1000,9999)
                if cod_aluno not in salas:
                    return {'nome': aluno, 'codigo':cod_aluno}
                else:
                    continue
        else:
            os.system('cls')
            print('Nome do aluno não pode conter números')
            continue
