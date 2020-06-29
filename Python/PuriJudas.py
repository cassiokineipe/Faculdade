import random, time

#  Funções Gerais:          Usadas no jogo todo4
#  Integrantes do grupo: 
     # Guilherme Santiago Reis      RA: 31920918
     # Rafael Lua De Sousa e Silva  RA: 31948571
     # Cássio Kineipe da Costa      RA: 31929265
def Regras_Jogo(jogo_):
    if jogo_ == 'jogo':
        print(''' \n
Este é o menu principal!
Toda vez que um jogo terminar você vai ser direcionado para cá. 
Aqui é onde você escolhe os jogos para jogar.  \n \n
 --> Mecanismos do jogo em si:
Após a execução do programa, não será mais necessária a utilização do mouse, apenas o teclado.
O(s) jogo(s) em dupla tem a opção de joga-lo(s) novamente sem precisar voltar ao menu. \n
 --> Sobre os jogos:
Em caso de desistência, sai no meio, o jogo "pausa".
Caso deseje jogar um jogo ja escolhido novamente, ele vai retornar de onde parou.
Se já completou algum jogo, não tem como reinici-lo, aparecerá ele completo para você.
Toda vez que estiver no Menu sua pontuação é mostrada.   

Boa Sorte e bom jogo! :) \n  ''')
    time.sleep(5)
    
    if jogo_ == 'cruza':
        print('''Observações:                                                                                    
- Digite primeiro o número da coluna e depois a palavra.
- Caso queira parar de jogar no meio, basta escrever "DESISTO" na palavra.  \n ''' )
    time.sleep(3)

    Jogo_rodada = 0

def Apresentacao(esp,jogo):
    print ('{}===========================================   '   .format(esp) )                 #20     Cruzadinha - > Fácil    
    print ('{}=>                                       <=   '   .format(esp) )                 #22    Cruzadinha - > Dificil    
    print ('{}=>{}<=                                  '  .format(esp, jogo)  )                 #23    Caça-Palavras -> Dificl  
    print ('{}=>                                       <=   '   .format(esp) )                 #22    Caça-Palavras -> Fácil   
    print ('{}===========================================   '   .format(esp) )                 #05            Forca              

def Pontuação(num_acertos, num_erros):            #   Função para a pontuação
    global acertos, erros
    acertos = num_acertos
    erros = num_erros

def Espaco(n):                                    #   Função para printar espaços
    espaços = ['\n'] * n                          #   Printa de acordo com a quantidade
    for index in range(len(espaços)):
        print(espaços[index])

def Validar_Input (palavra_,lista1_,lista2_,texto1,texto2,texto3):
    global input_validado
    validar = False
    while validar == False:                                                                  #  Enquanto a validação for falsa.

        palavra_ = str(input('\n{} ' .format(texto1))).lower()                               #  Palavra para o jogo.

        if len(palavra_) == 0 or palavra_ == ' ':                                            #  Se apertar "enter" ou "espaço" não vale
            print('\n{} ' .format(texto2))

        for x in range (len(palavra_)):
            if palavra_[x] not in lista1_:                                                   #  Se não for uma letra não aceita
                print('{}\n ' .format(texto2)) 
                validar = False
                break
            if palavra_[x] in lista1_:                                                       #  Se a letra existe, validaçao é veridadeira
                validar = True
        
        if palavra_ in lista2_:
            print('{}\n ' .format(texto3))
            validar = False

    input_validado = palavra_

def Trofeus(comando):
    global trefeus_ganhos
    
    if comando == 'AddTrofeu':
        for index in range (4):                                     #          .__. 
            print(partes_trofeu[index])                             #         (|  |)
            quant_trofeu[index].append(partes_trofeu[index])        #          (  )  
        trefeus_ganhos += 1                                         #          _)(_  

    if comando == 'print':
        for lista_dentro in range(4):
            for parte_trofeu in range(len(quant_trofeu[lista_dentro])):
                print(quant_trofeu[lista_dentro][parte_trofeu], end = ' ')
            print('')
        


#  Funções para CRUZADINHA:

def Cruzadinha_Facil():     #                  Dicas ficam nessa coluna  <=|  | Aqui é definido pelo format as letras  
    Espaco(1)
    print('                          2.                                      ')
    print('      ----- ----- ----- ----- ----- ----- ----- -----          {} '  .format('DICAS:'))
    print('   1. | {} | | {} | | {} | | {} | | {} | | {} | | {} | | {} |     '         .format(Cf_1[0], Cf_1[1], Cf_1[2], Cf_1[3], Cf_1[4], Cf_1[5], Cf_1[6], Cf_1[7]))
    print('      ----- ----- ----- ----- ----- ----- ----- -----          {} '  .format('1. Resolve equações do segundo grau. '))
    print('                        | {} |                                    '         .format(Cf_2[1]))
    print('                        -----                                  {} '  .format('2. "Só sei que nada sei."'))
    print('                        | {} |                                    '         .format(Cf_2[2]))
    print('                        -----                                  {} '  .format('3. Área da biologia que estuda cruzamento de ervilha.'))
    print('                        | {} |                     5.             '         .format(Cf_2[3]))
    print('                        -----                   -----          {} '  .format('4. 3,14'))
    print('                        | {} |         4.        | {} |           '         .format(Cf_2[4], Cf_5[0]))
    print('                        -----       -----       -----          {} '  .format('5. Ácido Desoxirribonucleico.'))
    print('                        | {} |       | {} |       | {} |          '         .format(Cf_2[5], Cf_4[0], Cf_5[1]))
    print('      ----- ----- ----- ----- ----- ----- ----- -----             ')
    print('   3. | {} | | {} | | {} | | {} | | {} | | {} | | {} | | {} |     '         .format(Cf_3[0], Cf_3[1], Cf_3[2], Cf_3[3], Cf_3[4], Cf_3[5], Cf_3[6], Cf_3[7]))
    print('      ----- ----- ----- ----- ----- ----- ----- -----             ')
    print('                        | {} |                                    '         .format(Cf_2[7]))
    print('                        -----                                     ')
    Espaco(1)

