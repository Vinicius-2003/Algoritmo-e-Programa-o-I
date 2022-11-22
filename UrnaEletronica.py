def cadastro_cand(f,g,p): # No parametro , eu coloquei essas letras para "puxar" os assuntos de cada lista para fora
# mais facilmente. f = prefeito / g = governador / p = presidente
    pref = list()# aqui eu criei 3 listas, uma para cada cargo
    gov = list()
    pres = list()
    while True:
        cargo = input('A qual cargo ele disputará : ').upper()
        if cargo == 'PREFEITO': # eu coloquei esse if já para separar cada candidato em sua lista de acordo com o cargo.
            nome = input('Digite o nome do candidato : ').upper()
            pref.append(nome)
            num = int(input('Digite o número : '))
            pref.append(num)
            partido = input('Digite a qual partido ele pertence : ').upper()
            pref.append(partido)
            pref.append(0)
            f.append(pref)
            pref = list()
            continuar = input('Deseja continuar ? : ').upper()
            if continuar == 'SIM': 
                continue # caso a pessoa confirme, irá cadastrar outro candidato enquanto a pessoa continuar dizendo sim .
            else:
                break # caso contrário, irá quebrar o ciclo, e seguir para a proxima instrução fora do while. 
        elif cargo == 'GOVERNADOR':
            nome = input('Digite o nome do candidato : ').upper()
            gov.append(nome)
            num = int(input('Digite o número : '))
            gov.append(num)
            partido = input('Digite a qual partido ele pertence : ').upper()
            gov.append(partido)
            gov.append(0)
            g.append(gov)
            gov = list()
            continuar = input('Deseja continuar ? : ').upper()
            if continuar == 'SIM':
                continue
            else:
                break
        elif cargo == 'PRESIDENTE':
            nome = input('Digite o nome do candidato : ')
            pres.append(nome)
            num = int(input('Digite o número : '))
            pres.append(num)
            partido = input('Digite a qual partido ele pertence : ').upper()
            pres.append(partido)
            pres.append(0)
            p.append(pres)
            pres = list()
            continuar = input('Deseja continuar ? : ').upper()
            if continuar == 'SIM':
                continue
            else:
                break

prefeitos = list() # essas listas , quando eu chamar a função acima, vamo ocupar em ordem o local correspondente a cada letra do parametro 
# da função, dessa forma tudo que tiver "acoplado" em cada letra será adicionado a lista correspondente. 
governadores = list()
presidentes = list()


def pessoa(listapessoa):
    while True:
        nome = input('Insira seu nome : ').upper()
        cpf = input('Insira seu cpf : ')
        listaaux = list()
        listaaux.append(nome)
        listaaux.append(cpf)
        for i in range(3): # Nesse passo criei 3 valores falsos no local correspondentes a cada candidato
# Dessa forma, eu evito que uma mesma pessoa ao cadastra outra, vote duas vezes.Sem esse mecanismos possibilitaria uma "fraude" eleitoral.  
            listaaux.append(False)
        listapessoa.append(listaaux)
        continuar = input('Deseja continuar ? : ').upper()
        if continuar == 'SIM':
            continue
        else:
            break

eleitores = list() # criei uma lista para guardar os dados do eleitor cadastrado. 


def votar(b,n,e,tot): # Eu utilizei a mesma estratégia que na primeira função. Sendo:
# b = brancos / n = nulos / e = eleitores / tot = total de votos
    for y in e:
        print('É a vez de {} / {} votar!'.format(y[0],y[1])) # Quando houver mais de uma pessoa cadastrada, o for vai repetir as opções abaixo 
# até que todas as pessoas tenha votado. 
        print('Ordem de votação : \033[4;33mPREFEITO / GOVERNADOR / PRESIDENTE\033[m')
        podeBreak1 = False # Cada podeBreak será utilizado para confirmar o voto de cada cargo
