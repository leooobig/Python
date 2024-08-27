import os
from variavelsalas import salas
from f_prjsala import v_aluno, v_opcao,v_sala
validando_loop = True

while validando_loop: #loop da main
    print('---------------------------------------')
    opcao = v_opcao() #verificando opção
    if opcao =='f': #finalizando programa
        os.system('cls')
        for i,item in enumerate(salas): #Listando salas depois do cadastro
            print(f'---Sala {i+1}---')
            if len(salas[i]) == 0:
                print('Sala Vazia')
            for j,aluno in enumerate(salas[i]):
                print(f'{j+1}. {aluno['nome']} #{aluno['codigo']}')
        break

    sala = v_sala() #verificando sala
    if opcao == 'l': # listando salas 
        os.system('cls')
        print(f'---Sala {sala+1}---')
        if len(salas[sala]) == 0:
            print('Sala Vazia')
        for i,aluno in enumerate(salas[sala]): 
            print(f'{i+1}. {aluno['nome']} #{aluno['codigo']}')
        continue
    
    aluno = v_aluno() #verificando aluno
    if opcao == 'i':
        os.system('cls')
        salas[sala].append(aluno) #adicionando aluno a sala desejada
        os.system('cls')
        print(f'Aluno {aluno["nome"]} #{aluno["codigo"]} adicionado a Sala {sala+1}')

    if opcao == 'a':
         for i in salas[sala]:
            if i['nome'] == aluno['nome']:
                salas[sala].remove(i)
                os.system('cls')
                continue