def Cruzadinha_Dificil():   #                  Dicas ficam nessa coluna  <=|  | Aqui é definido pelo format as letras  
    Espaco(1)
    print('                          1.                      8.              ')
    print('                        -----                   -----          {} '  .format('DICAS:'))
    print('                        | {} |                   | {} |           '         .format(Cd_1[0], Cd_8[0]))
    print('                  ----- ----- ----- ----- ----- -----          {} '  .format('1. Mundo de blocos (jogo).'))
    print('               2. | {} | | {} | | {} | | {} | | {} | | {} |       '         .format(Cd_2[0], Cd_1[1], Cd_2[2], Cd_2[3], Cd_2[4], Cd_8[1]))
    print('                  ----- ----- ----- ----- ----- -----          {} '  .format('2. O segundo homem mais odiado da história.'))
    print('        3.          5.  | {} |                   | {} |           '         .format(Cd_1[2], Cd_8[2]))
    print('      ----- ----- ----- ----- -----             -----          {} '  .format('3. Estilo musical \ "Um Maluco no Pedaço".'))
    print('   4. | {} | | {} | | {} | | {} | | {} |             | {} |       '         .format(Cd_3[0], Cd_4[1], Cd_5[0], Cd_1[3], Cd_4[4], Cd_8[3]))
    print('      ----- ----- ----- ----- -----             -----          {} '  .format('4. "Why so serious ?" - Personagem. (em inglês).'))
    print('      | {} |       | {} | | {} |         7.        | {} |         '         .format(Cd_3[1], Cd_5[1], Cd_1[4], '#'))
    print('      -----       ----- -----       -----       -----          {} '  .format('5. Tablet para ler livros.'))
    print('      | {} |       | {} | | {} |       | {} |       | {} |        '         .format(Cd_3[2], Cd_5[2], Cd_1[5], Cd_7[0], Cd_8[5]))
    print('      -----       ----- ----- ----- -----       -----          {} '  .format('6. Lance sua sorte. '))
    print('      | {} |    6. | {} | | {} | | {} | | {} |       | {} |       '         .format(Cd_3[3], Cd_5[3], Cd_1[6], Cd_6[2], Cd_7[1], Cd_8[6]))
    print('      -----       ----- ----- ----- -----       -----          {} '  .format('7. Jogo que suga sua vida ou pior jogo que existe, tanto faz. :)'))
    print('                  | {} | | {} |       | {} |       | {} |         '         .format(Cd_5[4], Cd_1[7], Cd_7[2], Cd_8[7]))
    print('                  ----- -----       -----       -----          {} '  .format('8. O melhor vingador (em inglês).'))
    print('                  | {} | | {} |                                   '         .format(Cd_5[5], Cd_1[8]))
    print('                  ----- -----                                     ')
    Espaco(1)

def Colocar_letra(inicio, fim, lista):
    for index in range(inicio, fim):
        lista[index] = palavra[index]

def Acerto(lista_):
    global acertos, acertos_totais
    print('Uhuul, você achou uma palavra!')
    time.sleep(1)
    lista_.append(posicao)
    acertos_totais += 1
    acertos += 1


#  Funções para o CAÇA-PALAVRAS:

def Tabuleiro_CacaPalavras(num_palavras):
    print('''
      -------------------------------------------------- 
     | {0[00]}  {0[01]}  {0[02]}  {0[03]}  {0[04]}  {0[05]}  {0[06]}  {0[07]}  {0[08]}  {0[09]} | \n     |\t\t\t\t\t\t\t|  
     | {0[10]}  {0[11]}  {0[12]}  {0[13]}  {0[14]}  {0[15]}  {0[16]}  {0[17]}  {0[18]}  {0[19]} | \n     |\t\t\t\t\t\t\t|
     | {0[20]}  {0[21]}  {0[22]}  {0[23]}  {0[24]}  {0[25]}  {0[26]}  {0[27]}  {0[28]}  {0[29]} | \n     |\t\t\t\t\t\t\t|  
     | {0[30]}  {0[31]}  {0[32]}  {0[33]}  {0[34]}  {0[35]}  {0[36]}  {0[37]}  {0[38]}  {0[39]} | \n     |\t\t\t\t\t\t\t|  
     | {0[40]}  {0[41]}  {0[42]}  {0[43]}  {0[44]}  {0[45]}  {0[46]}  {0[47]}  {0[48]}  {0[49]} | \n     |\t\t\t\t\t\t\t|  
     | {0[50]}  {0[51]}  {0[52]}  {0[53]}  {0[54]}  {0[55]}  {0[56]}  {0[57]}  {0[58]}  {0[59]} | \n     |\t\t\t\t\t\t\t|  
     | {0[60]}  {0[61]}  {0[62]}  {0[63]}  {0[64]}  {0[65]}  {0[66]}  {0[67]}  {0[68]}  {0[69]} | \n     |\t\t\t\t\t\t\t|  
     | {0[70]}  {0[71]}  {0[72]}  {0[73]}  {0[74]}  {0[75]}  {0[76]}  {0[77]}  {0[78]}  {0[79]} | \n     |\t\t\t\t\t\t\t|  
     | {0[80]}  {0[81]}  {0[82]}  {0[83]}  {0[84]}  {0[85]}  {0[86]}  {0[87]}  {0[88]}  {0[89]} | \n     |\t\t\t\t\t\t\t|  
     | {0[90]}  {0[91]}  {0[92]}  {0[93]}  {0[94]}  {0[95]}  {0[96]}  {0[97]}  {0[98]}  {0[99]} |
      -------------------------------------------------- \n
                            Palavras achadas: {1}/{2} 
                                    Erros: {3}                ''' .format(pos, pal_achadas, num_palavras, erros) )