# Ou seja, enquanto houver candidatos "votáveis" e o eleitor não votar, não sairá daquele cargo até que o mesmo vote.
# Dessa forma eu obrigo o eleitor a votar para aquele cargo, e tenho certeza que todos os votos serão validos. 
        podeBreak2 = False # O primeiro break é para os prefeitos, o segundo para governadores e o terceiro para presidente.
        podeBreak3 = False 
        if y[2] == False:
            if len(prefeitos) != 0: # Aqui enquanto o número de prefeitos cadastrado for diferente de 0, ficará disponível para o eleitor votar.
                while True:
                    if podeBreak1 == True: # Nessa parte, o sistema verifica se a pessoa da vez a votar , já votou nesse cargo ou não. 
                        break # Caso ela já tenha, o break faz o sistema sair dessa while e continuar.
                    num1 = int(input('Digite o número do \033[1:32mPrefeito\033[m : '))
                    for p in prefeitos:
                        if num1 == -1: 
                            confirma = input('Seu voto foi marcado \033[1;30mbranco\033[m. confirma? (\033[32msim\033[m/\033[31mnão\033[m): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                b[0] +=1 # aqui serve para contabilizar os votos em branco, adicionando-o na primeira posição de uma lista criada.
                                # Visto que a posição 2 é para quem votar branco em governador e a terceira para brancos no presidente.
                                tot[0] += 1 # Soma-se um a uma lista que está contabilizando a quantidiade de votos. 
                                y[2] = True # Na lista de dados do eleitor a 2,3 e 4 espaços são para guardar os votos
                                # Nesse caso 2 posição representa o prefeito, e como o voto foi confirmado, o valor passa a ser True,
                                # evitando que a pessoa vote de novo.
                                podeBreak1 = True #Com o voto confirmado, o sistema sai do primeiro if e segue. 
                                break
                        elif num1 ==-2: # Caso o eleitor vote nulo
                            confirma = input('Seu voto foi marcado nulo. confirma? (\033[32msim\033[m/\033[31mnão\033[m): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                n[0] +=1 # Criei uma lista para agregar os valores  nulos referentes a cada cargo. 
                                y[2] = True
                                tot[0] += 1
                                podeBreak1 = True
                                break
                        if p[1] == num1: # Caso o valor digitado pelo usuário for igual ao valor do número que ocupa a 2ª posição de cada candidato a prefeito
                            # o sistema irá pegar todos os dados daquele candidato com o mesmo número digitado. 
                            confirma = input('{} esse é o seu candidato? (\033[32msim\033[m/\033[31mnão\033[m) : '.format([p])).upper() # caso o valor digitado corresponder ao valor digitado pelo usuário
                            # O sistema printa os dados daquele candidato e pede uma confirmação ao eleitor. 
                            if confirma =='SIM':
                                y[2] = True
                                p[3] += 1 
                                tot[0] += 1
                                print(tot)
                                print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                podeBreak1 = True
                                break
            else: # Caso não haja nenhum prefeito cadastrado, o sistema mostra essa mensagem  pula para o próximo cargo. 
                print('\033[0;31mNão há nenhum Prefeito cadastrado!\033[m')
        else: # Caso uma pessoa já tenha votado e cadastrou outra eleitor, para que essa pessoa não vote de novo, aparecerá essa mensagem.
            print('\033[0;32mEssa pessoa já votou!!\033[m')
        if y[3] == False: # Caso o eleitor ainda não tenha votado em nenhum governador.  
            if len(governadores) != 0:
                while True:
                    if podeBreak2 == True: # Quando a pessoa tivr votado, quebra o while. 
                        break
                    num2 = int(input('Digite o número do \033[1:32mGovernador\033[m : '))
                    for g in governadores: # Esse for vai percorrer apenas as sub-listas dos governadores, facilitando a procura do candidato.
                        if num2 == -1:
                            confirma = input('Seu voto foi marcado \033[1;30mbranco\033[m. confirma? (\033[32msim\033[m/\033[31mnão\033[m): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                b[1] +=1
                                y[3] = True
                                tot[1] += 1
                                podeBreak2 = True
                                break
                        elif num2 == -2:
                            confirma = input('Seu voto foi marcado nulo. confirma? (\033[32msim\033[m/\033[31mnão\033[m): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                n[1] += 1
                                y[3] = True
                                tot[1] += 1
                                podeBreak2 = True
                                break
                        if g[1] == num2:
                            confirma = input('{} esse é o seu candidato? (\033[32msim\033[m/\033[31mnão\033[m) : '.format([g])).upper()   
                            if confirma == 'SIM':
                                y[3] = True
                                g[3] += 1
                                tot[1] += 1
                                print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                podeBreak2 = True
                                break
            else:
                print('\033[0;31mNão há nenhum Governador cadastrado!\033[m')
        else:
            print('\033[0;32mEssa pessoa já votou!!\033[m')
        if y[4] == False:
            if len(presidentes) != 0:
                while True:
                    if podeBreak3 == True:
                        break
                    num3 = int(input('Digite o número do \033[1:32mPresidente\033[m : '))
                    for pres in presidentes:
                        if num3 == -1:
                            confirma = input('Seu voto foi marcado \033[1;30mbranco\033[m. confirma? (\033[32msim\033[m/\033[31mnão\033[m): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                b[2] +=1
                                y[4] = True
                                tot[2] += 1
                                podeBreak3 = True
                                break
                        elif num3 ==-2:
                            confirma = input('Seu voto foi marcado nulo. confirma? (\033[32msim\033[m/\033[31mnão\033[m): ').upper()
                            if confirma =='SIM':
                                print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                n[2] +=1
                                y[4] = True
                                tot[2] += 1
                                podeBreak3 = True
                                break
                        else:
                            if pres[1] == num3:
                                confirma = input('{} esse é o seu candidato? (\033[32msim\033[m/\033[31mnão\033[m) : '.format([pres])).upper()   
                                if confirma == 'SIM':
                                    y[4] = True
                                    pres[3] += 1
                                    tot[2] += 1
                                    print('Seu voto foi confirmado \033[36m{}\033[m!'.format(y[0]))
                                    podeBreak3 = True
                                    break
            else:
                print('\033[0;31mNão há nenhum Presidente cadastrado!\033[m')
        else:
            print('\033[0;32mEssa pessoa já votou!!\033[m')

total = [0,0,0] # Aqui eu criei as listas para armazenar os votos em branco, nulos e o total de votos.
votoembranco = [0,0,0] # cada zero na 1ª casa representa o cargo de prefeito, o 2º de governador e o 3º de presidente.
votonulo = [0,0,0]


def apurar_resulpref(prefeitos): # Criei uma função para apurar e organizar  os resultados do mais votado para o menos de cada candidato.
    for i in range(len(prefeitos)-1): # Essa lista não vai até o final, para que a lista debaixo possa verificar o ultimo valor com o penultimo.
        for j in range(i+1, len(prefeitos)): # Por esse motivo, a contagem de bloco está um valor a frente do i, para comparar o "de tras "
            # que é o valor de i com o "da frente" que é o valor de j
            if prefeitos[i][3]< prefeitos[j][3]: # caso o valor de i for menor que o de j em questão de votos 
                prefeitos[i],prefeitos[j] = prefeitos[j],prefeitos[i] # o valor de i troca de posição com de j, organizando assim a lista.
    print('\033[0;33mRanking de Prefeitos!\033[m')
    if prefeitos[0][3] > prefeitos[1][3]:
        print('\033[0;32m{}\033[m é o novo prefeito eleito!'.format(prefeitos[0]))
    elif prefeitos [0][3] == prefeitos [1][3]:
        print('Houve um empate entre {} e {} !'.format(prefeitos[0],prefeitos[1]))
    for a in range(len(prefeitos)): #Esse for vai printar a lista de prefeitos do maior para o menor, mostrando os dados da votação.
        print('-=-'*30)
        #print('\033[0;33mRanking de Prefeitos!\033[m')
        print('{}: {} | {} | Total de votos: {} ' .format(a+1,prefeitos[a][0],prefeitos[a][2],prefeitos[a][3]))
        print('-=-'*30)
        print('Total de votos = {}'.format(total[0]))
        print('-=-'*30)
        print('Total de brancos = {}'.format(votoembranco[0]))
        print('-=-'*30)
        print('Total de nulos = {}'.format(votonulo[0]))
        
        
def apurar_resulgov(governadores): #Serve para o mesmo propósito da função dos prefeitos acima.
    for i in range(len(governadores)-1): 
        for j in range(i+1, len(governadores)):
            if governadores[i][3]< governadores[j][3]:
                governadores[i],governadores[j] = governadores[j],governadores[i]
    print('\033[0;33mRanking de Governadores!\033[m')
    if governadores[0][3] > governadores[1][3]:
        print('\033[0;32m{}\033[m é o novo prefeito eleito!'.format(governadores[0]))
    elif governadores [0][3] == governadores [1][3]:
        print('Houve um empate entre {} e {} !'.format(governadores[0],governadores[1]))
    for a in range(len(governadores)):
        print('-=-'*30)
        print('{}: {} | {} | Total de votos: {} ' .format(a+1,governadores[a][0],governadores[a][2],governadores[a][3]))
        print('-=-'*30)
        print('Total de votos = {}'.format(total[1]))
        print('-=-'*30)
        print('Total de brancos = {}'.format(votoembranco[1]))
        print('-=-'*30)
        print('Total de nulos = {}'.format(votonulo[1]))
        
        
def apurar_resulpres(presidentes): # Conseuqnetemente serve para também organizar, só que dessa vez o valor dos candidatos a presidência. 
    for i in range(len(presidentes)-1):
        for j in range(i+1, len(presidentes)):
            if presidentes[i][3]< presidentes[j][3]:
                presidentes[i],presidentes[j] = presidentes[j],presidentes[i]
    print('\033[0;33mRanking de Presidentes!\033[m')
    if presidentes[0][3] > presidentes[1][3]:
        print('\033[0;32m{}\033[m é o novo prefeito eleito!'.format(presidentes[0]))
    elif presidentes [0][3] == presidentes [1][3]:
        print('Houve um empate entre {} e {} !'.format(presidentes[0],presidentes[1]))
    for a in range(len(presidentes)):    
        print('{}: {} | {} | Total de votos: {} ' .format(a+1,presidentes[a][0],presidentes[a][2],presidentes[a][3]))
        print('-=-'*30)
        print('Total de votos = {}'.format(total[2]))
        print('-=-'*30)
        print('Total de brancos = {}'.format(votoembranco[2]))
        print('-=-'*30)
        print('Total de nulos = {}'.format(votonulo[2]))



def estatisticas(eleitores):
    eleitores.sort() # Aqui serve para organizar o nome e o cpf dos todos os eleitores cadastrado que votaram. 
    for i in range(len(eleitores)):
        print(eleitores[i][0:2])



while True:
    menu = print('''
    ============MENU==============
    \033[34m1. Cadastrar Candidatos\033[m
    \033[34m2. Cadastrar Eleitores\033[m
    \033[34m3. Votar\033[m
    \033[34m4. Apurar Resultados\033[m
    \033[34m5. Relatório e Estatísticas\033[m
    \033[34m6. Encerrar\033[m
    ==============================''')
    menu_escolha = int(input('Digite o valor desejado : '))
    if menu_escolha == 1:
        cadastro_cand(prefeitos,governadores,presidentes)
        print(prefeitos)  
        print(governadores)
        print(presidentes)
    elif menu_escolha == 2:
        pessoa(eleitores)
        print(eleitores)
    elif menu_escolha == 3:
        votar(votoembranco,votonulo,eleitores,total)
    elif menu_escolha == 4:
        apurar_resulpref(prefeitos)
        apurar_resulgov(governadores)
        apurar_resulpres(presidentes)
    elif menu_escolha == 5:
        estatisticas(eleitores)
    elif menu_escolha == 6:
        print('desligando urna...')
        break
