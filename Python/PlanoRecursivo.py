
# Código base que usa recurcividade para printar uma mensagem que não pode ser lida pelo codigo 
# gado dmais

def menssagem(lista,cont,codigo,dia):

  cont += 3
  
  if lista[cont] != '?':
   codigo += lista[cont] 
   
   menssagem(lista,cont,codigo,dia)
  else:
    print('\033c')
    print(codigo+" "+"dia"+" "+dia+" "+"?")

    
dia = input("Digite um dia dessa semana: ")

lista = ['V',"l","d",'a',"w","d",'m',"n","d",'o',"i","d",'s',"s","v",' ',"w","d",'s',"w","d",'a',"ç","a",'i',"c","a",'r',"o","l",'?',"u","r"]

codigo = ''
cont = -3
menssagem(lista,cont,codigo,dia)