
#  Integrantes do grupo: 
     
     # Rafael Lua De Sousa e Silva  RA: 31948571
     # Cássio Kineipe da Costa      RA: 31929265


def tabuleiro():
  print('         ',A,'|',B,'|',C,'            1 | 2 | 3')
  print('         -----------','          -----------')
  print('         ',D,'|',E,'|',F,'            4 | 5 | 6')
  print('         -----------','          -----------')
  print('         ',G,'|',H,'|',I,'            7 | 8 | 9')


print('\033c')   # Limpar Terminal

A = ' '
B = ' '
C = ' '
D = ' '
E = ' '
F = ' '
G = ' '
H = ' '
I = ' '

mensagem = ''   # Mensagem a ser apresentada
marca1 = 'x'
marca2 = 'o'


lista1 = [] # Jogador1
lista2 = [] # Jogador2

jogador = 1 # (1 ou 2)
cont = 0    # Numero de jogadas

velha = False

while True:
  escolha = ''

  print('\033c')
  print(mensagem)
  mensagem = ''
  print()
  tabuleiro()
  print()
  cont += 1

  if cont % 2 == 1:
    jogador = 1
  else:
    jogador = 2

  if jogador == 1:
    marca = marca1
  else:
    marca = marca2
    
  escolha = input('Jogador {}, digite sua escolha: '.format(jogador))
  escolha = escolha.upper()

  if escolha == 'A' or escolha =='1':
    escolha = 'A'
    if A == ' ':
      A = marca
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1

  elif escolha == 'B' or escolha == '2':
    escolha = 'B'
    if B == ' ':
      B = marca
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1
  
  elif escolha == 'C' or escolha == '3':
    escolha = 'C'
    if C == ' ':
      C = marca
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1
  
  elif escolha == 'D' or escolha =='4':
    escolha = 'D'
    if D == ' ':
      D = marca
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1
  
  elif escolha == 'E' or escolha == '5':
    escolha = 'E'
    if E == ' ':
      E = marca
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1
  
  elif escolha == 'F' or escolha == '6':
    escolha = 'F'
    if F == ' ':
      F = marca
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1
  
  elif escolha == 'G' or escolha == '7':
    escolha = 'G'
    if G == ' ':
      G = marca
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1
  
  elif escolha == 'H' or escolha == '8':
    escolha = 'H'
    if H == ' ':
      H = marca   
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1
  
  elif escolha == 'I' or escolha == '9':
    escolha = 'I'
    if I == ' ':
      I = marca
    else:
      escolha = ''
      mensagem = 'Posição Ocupada, digite novamente.'
      cont -= 1
  
  else:
    escolha = ''
    mensagem = 'Formato Invalido, digite novamente'
    cont -= 1
  
  # Adicionar em listas para verificar se deu velha futuramente
  if jogador == 1: 
    lista1.append(escolha)
  elif jogador == 2:
    lista2.append(escolha)
  
  #print('escolha',escolha)
  #print('lista1',lista1)
  #print('lista2',lista2)
  
  
  
# Validações:


  # Validções Jogador 1
  if 'A' in lista1 and 'B' in lista1 and 'C' in lista1:
    break
  elif 'A' in lista1 and 'E' in lista1 and 'I' in lista1:
    break
  elif 'A' in lista1 and 'D' in lista1 and 'G' in lista1:
    break
  elif 'D' in lista1 and 'E' in lista1 and 'F' in lista1:
    break
  elif 'B' in lista1 and 'E' in lista1 and 'H' in lista1:
    break
  elif 'C' in lista1 and 'F' in lista1 and 'I' in lista1:
    break
  elif 'C' in lista1 and 'E' in lista1 and 'G' in lista1:
    break
  elif 'G' in lista1 and 'H' in lista1 and 'I' in lista1:
    break


  # Validações Jogador 2 
  elif 'A' in lista2 and 'B' in lista2 and 'C' in lista2:
    break
  elif 'A' in lista2 and 'E' in lista2 and 'I' in lista2:
    break
  elif 'A' in lista2 and 'D' in lista2 and 'G' in lista2:
    break
  elif 'D' in lista2 and 'E' in lista2 and 'F' in lista2:
    break
  elif 'B' in lista2 and 'E' in lista2 and 'H' in lista2:
    break
  elif 'C' in lista2 and 'F' in lista2 and 'I' in lista2:
    break
  elif 'C' in lista2 and 'E' in lista2 and 'G' in lista2:
    break
  elif 'G' in lista2 and 'H' in lista2 and 'I' in lista2:
    break

  else: # Verificar a Velha

    if cont >= 9: # Enquanto for menor que 9 jogadas, impossivel de ter dado velha
      velha = True
      break

print('\033c') # Limpar terminal

if velha == True:
  tabuleiro()
  print('Velha x_x')

else:
  tabuleiro()
  print()
  print('Jogador {}, Você ganhou :D'.format(jogador)) #.format para encaixar uma variaáel em uma posição de um print



