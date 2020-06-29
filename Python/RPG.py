
    
#  Trabalho de Algorítmo e Programação I - 1º semestre (2019)

#  Integrantes do grupo: 
     # Guilherme Santiago Reis      RA: 31920918
     # Rafael Lua De Sousa e Silva  RA: 31948571
     # Cássio Kineipe da Costa      RA: 31929265

#Bibliotecas usadas:

import random
import time

pontuação_jogo = 0

n = (1,2,3,4,5,6,7,8,9,10,11,12)

d12 = random.choice(n)

#Nome do jogo:

print ('**************************************')
print ('*                                    *')
print ('*      Belli Orbis Terrarum II       *')
print ('*              (BOT II)              *')
print ('*                                    *')
print ('**************************************')
print ('\n \n')

print ('Você está em uma nação que está em guerra.')
print ('De um lado existe os Soyouz e algumas tribos aliadas, e do outro os Poros, também com suas alianças. \n')
print ('Os Poros são uma tribo que, de acordo com eles, estão com o seu país vulnerável para ameaças por causa dos Yahudis, uma tribo que estaria enfraquecendo a cidade e afetando o comércio.')
print ('Como alternativa, os Poros passaram a invadir outras terras para recompensar as perdas causadas pelos Yahudis.')
print ('Uma das terras invadidas era aliada dos Soyouz \n')
print ('Por serem uma tribo orgulhosa e ambiciosa, como resposta a esse ataque, começaram uma guerra contra os Poros. \n')
print ('Voce é um comandante.')
print ('Deseja ser o comandante do exército Soyouz (1), atacando brutalmente os Poros')
print ('Ou deseja ser comandantes dos Poros (2) ajudando-os na defesa de su país? \n')

exercito_barco = 0
exercito_arqueiros = 0
exercito_guerreiros = 0

mortes = 0