def Definindo_Palavra(palavra, comeco, fim, pulo):
    global index_palavra
    for posicao_ocupada in range (comeco, fim, pulo):
        pos[posicao_ocupada] = ' {} ' .format(palavra[index_palavra])
        index_palavra += 1
    index_palavra = 0

def Colocando_Palavra(palavra,lista_, comeco, fim, pulo):
    global index_palavra, pal_achadas, acertos_totais
    for posicao_ocupada in range (comeco, fim, pulo):
        pos[posicao_ocupada] = ':{}:' .format(palavra[index_palavra])
        index_palavra += 1
    
    if CacaF_rodada <= 1 and CacaD_rodada <= 1:
        print('Uhuul, você achou uma palavra!')
        lista_.append(palavra.lower())
        acertos_totais += 1
        time.sleep(1)

    pal_achadas += 1
    index_palavra = 0

def Colocando_random(num):
    for x in range(100):
        if num == 1:
            if pos[x] == ' ':
                pos[x] = ' {} ' .format(random.choice(alfabeto))
        else:
            pos[x] = ' {} ' .format(random.choice(alfabeto))

def Palavra_Certa(dificul_):
    global erros
    if dificul_ == '1':
        if palavra == 'basquete':
            Colocando_Palavra('BASQUETE',palavras_achadas[0],0, 7+1 ,1)

        elif palavra == 'tiro':
            Colocando_Palavra('TIRO',palavras_achadas[0],40, 43+1, 1)

        elif palavra == 'natação':
            Colocando_Palavra('NATAÇÃO',palavras_achadas[0],11, 77+1 ,11)

        elif palavra == 'atletismo':
            Colocando_Palavra('ATLETISMO',palavras_achadas[0],9, 89+1 ,10)

        elif palavra == 'triatlo' :
            Colocando_Palavra('TRIATLO',palavras_achadas[0],71,17-1,-9)
        
        elif palavra == 'vela':
            Colocando_Palavra('VELA',palavras_achadas[0],73,76+1,1)

        elif palavra == 'esgrima':
            Colocando_Palavra('ESGRIMA',palavras_achadas[0],97, 91-1,-1)

        else:
            print('Sorry baby, você errou!')
            erros += 1
            time.sleep(1)
            
    if dificul_ == '2':
        if palavra == 'assembly':
            Colocando_Palavra('ASSEMBLY',palavras_achadas[1], 37, 30-1, -1)

        elif palavra == 'python':
            Colocando_Palavra('PYTHON',palavras_achadas[1], 29, 74+1, 9)

        elif palavra == 'java':
            Colocando_Palavra('JAVA',palavras_achadas[1], 90, 93+1, 1)

        elif palavra == 'cobol':
            Colocando_Palavra('COBOL',palavras_achadas[1], 71, 31-1, -10)
        
        elif palavra == 'ruby':
            Colocando_Palavra('RUBY',palavras_achadas[1], 49, 79+1, 10)

        else:
            print('Sorry baby, você errou!')
            erros += 1
            time.sleep(1)


#  Funções para FORCA:

def Tabuleiro_Forca(d1, d2, d3):                                        #   Função para o desenho da forca.
    LetrasErradas()                                                             #  Mostra as letras erradas.
    print('\n ________________')                                                #  Parte horizontal da forca, onde fica a corda.
    print('{}\n{}\n{}\n|\n|\n|\n|' .format(d1, d2, d3))                         #  Corpo da forca e onde mostra o boneco.
    LinhaForca()                                                                #  Letras da palavra.
    print()

def LinhaForca():                                                       #   Função para as linhas da forca, da palavra.
    print('   ', end = '')                                                      # Espaço antes das linhas, para não ficar junto.
    for tam_palavra in range (len(palavra)):
        print(linha_forca[tam_palavra], end = ' ')  

def LetraForca():                                                       #   Função para trocar as letras
    global acertos, erros, verificar
    verificar = None

    for index_lista in range(len(palavra)):
        if palavra[index_lista] == letra:                               #  Se alguma letra da palvra for igual a letra..
            linha_forca[index_lista] = ' {} ' .format(letra.upper())    #  A linha se torna a letra
            verificar = True
            acertos += 1

    if verificar != True:                                                       #  Se não tiver a letra:                             
        letras_usadas.append(letra.upper())
        erros += 1
     
def LetrasErradas():                                                    #   Função para printar as letras erradas.
    for index in range(len(letras_usadas)):
        print(letras_usadas[index], end = ' - ')    



