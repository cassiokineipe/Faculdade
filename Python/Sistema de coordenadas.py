#Integrantes:
# Cassio Kineipe - 31929265 
# Rafael Lua - 31948571



cont1 = 0 # Usado para calcular a porcentagem
cont2 = 0
cont3 = 0
cont4 = 0


def quadrantes(x, y): #identificar os quadrantes
    global X1
    global X2
    global cont1
    global cont2
    global cont3
    global cont4

    if x > X1 and y > Y1: # quadrante 1
        qua = 1
        cont1 += 1
    elif x < X1 and y > Y1: # quadrante 2
        qua = 2
        cont2 += 1
    elif x < X1 and y < Y1: # quadrante 3
        qua = 3
        cont3 += 1
    elif x > X1 and y < Y1: # quadrante 4
        qua = 4
        cont4 += 1
    else:
        qua = 0

    if qua == 0:
        # print('Os pontos {},{} estão na origem'.format(x,y))
        return False

    else:
        # print('O pontos {},{} está no quadrante {}'.format(x,y,qua))
        return qua


def distancias(x, y, distancia): #calcula as distancias
    global var1
    global var2
    global pontoX
    global pontoY
    global pontoA
    global pontoB

    if var1 < distancia: # menor distancia
        var1 = distancia
        pontoX = x
        pontoY = y

    if var2 > distancia: # maior distancia
        var2 = distancia
        pontoA = x
        pontoB = y


def porcentagem(): # calcula a porcentagem de pontos em cada quadrante
    global num
    global cont1
    global cont2
    global cont3
    global cont4
    global calculo1
    global calculo2
    global calculo3
    global calculo4

    calculo1 = ((cont1 * 100) / num) / 3
    calculo2 = ((cont2 * 100) / num) / 3
    calculo3 = ((cont3 * 100) / num) / 3
    calculo4 = ((cont4 * 100) / num) / 3


var1 = 0  # maior distancia
var2 = 100  # menor distancia

num = int(input('Numero de pontos: ')) # determina a quantidade de pontos
X1, Y1 = input('Digite o dois pontos da origem:').split()
X1 = int(X1)
Y1 = int(Y1)

for c in range(num): # input dos pontos
    print()
    x, y = input('Digite os dois pontos: ').split()
    x = int(x)
    y = int(y)

    quadrantes(x, y)

    if quadrantes(x, y) == False: 
        print('Os pontos {},{} estão na origem'.format(x, y))
    else:
        print('O pontos {},{} está no quadrante {}'.format(x, y, quadrantes(x, y)))

    distancia = ((((x - X1) ** 2) + (y - Y1) ** 2) ** 0.5)

    distancias(x, y, distancia)

if num != 1: #printa as distancias
    print()
    print("O ponto {},{} é o mais proximo, distancia ={:.2f}".format(pontoA, pontoB, var2))
    print("O ponto {},{} é o mais distante, distancia= {:.2f}".format(pontoX, pontoY, var1))
else:
    print("O ponto {},{} é o mais proximo, distancia ={:.2f}".format(pontoA, pontoB, var2))
    print("O ponto {},{} é o mais distante, distancia= {:.2f}".format(pontoA, pontoB, var2))

porcentagem() # printa as porcentagem

print()
print()
print('A porcentagem de pontos do 1° quadrante é {:.2f}% '.format(calculo1))
print('A porcentagem de pontos do 2° quadrante é {:.2f}%'.format(calculo2))
print('A porcentagem de pontos do 3° quadrante é {:.2f}% '.format(calculo3))
print('A porcentagem de pontos do 4° quadrante é {:.2f}% '.format(calculo4))