while True:
        escolha_lado = input('Digite sua escolha (1 ou 2): ')

        if escolha_lado == '1':

                exercito_barco = exercito_barco + 50
                exercito_arqueiros = exercito_arqueiros + 1500 
                exercito_guerreiros = exercito_guerreiros + 3000      

                print ('Parabéns, você é o comandante da tribo Soyouz.')
                time.sleep(2)
                print ('Agora você tem como objetivo vencer essa guerra com o menor número de baixas ao seu lado')
                time.sleep(2)
                print ('Para atingir seu objetivo, de invadir Poros, você precisa: \n')
                time.sleep(2)
                print ('- Atravessar a ponte que divide as duas tribos; \n- Invadir a tribo mais próxima \n- E, finalmente, invadir Poros')
                time.sleep(2)

                ######   Batalha 1   ######

                print ('Sua primeira batalha vai começar: \n')
                time.sleep(3)
                print ('Você deve atravessar a ponte.')
                time.sleep(3)
                print ('A invasão pode ser pela água e/ou pela própria ponte.')
                time.sleep(3)
                print ('Você tem disponível: \n')
                time.sleep(3)
                print ('- 50 barcos com 35 guerreiros em cada; \n- 3000 guerreiros; \n- 1500 arqueiros; \n')
                time.sleep(3)
                print ('Você tem direito a escolher apenas duas das três tropas disponíveis; \n')
                time.sleep(3)
                print ('55% - (1) Barcos e Arqueiros; \n70% - (2) Barcos e Guerreiros; \n30% - (3) Guerreiros e Arqueiros;')
                print ('As "%" indicam a probabilidade de ganho. \n') 

                print ('LEMBRE-SE QUE: cada escolha sua tem uma pontuação')       
                time.sleep(2)
                
                while True: 
                        escolha_tropas = input ('Esolha as tropas que deseja: ', )
                
                        if escolha_tropas == '1':
                                mensagem_ataque = 'Barcos atiram com seus canhões, sempre mirando na destruição de seus oponentes.'
                                mensagem_vitoria = 'Parabéns pela sua vitória comandante.'
                
                                pontuação_jogo = pontuação_jogo + 20 
                                break
                        
                        elif escolha_tropas == '2':
                                mensagem_ataque = 'Barcos atiram com seus canhões, sempre mirando na destruição de seus oponentes'
                                mensagem_vitoria = 'Você ganhou com uma vitória esmagadora, parabéns comandante'

                                pontuação_jogo = pontuação_jogo + 15
                                break
                        
                        elif escolha_tropas == '3':
                                mensagem_ataque = 'Seus guerreiros e arqueiros estâo em sintonia, com foco em destruir os inimigos'
                                mensagem_vitoria = 'Parabéns comandante, foi por pouco, mas vc conseguiu'

                                pontuação_jogo = pontuação_jogo + 10
                                break

                        else:
                                print('Por favor, digite uma das opções: 1, 2 ou 3')
                
                print ('O dado usado será um D8 (oito lados) \n')
                time.sleep(2)
                print ('As tropas estão prontas em suas respectivas posições, esperando o seu comando para atacarem.')
                time.sleep(2)

                comando_b1 = input('Digite seu comando (seu comanado para atacar (qualquer coisa rs)): ', )
                time.sleep(2)

                print ('\nA batalha começou. \n')
                time.sleep(2)
                print ('Os Poros estão defendendo seu território com muitos arqueiros e inúmeros guerreiros.')
                time.sleep(2)
                print ('Flechas de fogo voam pelo território, apenas buscando uma vítima para incendiar.')
                time.sleep(3)
                print ('O som das espadas se chocando ressoa pela cidade, espalhando o medo e terror por todos os lados.')
                time.sleep(3)
                print (mensagem_ataque,'\n')
                time.sleep(3)
                print ('O dado vai ser lançado..')
                time.sleep(2)

                dado_b1 = input('Jogue o dado (jogar): ', )

                print('Dado = 7')
                time.sleep(2)
                print ('Depois de árduas horas de batalha..')
                time.sleep(2)
                print ('Seu exército consegue avançar e conquistar a ponte!!! \n')
                time.sleep(2)
                print (mensagem_vitoria, '\n')
                time.sleep(3)
                print ('Nessa batalha:')
                time.sleep(2)

                if escolha_tropas == '1':
                        print ('Restaram: 1050 guerreiros (30 barcos) e 1100 Arqueiros')
                        mortes = mortes + 700 + 400
                        print ('E você teve:', mortes, 'mortes' '\n')
                elif escolha_tropas == '2':
                        print ('Restaram: 1050 guerreiros (30 barcos) e 1200 Guerreiros')
                        mortes = mortes + 700 + 1800
                        print ('E você teve:', mortes, 'mortes' '\n')
                else:
                        print ('Restaram: 1100 Arqueiros e 1200 Guerreiros')
                        mortes = mortes + 400 + 1800
                        print ('E você teve:', mortes, 'mortes' '\n')
                
                print ('Seus guerreiros estâo felizes junto com você \n')
                time.sleep(2)
                print ('Pela noite: parte deles comemoram a vitória, mas aluguns ficam de luto pela perda de seus companheiros. \n \n')
                time.sleep(2)
                print ('Passaram-se alguns dias.. \n')
                time.sleep(3)
                print ('Você e sua tropa marcham em direção a cidade vizinha de Poros, o caminho mais fácil para chegar em Poros. \n \n')
                time.sleep(2)

                ######      Batalha 2     ######

                print ('INÍCIO DA BATALHA 2: \n')
                time.sleep(2)
                print ('Você chegou no campo de batalha.')
                time.sleep(2)
                print ('Você precisa decidir como organizar as suas tropas!!')
                time.sleep(2)
                print ('O terreno é reto com árvores nas laterais. \n')
                time.sleep(2)
                print ('Você tem duas opções:')
                time.sleep(2)

                print ('1 - Dividir suas tropas, colocando parte para atacar no meio e a outra parte pela lateral.')
                print ('2 - Manter suas tropas juntas, atacando pelo meio.')
                print ('A primeira tem 65% de vitória e a segunda tem 55%.')
                time.sleep(2)

                while True:
                        escolha_estrategia_b2_1 = input('Qual a sua decisão ??: ', )

                        if escolha_estrategia_b2_1 == '1':
                                pontuação_jogo = pontuação_jogo + 20
                                break
                
                        elif escolha_estrategia_b2_1 == '2':
                                pontuação_jogo = pontuação_jogo + 10
                                break

                        else:
                                print('Por favor, digite uma das opções: 1 ou 2')

                print ('Boa estratégia comandante!! \n')
                time.sleep(2)
                print ('A tropa inimiga também está se preparando do outro lado. \n')
                time.sleep(2)
                print ('Suas tropas já estão posicionadas como disse, eles estâo á espera do seu comando!!!! \n')
                time.sleep(2)

                comando_b2 = input('Digite seu comando: ', )

                print ('A batalha começou!!!! \n \n')
                time.sleep(2)
                print ('Você dá uma olhada geral e percebe que o lado inimigo tem menos pessoas do que vc imaginou!!')
                time.sleep(2)
                print ('Seus guerreiros estão fervorozos \n')
                time.sleep(2)
                print ('Nessa batalha o dado utilizado será o D10 (dez lados) \n')
                time.sleep(2)
                print ('O dado vai ser lançado...')
                time.sleep(2)

                dado_b2 = input('Jogue o dado (jogar): ', )

                print('Dado = 4 \n')
                time.sleep(2)
                print ('A batalha teve um caminho.. \n')
                time.sleep(2)
                print ('Você percebe que o inimigo está levando a batalha para o lado deles, para uma floresta do outro lado.')
                time.sleep(2)
                print ('Você já está quase ganhando.. \n')
                time.sleep(3)
                print ('1 - Você deseja finalizar com eles seguindo-os até a floresta?')
                print ('2 - Ou deseja se manter no compo de batalha??')

                while True:
                        escolha_estrategia_b2_2 = input('Escolha o que deseja fazer: ', )

                        if escolha_estrategia_b2_2 == '1':
                                print ('Você diz para as suas tropas para seguir eles e acabar com eles de vez.')
                                time.sleep(2)
                                print ('Seus guerreiros começam a ir atrás deles. \n')
                                time.sleep(2)

                                pontuação_jogo = pontuação_jogo + 20
                                break
                        elif escolha_estrategia_b2_2 == '2':
                                print ('Suas tropas começam a cantar vitória!!')
                                time.sleep(2)
                                print ('Todos estâo felizes. \n')
                                time.sleep(2)

                                pontuação_jogo = pontuação_jogo = 15
                                break
                        else:
                                print('Por favor, digite uma das opções: 1 ou 2')

                print ('Porém acontece um imprevisto.. \n')
                time.sleep(2)
                print ('Suas tropas começam a ser atacada por todos os lados..')
                time.sleep(2)
                print ('As tropas inimigas conseguiram reforços e você não contava com isso')
                time.sleep(3)
                print ('Suas tropas começam a morrer consideravelmente!!!')
                time.sleep(2)
                print ('Você precisa sair do campo rápido para evitar uma massacre total e também se salvar!! \n')
                time.sleep(2)
                print ('Seu conselheiro pergunta o que você deseja fazer: \n')
                print ('1 - Recua e tente uma nova estratégia, possívelmente com mais soldados pedindo para as outras tribos.')
                print ('95% de chance de sair vivo e salvando as tropas restantes.')
                print ('2 - Se mantém orgulhoso e continua a batalha.')
                print ('20% de chance de sair vivo e de salvar suas tropas')

                while True:
                        escolha_estrategia_b2_3 = input('Digite sua escolha: ', )

                        if escolha_estrategia_b2_3 == '1':
                                print ('Você foi muito sábio!!')
                                time.sleep(2)
                                print ('Você conseguiu se salvar e também parte de suas tropas. \n')
                                time.sleep(2)

                                pontuação_jogo = pontuação_jogo + 20
                                break
                        elif escolha_estrategia_b2_3 == '2':
                                print ('Você se deixou levar pela sua ignorância!!')
                                time.sleep(2)
                                print ('Seu conselheiro passou a ordem de retira em lugar e te tirou da força \n')
                                time.sleep(2)

                                pontuação_jogo = pontuação_jogo + 5
                                break
                        else:
                                print('Por favor, digite uma das opções: 1 ou 2')

                print ('Nessa última batalha você perdeu muitos homens.. \n')
                time.sleep(2)

                if escolha_tropas == '1':
                        print ('Restaram: 900 guerreiros')
                        mortes = mortes + 600 + 650
                elif escolha_tropas == '2':
                        print ('Restaram: 900 guerreiros')
                        mortes = mortes + 600 + 800
                else:
                        print ('Restaram: 500 arqueiros e 400 guerreiros.')
                        mortes = mortes + 650 + 800

                print ('Número de mortes até agora: ', mortes, '\n')
                time.sleep(2)
                print ('Mesmo com essa derrota nâo significa que você perdeu a guerra. \n \n')
                time.sleep(2)
                print ('Algumas tribos aliadas enviaram tropas de suporte para te ajudar na próxima batalha')
                time.sleep(2)
                print ('Você não conseguiu pelo caminho fácil, a cidade vizinha, mas tem o outro lado: pelas montanhas')
                time.sleep(2)
                print ('Com o suporte você passa a ter: 1200 arqueiros e 1400 guerreiros \n')
                time.sleep(2)
                
                ######      Batalha 3     ######

                print ('A próxima batalha será a mais díficl:')
                time.sleep(2)
                print ('Você vai atacar Polos diretamente porém o números de tropas são praticamente iguais.')
                time.sleep(2)
                print ('Você tem duas opções de estrategia:')
                time.sleep(2)
                print ('1 - Esperar escurecer para fazer um ataque silencioso.')
                print ('2 - Mandar todos os seus guerreiros para um ataque surpresa a luz do dia.')
                print ('Em ambas as escolhas voce tem 50% de chance de exito')

                while True:
                        escolha_estrategia_b3_1 = input('Qual estratégia deseja usar?: ', )

                        if escolha_estrategia_b3_1 == '1' or '2':
                                print('Exelente estratégia!!!')
                                break
                        else:
                                print('Por favor, digite uma das opções: 1 ou 2')

                print ('Suas tropas já estão posicionadas como disse, eles estâo á espera do seu comando!!!! \n')
                time.sleep(2)
                
                comando_b3 = input('Digite seu comando: ', )

                print ('Suas tropas começaram a avançar!!! \n')
                time.sleep(2)
                print ('Nessa batalha o dado utilizado será o D12 (doze lados) \n')
                time.sleep(2)
                print ('O dado vai ser lançado...')
                time.sleep(2)

                dado_b3 = input('Jogue o dado (jogar): ', )

                print('Dado =', d12, '\n')
                time.sleep(2)

                if d12 > 6:
                        print('Definitivamente os Poros não estavam esperando por isso, a invasão foi um sucesso!!! \n')
                        time.sleep(2)
                        print('Mas isso foi apenas uma vitória, ainda está longe da guerra acabar.')
                        time.sleep(2)
                        print('Ainda faltam os territórios que eles conquistaram.')
                        time.sleep(2)
                        print('Até isso acontecer muitas pessoas ainda vão morrer. \n')
                        time.sleep(2)
                        print('Porém.. \n')
                        time.sleep(2)
                        print('Há uma forma de acabar com a guerra agora.')
                        time.sleep(2)
                        print('As cidades que foram conquistadas tem a mesma fonte de água! \n')
                        time.sleep(2)
                        print('Portanto..')
                        time.sleep(2)
                        print('Você tem duas opções:')
                        time.sleep(2)
                        print('1 - Seguir para o próximo conflito com o restante de suas tropas e possivelmnete ter alianças durante o processo.')
                        print('Porém a guerra pode levar anos (estimativa de 5 anos), além das mortes a mais que seu povo terá')
                        print('Ou')
                        time.sleep(2)
                        print('2 - Jogar um veneno mortal na fonte de água das cidades, assim a guerra finalizará de vez e a ameaça acabará de vez. \n')
                        time.sleep(2)
                
                while True:
                        escolha_estrategia_b3_2 = input('Qual é a sua decisão comandante??: ', )
                        
                        if escolha_estrategia_b3_2 == '1':
                                print('A guerra ainda correu por alguns anos, mas você rescreveu a historia e salvou milhares de inocentes.')
                                time.sleep(2)

                                break
                        elif escolha_estrategia_b3_2 == '2':
                                print('O veneno foi lançado!!')
                                time.sleep(2)
                                print('Além das tropas, mulheres e crianças foram mortas de todas essas civilizações conquistdas!')
                                time.sleep(2)
                                print('Pelo menos a guerra acabou..')
                                time.sleep(2)

                                break
                        else:
                                print('Por favor, digite uma das opções: 1 ou 2')        

                else:
                        print ('Nao foi uma boa ideia atacar pela escolha: ', escolha_estrategia_b3_1)
                        time.sleep(2)
                        print ('Eles estavam esperando por nós, foi uma enboscada')
                        time.sleep(2)
                        print ('Suas tropas foram aniquiladas e sua tribo invadida pelo Poros')
                        time.sleep(2)
                        print ('Foi algo terrivel de se ver..')
                        time.sleep(2)
                
                print('FIM DE JOGO')    

                print ('Sua pontuação foi de: ', pontuação_jogo, 'de 100')
                time.sleep(2)
                break

        elif escolha_lado == '2':

                exercito_barco = exercito_barco + 50
                exercito_arqueiros = exercito_arqueiros + 2000 
                exercito_guerreiros = exercito_guerreiros + 1300      

                print ('Parabéns, você é o comandante da tribo Poros. \n')
                time.sleep(2)
                print ('Você tem como objetivo vencer essa guerra com o menor número de baixas do seu lado')
                time.sleep(2)
                print ('Para atingir seu objetivo, de se defender dos brutais ataques da tribo Soyoz, você precisa: \n')
                time.sleep(2)
                print ('- Defender a ponte que divide as duas tribos; \n- Defender a tribo mais próxima \n- E defender a capital de Poros')
                time.sleep(2)
                ######   Batalha 1   ######

                print ('Sua primeira batalha vai começar: \n')
                time.sleep(2)
                print ('Você deve defender a ponte.')
                time.sleep(2)
                print ('A invasão dos Soyouz pode ser pela água e/ou pela própria a ponte:')
                time.sleep(2)
                print ('Você tem disponível:')
                print ('- 15 barcos com 35 guerreiros em cada; \n- 1300 guerreiros; \n- 2000 arqueiros;')
                print ('Você tem direito a escolher apenas duas das três tropas disponíveis;')
                time.sleep(2)
                print ('25% - (1) Barcos e Arqueiros; \n30% - (2) Barcos e Guerreiros (BG); \n80% - (3) Guerreiros e Arqueiros (GA);')
                print ('As "%" indicam a probabilidade de ganho. \n') 
                print ('LEMBRE-SE QUE: cada escolha sua tem uma pontuação')         

                while True:
                
                        escolha_tropas = input ('Escolha as tropas que deseja: \n')

                        if escolha_tropas == '1':
                                mensagem_ataque = 'Barcos atiram com seus canhões, sempre mirando na destruição de seus oponentes\n Todos os seus barcos foram destruidos'
                                mensagem_derrota = 'Você perdeu com uma derrota esmagadora'
                                mensagem_final = 'Todos os seus barcos foram destruidos'

                                pontuação_jogo = pontuação_jogo + 10
                                break 
                        elif escolha_tropas == '2':
                                mensagem_derrota = 'Você perdeu, mas chegou bem perto'
                                mensagem_final = 'Todos os seus barcos se tornaram Guerreiros'

                                pontuação_jogo = pontuação_jogo + 20
                                break
                        elif escolha_tropas == '3':
                                mensagem_ataque = 'Barcos atiram com seus canhões, sempre mirando na destruição de seus oponentes\n Todos os seus barcos foram destruidos'
                                mensagem_derrota = 'Você perdeu a primeira batalha'
                                mensagem_final = 'Todos os seus barcos foram destruidos'

                                pontuação_jogo = pontuação_jogo + 10
                                break
                        else:
                                print('Por favor, digite uma das opções: 1, 2 ou 3')

                print ('O dado usado será um D8 (oito lados). \n')
                time.sleep(2)
                print ('As tropas estão prontas em suas respectivas posições, esperando o seu comando.')
                time.sleep(2)
                
                comando_b1 = input('Digite seu comando: ', )

                print ('\nA batalha começou. \n')
                time.sleep(2)
                print ('Os Soyoz estão atacando seu território com muitos Arqueiros e incontaveis Guerreiros')
                time.sleep(2)
                print ('Flechas de fogo voam pelo território, apenas buscando uma vítima para incendiar.')
                time.sleep(2)
                print ('O som das espadas se chocando ressoa pela cidade, espalhando o medo e terror por todos os lados.')
                time.sleep(2)
                print(mensagem_ataque, '\n')
                time.sleep(2)

                print ('O dado vai ser lançado..')
                time.sleep(2)

                dado_b1 = input('Jogue o dado (jogar): ', )

                print ('Dado = 5')
                time.sleep(2)
                print ('Depois de árduas horas de batalha.. ')
                time.sleep(2)
                print ('Seu exército começa a perder posição para o invasor. \n')
                time.sleep(2)
                print (mensagem_final, '\n')
                time.sleep(2)

                print ('Nessa batalha:')

                if escolha_tropas == '1':
                        print ('Restaram: nenhum guerreiro (15 barcos) e 500 Arqueiros')
                        mortes = mortes + 525 + 1500
                        print ('Número de mortes = ', mortes, '\n')

                elif escolha_tropas == '2':
                        print ('Restaram: 500 Arqueiros e 400 Guerreiros')
                        mortes = mortes + 1500 + 900
                        print ('Número de mortes = ', mortes, '\n')

                else:
                        print ('Restaram: nenhum guerreiro (15 barcos) e 400 Guerreiros')
                        mortes = mortes + 525 + 900
                        print ('Número de mortes = ', mortes, '\n')
                time.sleep(2)

                print ('Você perdeu a primeira batalha, mas ainda não perdeu a guerra \n')
                time.sleep(2)
                print ('Passaram-se alguns dias.. \n')
                time.sleep(2)
                print ('Seus soldados estão cansados, muitos morrendo de fome')
                time.sleep(2)
                print ('Seu vice-comandante lhe informa que o povo Yahudi não enviou soldados a guerra.')
                time.sleep(2)
                print ('E, enquanto o país sofre com a crise, a tribo Yahudi ainda se beneficia com farta comida')
                time.sleep(2)
                print ('Sem dividir nada com seus soldados \n')
                time.sleep(2)
                print ('Em relação a isso você pode: ')
                print ('1 - Confiscar os bens dos Yahudi para alimentar e melhorar seu exercito;')
                print ('Sabendo que eles não ajudaram seus soldados exaustos')
                print ('2 - Ignorar esse fato e permitir que continuem se beneficiando sem participar da guerra')
                time.sleep(2)

                while True:
                
                        escolha_acao = input('O que deseja fazer?: ', )

                        if escolha_acao == '1':
                                print('Você confiscou os bens do povo Yahudi.')
                                time.sleep(2)
                                print('Isso contribui muito para aumentar e fortalecer seu exercito')
                                time.sleep(2)

                                pontuação_jogo = pontuação_jogo + 20
                                break

                        elif escolha_acao == '2':
                                print('Você não confisca os bens do povo Yahudi, seu exercito acaba tendo ainda mais baixas.')
                                time.sleep(2)
                                print('Muitos morrem de fome e o povo Yahudi continua se beneficiando da guerra e sem contribuir com o pais')
                                time.sleep(2)
                                print('Apesar de sua escolha, uma tribo aliada resolveu mandar novas tropas para auxiliar seu exercito')
                                time.sleep(2)

                                pontuação_jogo = pontuação_jogo + 10
                                break

                        else:
                                print('Por favor, digite uma das opções: 1 ou 2')

                print('Você ganhou 2000 arqueiros e 1000 guerreiros')
                time.sleep(2)
                
                exercito_arqueiros = exercito_arqueiros + 2000
                exercito_guerreiros = exercito_guerreiros + 1000

                ######      Batalha 2     ######

                print ('INÍCIO DA BATALHA 2: \n')
                time.sleep(2)
                print ('Agora você tem 1500 guerreiros e 2000 arqueiros')
                time.sleep(2)
                print ('Você tem uma grande vantagem, pois seu exército conhece o território em que está lutando \n')
                time.sleep(2)
                print ('As tropas estão prontas em suas respectivas posições, esperando o seu comando. \n')
                time.sleep(2)
                
                comando_b2 = input('Digite seu comando: ', )

                print ('A batalha da cidade começou. \n')
                time.sleep(2)
                print ('Os Soyouz estão atacando seu território com muitos Arqueiros e incontaveis Guerreiros')
                time.sleep(2)
                print ('O som do desespero é evidente')
                time.sleep(2)
                print ('O dado usado será um D10 (dez lados). \n')
                time.sleep(2)
                print ('O dado vai ser lançado..')
                time.sleep(2)

                dado_b2 = input('Jogue o dado (jogar): ', )

                print ('Dado = 6 \n')
                time.sleep(2)
                print ('Seu exército conseguiu defender o território, muitas tropas foram perdidas, mas seu sacrificio salvará a vida de muitos')
                time.sleep(2)
                print ('Você percebe que pode ganhar mais espaço e atacar o inimigo de surpresa recuando para a floresta, um terreno que suas tropas ja conhecem')
                time.sleep(2)
                print ('O inimigo desconhece as suas novas tropas, por isso, use elas para emboscar ele por todos os lados')
                print ('1 - Você deseja atrair seus inimigos para a floresta?')
                print ('2 - Ou deseja se manter no compo de batalha??')

                while True:
                        escolha_estrategia_b2_1 = input('Qual você escolhe?? (1,2)', )

                        if escolha_estrategia_b2_1 == '1':
                                print ('Você diz para as suas tropas para recuar para a floresta e usar a cobertura das arvores para atacar o inimigo.')
                                time.sleep(1)
                                print ('Os Soyoz começam a ir atrás deles.')
                                time.sleep(1)

                                pontuação_jogo = pontuação_jogo + 20
                                break
                
                        elif escolha_estrategia_b2_1 == '2':
                                print ('Suas tropas começam batalhar fortemente no campo de batalha')
                                time.sleep(1)
                                print ('Porém o ataque do inimigo é brutal, seus soldados são obrigados a recuarem para a floresta.')
                                time.sleep(1)

                                pontuação_jogo = pontuação_jogo + 10
                                break
                        else:
                                print('Por favor, digite uma das opções: 1 ou 2')

                print ('As tropas inimigas começam a seguir seus soldados para a floresta')
                time.sleep(2)
                print ('Surge o momento de atacar eles por todos os lados com suas novas tropas')
                time.sleep(2)
                print ('O inimigo não esperava por seu aumento de tropas, o inimigo começa a morrer consideravelmente')
                time.sleep(2)
                print ('O inimigo recua de volta para a ponte, você ganhou essa batalha, parabéns comandante')
                time.sleep(2)
                print ('Nessa batalha restaram: 1500 arqueiros e 900 guerreiros \n')
                time.sleep(2)

                mortes = mortes + 600 + 500

                print ('Número de mortos até agora: ', mortes)
                time.sleep(2)

                #### batalha 3 ####

                print('Após alguns dias, uma nova batalha se aproxima')
                time.sleep(2)
                print('A batalha final que decidira todos os caminhos')
                time.sleep(2)
                print ('Porém mesmo vencendo a batalha anterior você ainda perdeu muitos homens.')
                time.sleep(2)
                print ('Por causa da sua vitória, você conseguiu adiantar a chegada dos Soyouz')
                time.sleep(2)
                print ('Porém você está com uma dificuldade na sua defesa:')
                time.sleep(2)
                print ('O seu ponto fraco são os Yahudis, eles possuem a barreira muito fraca, sem defesas, nos tornando vulneráveis. \n')
                time.sleep(2)
                print ('Você tem duas opções:')
                print ('1 - Finalmente tirar os Yahudis da jogada, dizimando-os.')
                print ('Assim você tem total controle da sua defesa. - 75% êxito')
                print ('2 - Deixar assim mesmo e tentar fazer uma emboscada para os Soyouz. - 37% êxito')

                while True:
                        escolha_estrategia_b3_1 = input('Escolha o que deseja fazer:', )

                        if escolha_estrategia_b3_1 == '1':
                                print ('Suas tropas fazem o trabalho com entusiasmo.')
                                time.sleep(1)
                                print ('Em Poros, não tem mais Yahudis. \n')
                                time.sleep(1)

                                pontuação_jogo = pontuação_jogo + 20
                                break
                        elif escolha_estrategia_b3_1 == '2':
                                print ('Você não tem acesso as defesas..')
                                time.sleep(1)
                                print ('Você está dependendo do Yahudis \n')
                                time.sleep(1)

                                pontuação_jogo = pontuação_jogo = 15
                                break
                        else:
                                print('Por favor, digite uma das opções: 1 ou 2')

                print ('A batalha está prestes a começar..')
                time.sleep(2)
                print ('O inimigo faz um ataque surpresa, ninguém esperava por essa!')
                time.sleep(2)
                print ('O dado usado será um D12 (doze lados). \n')
                time.sleep(2)
                print ('O dado vai ser lançado..')
                time.sleep(2)

                dado_b2 = input('Jogue o dado (jogar): ', )

                if d12 <= 6 :
                        print ('Dado = ', d12, '\n')
                        time.sleep(2)
                        print ('Mesmo com poucas chances de vitória você venceu a batalha.')
                        time.sleep(2)
                        print ('Agora você é, praticamente, o mais forte da nação')
                        time.sleep(2)

                        if escolha_estrategia_b3_1 == '1':
                                print ('Você já consegue eliminar todos os Yahudes de seus territórios conquistados.')
                                time.sleep(2)
                        else:
                                print ('Com esse poderío, você pode eliminar os Yahudis de suas terras.')
                                time.sleep(2)
                
                else:
                        print ('Dado = ', d12, '\n')
                        time.sleep(2)
                        print ('O ataque supresa foi mais forte do que você imaginou.')
                        time.sleep(2)
                        print ('Os Soyouz dominaram Poros.')         
                        time.sleep(2)
                        
                        print('FIM DE JOGO')
                        time.sleep(2)
                        print ('Sua pontuação foi de: ', pontuação_jogo, 'de 80')
                
                break
        
        else:
                print('Por favor, digite uma das opções: 1 ou 2')