#           LISTAS DAs CRUZADINHAS:        
cruza_colunas = [['1','2','3','4','5'],['1','2','3','4','5','6','7','8']]
cruza_colunas_usadas = [ [] , [] ]

#  LISTAS DAS PALAVRAS - CRUZADINHA FACIL (Cf):
Cf_1 = [' '] * 8     #  Bhaskara   - 8 letras          #  Aqui cria um vetor, com espaços da cruzadinha em branco, do tamanho da quantidade de letras
Cf_2 = [' '] * 8     #  Sócrates   - 8 letras
Cf_3 = [' '] * 8     #  Genética   - 8 letras
Cf_4 = [' '] * 2     #  Pi         - 2 letras
Cf_5 = [' '] * 3     #  Dna        - 3 letras

#  LISTAS DAS PALAVRAS - CRUZADINHA DIFÍCIL (Cd):
Cd_1 = [' '] * 9     #  Minecraft  - 9 letras
Cd_2 = [' '] * 6     #  Hitler     - 6 letras
Cd_3 = [' '] * 4     #  Jazz       - 4 letras
Cd_4 = [' '] * 5     #  Joker      - 5 letras
Cd_5 = [' '] * 6     #  Kindle     - 6 letras
Cd_6 = [' '] * 4     #  Dado       - 4 letras
Cd_7 = [' '] * 3     #  Lol        - 3 letras
Cd_8 = [' '] * 8     #  Iron Man   - 8 letras



#           VARiÁVEIS DO CAÇA-PALAVRAS:  
pos = [' '] * 100

palavras_achadas = [ [] , [] ]
pal_achadas = 0

CacaF_rodada = 0
CacaD_rodada = 0
index_palavra = 0


#  Listas e variáveis gerais:
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç','ã','é','ó']

sim_nao = [['sim','s'],['não','nao','n'],'não','nao','n','sim','s']
dado_inválido = '\nDado inválido. Digite "sim" ou "nao".'

niveis = [['1','fácil','facil'],['2','dificil','difícil'],'1','2','difícil','dificil','fácil','facil','voltar']

jogos_sep = [['1','cruzadinha'],['2','caça-palavras','caça palavras'],['3','forca']]
comandos_menu = ['1','cruzadinha','2','caça-palavras','caça palavras','3','forca','sair','regras']

lista_vazia = []

partes_trofeu = ['  .__.   ' , ' (|  |)  ' , '  (  )   ' , '  _)(_   ']
quant_trofeu = [ [] , [] , [] , [] ]
trefeus_ganhos = 0

trofeus_juntos = '''
                     ___________         
                    '._==_==_=_.'        
                    .-\:      /-.        
                   | (|:.     |) |       
                    '-|:.     |-'        
                      \::.    /          
  .__.      .__.       '::. .'       .__.      .__.  
 (|  |)    (|  |)        ) (        (|  |)    (|  |) 
  (  )      (  )       _.' '._       (  )      (  )  
  _)(_      _)(_      `"""""""`      _)(_      _)(_   '''


validação = None                #   Usada para validação (das letras da forca e dos inputs)

acertos_totais = 0            #   Pontuação geral
erros_totais = 0
acertos = 0
erros = 0

cont = 0
Jogo_rodada = 0



Espaco(1)
Apresentacao('\t','       BEM-VINDO AO PURIJUDAS 3.0      ')
time.sleep(2)

comecar = input('\nPressione "enter" para começar: ')


