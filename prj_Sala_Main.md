import os
from f_prjsala import v_aluno, v_opcao, v_sala
salas = [], [], []
validando_loop = True
validando_aluno = True

while validando_loop: #loop da main
    print('---------------------------------------')
    opcao = v_opcao() #verificando opção
    if opcao =='f': #finalizando programa
        os.system('cls')
        for i,item in enumerate(salas): #Listando salas depois do cadastro
            print(f'---Sala {i+1}---')
            if len(salas[i]) == 0:
                print('Sala Vazia')
            for j,item in enumerate(salas[i]):
                print(f'{j+1}.{item}')
        break
    sala = v_sala() #verificando sala
    if opcao == 'l': # listando salas 
        os.system('cls')
        print(f'---Sala {sala+1}---')
        if len(salas[sala]) == 0:
            print('Sala Vazia')
        for i,item in enumerate(salas[sala]): 
            print(f'{i+1}. {item}')
        continue
    aluno = v_aluno() #verificando aluno
    if opcao == 'i':
        salas[sala].append(aluno) #adicionando aluno a sala desejada
        os.system('cls')
        print(f'Aluno {aluno} adicionado a Sala {sala+1}')
    if opcao == 'a':
            if aluno in salas[sala]:
                salas[sala].remove(aluno) #removendo aluno da sala desejada
                continue
            else:
                os.system('cls')
                print('Aluno não encontrado')
                continue