print('Mas espera ai.. \n')
time.sleep(2)
print('REAL HISTÓRIA POR TRAZ DO JOGO: \n \n')
time.sleep(2)
print('Belli Orbis Terrarum II , em latim, significa Segunda Guerra Mundial.')
time.sleep(2)
print('"Poros" traduzido do indonezio fica Eixo.')
time.sleep(2)
print('"Soyouz" traduzido do russo fica Aliança.')
time.sleep(2)
print('"Yahudi" traduzido do indonezio fica judeos, povo judaíco.')
time.sleep(2)
print('Pela sua escolha:')
time.sleep(2)

if escolha_lado == '2':
        print('Você foi um comandante da Alemanha nazista e você liderava o Eixo') 
        time.sleep(2)
        print('Se você escolheu matar os Yahudis porque eles pareciam estar atrapalhando o país..')
        time.sleep(2)
        print('Provavelmente, se você estivesse presente na Alemanha nazista nessa époco, você seria nazista!!')
        time.sleep(2)

else: 
        print('Você foi um comandante nos EUA e estava liderando a Aliança .')
        time.sleep(2)
        print('A opção de usar o veneno no jogo foi represantado das bombas de Hiroshima e Nagasaki.')
        time.sleep(2)
        print('Que mataram cerca de 200 mil pessoas, principalmente inocentes.')
        time.sleep(2)
        print('Se vc optou por usar o veneno')
        time.sleep(2)
        if escolha_estrategia_b3_2 == '2':
                print('Então, se você estivesse presente durante essa época, provavelmente seria a favor de lançar as bombas.')