comando = ''
while comando != 'sair':
    Pontuação(0,0)
    palavra = '' .lower()                                                                           #  Todos os jogos que precisão escrever uma palavra é usado esse input.

   # APRESENTAÇÃO DO JOGO: 
    if acertos_totais == 25 and cont == 1:
        print('!!!!!!! PARABÉNS !!!!!!!')
        time.sleep(2)
        print('Você conseguiu todos os troféus!!')
        time.sleep(2)
        print('Você é incrível!!!')
        time.sleep(2)
        print('Por causa disso, deixamos uma surpresa na sua sala de troféus!')
        time.sleep(4)
        print('Mas antes...')
        time.sleep(2)
        print('Nós, Guilherme Reis, Refael Lua e Cássio gostariamos de agradecer por ter jogado nosso jogo!')
        time.sleep(4)
        print('Espero que tenha gostado!!')
        time.sleep(3)
        print(':)')
        time.sleep(2)
        
        enter = input('Pressione enter para ir ao Menu Principal.')

    if Jogo_rodada != 0:
        Apresentacao('\t\t','              PURIJUDAS 3.0            ')
    Espaco(1)

    Apresentacao('\b','            MENU PRINCIPAL             ')
    
    if Jogo_rodada == 0 or comando == 'regras':                                                     #  Quando for a primeira vez no menu ou quando pedir as regras .
        Regras_Jogo('jogo')                                                                         #  Monstra as regras e informações do jogo.

    print('\n- Para sair/finalizar o programa, digite "sair"')
    if Jogo_rodada != 0:                                                                            #  Quando entra no Menu dps da primeira vez 
        print('- Para rever as regras, digite "regras".')                                           #  Mostra a opção de pedir as regras
    
    print('''\n\n
Escolha um dos jogos para jogar:                            Sua Pontuação:
  1 - Cruzadinha.                                                {}/25
  2 - Caça-Palavras.   
  3 - Forca  \n\n '''  .format(acertos_totais) )


    if trefeus_ganhos > 0:
        Apresentacao('\b','          SALA DOS TROFÉUS:            ')
        
        if trefeus_ganhos == 1 and cont == 0:
            print('\nParabéns, você conseguiu completar um jogo!')
            print('Você desbloqueou a sala de troféus!!')
            print('Aqui você pode ver suas conquistas ganha durante o jogo!!')
            cont += 1
        
        if acertos_totais != 25:
            Trofeus('print')
        else:
            print(trofeus_juntos)
    
    Espaco(1)
    time.sleep(2)

    if acertos_totais == 25 and cont == 1:
        print('\nTodos os jogos foram completados!')
        print('Caso selecione um deles, vai mostrar ele feito!')
        print('Você ainda pode jogar forca se quiser!\n\n')
        time.sleep(2)
        cont += 1

    comando = input('Comando: ').lower()

 # Enquanto não for um dos comandos mostrados..
    while comando not in comandos_menu:                                                             #  Validação de input
        comando = input('Comando inexistente. \nComando: ').lower()

    if comando == 'sair':                                                                           #  Se escolher sair, fecha o programa
        break

    elif comando != 'regras':                                                                       #  Se não pedir as regras, vai para um dos jogos selecionados

        while True:
            Espaco(5)

            ###     CRUZADINHA     ###
            if comando in jogos_sep[0]:

                print('\n\n\tJogo da Cruzadinha foi selecionado.\n')
                time.sleep(1.5)
                
                print('Caso deseja volta para o Menu principal, digite "voltar". \n')
                print('Nesse jogo há duas dificuldades:')
                print('  1 - Fácil. \n  2 - Difícil. \n  ')
                time.sleep(2)

                coman_Nivel = str(input('Escolha a dificuldade/comando?: ')).lower()
                
              # Enquanto não for um dos comandos mostrados..  
                while coman_Nivel not in niveis:                                                   #  Validação de input
                    coman_Nivel = str(input('Dado inválido. Escolha uma dificuldade: ')).lower()
                
                if coman_Nivel == 'voltar':                                                        #  Volta para o Menu
                    break
            
                Espaco(2)
            
                # Dificuldade Fácil.
                if coman_Nivel in niveis[0]:

                    Apresentacao('\t\t','          Cruzadinha - > Fácil         ') 
                    Espaco(1)

                    if len(cruza_colunas_usadas[0]) == 5:
                        print('\n\nVocê já completou esse jogo!')
                        print('Vou mostrar seu desempenho:')
                        time.sleep(3)
                        Cruzadinha_Facil()
                        enter = input('\nPressione "enter" para voltar ao menu. ')
                    
                    else:
                        Regras_Jogo('cruza')                                       # Mostra as instruções
                        
                        print('\nBoa Sorte!')
                        time.sleep(1.5)

                        Cruzadinha_Facil()                                         #  Chama o tabuleiro em branco.


                        while True:                                                

                            posicao = str(input('Fila/Coluna: ')).lower()
                        
                        # Enquanto não for uma coluna existente ou uma posição que ja foi usada..  
                            while posicao not in cruza_colunas[0] or posicao in cruza_colunas_usadas[0]:                        #  Validação de input
                                if posicao in cruza_colunas_usadas[0]:
                                    print('Posição já usada. \n')
                                else:
                                    print('Posição inexistente. \n')
                                
                                posicao = str(input('Fila/Coluna: ')).lower()
                                
                            
                            Validar_Input(palavra,alfabeto,palavras_achadas,'Palavra:','Palavra inválida','Palavra já usada')   #  Validação de input pela função
                            palavra = input_validado.upper()

                            if palavra == 'DESISTO':                               #  Caso a pessoa não queira mais jogar, ou parar no meio..
                                break

                            elif posicao == '1' and palavra == 'BHASKARA':         #  Se a palavra e a coluna forem corretas:
                                Colocar_letra(0, 8, Cf_1)                                #  As letras serão colocadas no local certo
                                Acerto(cruza_colunas_usadas[0])                          #  Posição ja foi usada e ganha um acerto

                            elif posicao == '2' and palavra == 'SOCRATES':
                                Colocar_letra(1, 6, Cf_2)
                                Cf_1[3] = 'S'
                                Cf_3[3] = 'E'
                                Cf_2[7] = 'S'
                                Acerto(cruza_colunas_usadas[0])

                            elif posicao == '3' and palavra == 'GENETICA':
                                Colocar_letra(0, 8, Cf_3)
                                Acerto(cruza_colunas_usadas[0])

                            elif posicao == '4' and palavra == 'PI':
                                Cf_4[0] = 'P'
                                Cf_3[5] = 'I'
                                Acerto(cruza_colunas_usadas[0])

                            elif posicao == '5' and palavra == 'DNA':
                                Colocar_letra(0, 2, Cf_5)
                                Cf_3[7] = 'A'
                                Acerto(cruza_colunas_usadas[0])

                            else:                                                  #  Se não forem iguais, ela erra (soma os erros)
                                print('Sorry baby, você errou')
                                erros += 1

                            Cruzadinha_Facil()                                     #  Chama o tabuleiro atualizado

                            if len(cruza_colunas_usadas[0]) == 5:
                                print('Parabéns!! Você conseguiu todas as palavras!!')
                                print('E melhor ainda, um troféu!! \o/ \a')
                                time.sleep(2)
                                Trofeus('AddTrofeu')
                                time.sleep(3)
                                break

                # Dificuldade Difícil.
                elif coman_Nivel in niveis[1]:

                    Apresentacao('\t\t','        Cruzadinha - > Difícil         ')
                    Espaco(2)

                    if len(cruza_colunas_usadas[1]) == 8:
                        print('\n\nVocê já completou esse jogo!')
                        print('Vou mostrar seu desempenho:')
                        time.sleep(3)
                        Cruzadinha_Dificil()
                        enter = input('\nPressione "enter" para voltar ao menu. ')

                    else:
                        print('Recomendação: \n- Caso não tenha feito, faça primeiro a dificuldade fácil. \n')
                        Regras_Jogo('cruza')

                        print('\nBoa Sorte!')
                        time.sleep(1.5)

                        Cruzadinha_Dificil()                                      #  Chama o tabuleiro em branco

                        while True:                                       #  Mesmo processo que a opção fácil, apenas muda as palavras
                            
                            posicao = str(input('Fila/Coluna: ')).lower()

                        # Enquanto não for uma coluna existente ou uma posição que ja foi usada..    
                            while posicao not in cruza_colunas[1] or posicao in cruza_colunas_usadas[1]:                        #  Validação de input
                                if posicao in cruza_colunas_usadas[1]:
                                    print('Posição já usada. \n')
                                else:
                                    print('Posição inexistente. \n')
                                
                                posicao = str(input('Fila/Coluna: ')).lower()    

                            Validar_Input(palavra,alfabeto,palavras_achadas,'Palavra:','Palavra inválida','Palavra já usada')   #  Validação de input pela função
                            palavra = input_validado.upper()

                            if palavra == 'DESISTO':                                #  Mesmo esquema que a dificuldade anterior.
                                break

                            elif posicao == '1' and palavra == "MINECRAFT":
                                Colocar_letra(0, 9, Cd_1)
                                Acerto(cruza_colunas_usadas[1])

                            elif posicao == '2' and palavra == "HITLER":
                                Colocar_letra(2, 5, Cd_2)
                                Cd_2[0] = 'H'
                                Cd_1[1] = 'I'
                                Cd_8[1] = 'R'
                                Acerto(cruza_colunas_usadas[1])

                            elif posicao == '3' and palavra == 'JAZZ':
                                Colocar_letra(0, 4, Cd_3)
                                Acerto(cruza_colunas_usadas[1])

                            elif posicao == '4' and palavra == 'JOKER':
                                Cd_3[0] = 'J'
                                Cd_4[1] = 'O'
                                Cd_5[0] = 'K'
                                Cd_1[3] = 'E'
                                Cd_4[4] = 'R'
                                Acerto(cruza_colunas_usadas[1])

                            elif posicao == '5' and palavra == 'KINDLE':
                                Colocar_letra(0, 6, Cd_5)
                                Acerto(cruza_colunas_usadas[1])
                            
                            elif posicao == '6' and palavra == 'DADO':
                                Cd_5[3] = 'D'
                                Cd_1[6] = 'A'
                                Cd_6[2] = 'D'
                                Cd_7[1] = 'O'
                                Acerto(cruza_colunas_usadas[1])

                            elif posicao == '7' and palavra == 'LOL':
                                Colocar_letra(0, 3, Cd_7)
                                Acerto(cruza_colunas_usadas[1])

                            elif posicao == '8' and palavra == 'IRON MAN' or palavra == 'IRONMAN':
                                palavra = 'IRON MAN'
                                Colocar_letra(0, 8, Cd_8)
                                Cd_8[4] = '#'
                                Acerto(cruza_colunas_usadas[1])
                            else:
                                print('Sorry baby, você errou')
                                erros += 1

                            Cruzadinha_Dificil()

                            if len(cruza_colunas_usadas[1]) == 8:
                                print('Parabéns!! Você conseguiu todas as palavras!!')
                                print('E melhor ainda, um troféu!! \o/ \a')
                                time.sleep(2)
                                Trofeus('AddTrofeu')
                                time.sleep(3)
                                break
                    
    

            ###    CAÇA-PALAVRAS   ###
            elif comando in jogos_sep[1]:

                print('\n\n\tJogo do Caça-Palavras foi selecionado\n')
                time.sleep(1.5)
                
                print('Caso deseja volta para o Menu principal, digite "voltar". \n')
                print('Nesse jogo há duas dificuldades:')
                print('  1 - Fácil. \n  2 - Difícil. \n  ')
                time.sleep(2)
                    
                coman_Nivel = str(input('Escolha a dificuldade/comando?: ')).lower()
                while coman_Nivel not in niveis:
                    coman_Nivel = str(input('Dado inválido. Escolha uma dificuldade: ')).lower()
                
                if coman_Nivel == 'voltar':
                    break

                Espaco(2)
                
                pal_achadas = 0

                # Dificuldade Fácil.
                if coman_Nivel in niveis[0]:
                    CacaF_rodada += 1 

                    Definindo_Palavra('basquete' ,0, 7+1 ,1)
                    Definindo_Palavra('tiro' ,40, 43+1, 1)
                    Definindo_Palavra('natação' ,11, 77+1 ,11)
                    Definindo_Palavra('atletismo' ,9, 89+1 ,10)
                    Definindo_Palavra('triatlo' ,71,17-1,-9)
                    Definindo_Palavra('vela' ,73,76+1,1)
                    Definindo_Palavra('esgrima' ,97, 91-1,-1)

                    if CacaF_rodada >= 1 and len(palavras_achadas[0]) > 0:
                        for x in range(len(palavras_achadas[0])):
                            palavra = palavras_achadas[0][x]
                            Palavra_Certa('1')

                    Colocando_random(1)

                    Apresentacao('\t\t','           Caça-Palavras Fácil         ')
                    time.sleep(2)
                    

                    if pal_achadas == 7:
                        print('\n\nVocê já completou esse jogo!')
                        print('Vou mostrar seu desempenho:')
                        time.sleep(3)
                        Tabuleiro_CacaPalavras(7)
                        enter = input('\nPressione "enter" para voltar ao menu. ')

                    else:
                        print('\n\nO Tema é: Esportes Olímpicos.')
                        print('Há 7 palavras espalhadas. ')
                        print('Observação: Uma das sete é mais difícil!! :) ')
                        print('Caso não queira mais jogar durante o jogo, basta escrever "desisto".')
                        time.sleep(4)

                        print ('\nBoa Sorte!')
                        time.sleep(2)

                        while True:
                            Espaco(2)
                            Tabuleiro_CacaPalavras(7)
                            
                            if pal_achadas == 7:
                                print('\n\nParabéns!! Você conseguiu achar todas as palavras!! \n')
                                print('E melhor ainda, um troféu!! \o/ \a')
                                time.sleep(2)
                                Trofeus('AddTrofeu')
                                time.sleep(3)
                                break

                            Validar_Input(palavra,alfabeto,palavras_achadas[0],'Palavra:','Palavra inválida','Palavra já encontrada')
                            palavra = input_validado.lower()

                            if palavra == 'desisto':
                                break

                            Palavra_Certa('1')
                        

                # Dificuldade Difícil.
                elif coman_Nivel in niveis[1]: 
                    CacaD_rodada += 1

                    Definindo_Palavra('assembly', 37, 30-1, -1)
                    Definindo_Palavra('python', 29, 74+1, 9)
                    Definindo_Palavra('java', 90, 93+1, 1)
                    Definindo_Palavra('cobol', 71, 31-1, -10)
                    Definindo_Palavra('ruby', 49, 79+1, 10)

                    if CacaD_rodada >= 1 and len(palavras_achadas[1]) > 0:
                        for x in range(len(palavras_achadas[1])):
                            palavra = palavras_achadas[1][x]
                            Palavra_Certa('2')
                    
                    Colocando_random(1)

                    Apresentacao('\t\t','          Caça-Palavras Difíil         ')
                    time.sleep(1.5)

                    if pal_achadas == 5:
                        print('\n\nVocê já completou esse jogo!')
                        print('Vou mostrar seu desempenho:')
                        time.sleep(3)
                        Tabuleiro_CacaPalavras(5)
                        enter = input('\nPressione "enter" para voltar ao menu. ')

                    else:
                        print ('\n\nO Tema é: Linguagens da programação. ')
                        print ('Há 5 palavras espalhadas. ')
                        print ('Lembrete: Aqui não existem linguagens de uma só letra. :) ')
                        print ('Caso não queira mais jogar durante o jogo, basta escrever "desisto". ')
                        time.sleep(4)
                        
                        print ('\nBoa Sorte!')
                        time.sleep(2)

                        while True:
                            Espaco(2)
                            Tabuleiro_CacaPalavras(5)
                            
                            if pal_achadas == 5:
                                print('\n\nParabéns!! Você conseguiu achar todas as palavras!! \n')
                                print('E melhor ainda, um troféu!! \o/ \a')
                                time.sleep(2)
                                Trofeus('AddTrofeu')
                                time.sleep(3)
                                break

                            Validar_Input(palavra,alfabeto,palavras_achadas[1],'Palavra:','Palavra inválida','Palavra já encontrada')
                            palavra = input_validado.lower()  

                            if palavra == 'desisto':
                                break

                            Palavra_Certa('2')
                
                pal_achadas = 0
                Colocando_random(2)


            ###        FORCA       ###
            elif comando in jogos_sep[2]:
 
                print('\n\n\tJogo da Forca foi selecionada\n')
                time.sleep(1.5)

                Espaco(2)
                Apresentacao('\t\t','                 FORCA                 ')

                print('\n\nATENÇÂO! Esse jogo não conta na sua pontuação')
                print('\n\nEsse jogo é necessário 2 ou mais jogadores. ')
                print('Um jogador vai escrever a palavra que deseja e os outros vão ter que adivinhar. ')
                print('O(s) outro(s) jogador(es) podem errar até 6 vezes\n')
                time.sleep(4)

                print('Vamos começar..')
                time.sleep(1.5)

                jogo_again = ''
                while jogo_again not in sim_nao[1]:
                    Pontuação(0,0)
                    
                    print('\nRegras: ')
                    print('- É permitido apenas uma palavra, sem espaço; ')
                    print('- A palavra não pode conter acento ou números; \n ')
                    print('Observação: Durante os ajustes serão feitas algumas perguntas, basta responder "sim" ou "não". \n ')
                    time.sleep(3)
                    

                    modi_palavra = ' '
                    while modi_palavra not in sim_nao[1]:
                        
                        Validar_Input(palavra,alfabeto,lista_vazia,'Digite a palavra para a forca:','Palavra inválida','Não vale acentos.')
                        palavra = input_validado.lower()  
                                    
                        print('\n\nA palavra digitada foi: ', palavra.upper())                                    #  Mostra a palavra escrita

                        modi_palavra = str(input('Deseja mudar/arrumar a palavra?: ')).lower()                    #  Caso queira mudar a palavra
                        while modi_palavra not in sim_nao:                                                        #  Enquanto não for "sim" ou "não" não aceita
                            modi_palavra = input('{} Deseja adicionar?: ' .format(dado_inválido)).lower() 


                    print('\n\nVocê pode adicionar uma dica. Ela vai aparecer a partir do 3º erro. ')

                    dica_talvez = input('Deseja adicionar?: ').lower()
                    while dica_talvez not in sim_nao:                                                             #  Enquanto não for "sim" ou "não" não aceita
                        dica_talvez = input('{} \nDeseja adicionar?: ' .format(dado_inválido)).lower()

                    dica = ' '                                                                                    #  Se não tiver dica, printa um espaço no lugar onde ficaria a dica.
                    dicaEtexto = lambda text: 'Dica: ' + text                                                     #  Se tiver dica, printa ela com o texto "Dica:"

                    if dica_talvez in sim_nao[0]:
                        texto = str(input('\nDica: '))
                        dica = dicaEtexto(texto)

                    Espaco(40)                                                                                    #   Pula 80 linhas (2*40), para "esconder" a palavra para não ver.

                    print('\nIniciando a Forca', end = '')
                    for x in range (1,4):
                        z = '.'
                        print(end = z)
                        time.sleep(1.5)
                    Espaco(1)

                    print('Boa Sorte!! \n\n')
                    time.sleep(1.5)
                                                                                  
                    linha_forca = ["___"] * len(palavra)                                                          #   Define a quantidade de linhas pela quantidade de letras da palavra.
                    letras_repetidas = []                                                                         #   Guarda as letras repetidas, para evitar repetição.
                    letras_usadas = []                                                                            #   Guarda todas as letras usadas.

                    cabeça =  "|               O        "                                                              # Partes do boneco:
                    pescoco=  "|               |        "    # Printa a dica na linha dos braços
                    bracoE =  "|              -|     {} "  .format(dica)                                                   #    O
                    bracoDE=  "|              -|-    {} "  .format(dica)                                                   #   -|-
                    pernaE =  "|              /         "                                                                  #   / \
                    pernaDE=  "|              / \       "


                    Tabuleiro_Forca('|','|','|')                                                                  #   Antes de começar mostra o jogo, o tabuleiro.

                    # Enquanto não acertar todas as letras:
                    while acertos != len(palavra):                                                                #   Começo do jogo.

                        letra = str(input('\n\nLetra: ')).lower()

                        while letra not in alfabeto or letra.upper() in letras_usadas or letra in letras_repetidas:     #  Verificando se é uma letra e se já foi usada.
                            letra = str(input('\nLetra repetida ou inválida. \nLetra:')).lower()
                        Espaco(1)
                        
                        letras_repetidas.append(letra)
                        LetraForca()                               

                    #  Se:  a letra existir  e  não tiver nenhum erro:
                        if verificar == True and erros <= 0:                                                      #  Quando acerta uma letra no início, o tabuleiro se manté o mesmo.
                            Tabuleiro_Forca('|','|','|')

                        if erros == 1:                                                                            #  Conforme os erros, vai adicionando as partes do boneco.
                            Tabuleiro_Forca(cabeça,'|','|')
                        elif erros == 2:
                            Tabuleiro_Forca(cabeça,pescoco,'|')
                        elif erros == 3:
                            Tabuleiro_Forca(cabeça,bracoE,'|')
                        elif erros == 4:
                            Tabuleiro_Forca(cabeça,bracoDE,'|')
                        elif erros == 5:
                            Tabuleiro_Forca(cabeça,bracoDE,pernaE)
                        elif erros == 6:
                            Tabuleiro_Forca(cabeça,bracoDE,pernaDE)
                            break                                                                                 #  Quando errar 6 vezes, quando o boneco estiver completo, o jpgo para.
                        
                        verificar == None
                        Espaco(6)
                
                    print('\n\nFIM DE JOGO') 
                    time.sleep(1)

                    if erros == 6:
                        print('   X_X    \n')
                        print('Você não conseguiu :/')
                        time.sleep(2)
                        print('A palavra era:', palavra.upper())
                        time.sleep(3)


                    elif acertos == len(palavra):
                        print('\n\nVocê Acertou! Parabéns :D\n')
                        time.sleep(2)

                    jogo_again = str(input('\n\nDeseja jogar forca de novo?: ')).lower()
                    while jogo_again not in sim_nao:                                                              #  Enquanto não for "sim" ou "não" não aceita
                        jogo_again = input('{} \nDeseja jogar forca de novo?: ' .format(dado_inválido)).lower()
                    time.sleep(2)

                if jogo_again in sim_nao[1]:
                    break

        #  Em caso de desistência..
            if palavra.upper() == 'DESISTO':
                Espaco(2)
                print('Poxa que pena que você desistiu. :/')
                time.sleep(2)
                print('Tenta de novo depois!! :)')
                time.sleep(3)
                break

            break

        Jogo_rodada += 1

        print('\n\nRedirecionando para o Menu', end = '')
        for x in range (3):
            z = '.'
            print(end = z)
            time.sleep(1.3)
        Espaco(4)

print('Obrigado por ter jogado! :)\n')
time.sleep(2)

print('O programa vai fechar em ', end = '')
for x in range (3,0,-1):
    print(end = '{}.. ' .format(x))
    time.sleep(1)
print(' ', end = '\r')