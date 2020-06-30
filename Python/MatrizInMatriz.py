#  Integrantes do grupo: 
     
     # Rafael Lua De Sousa e Silva  RA: 31948571
     # Cássio Kineipe da Costa      RA: 31929265
     # Marcelo Nao Takayama         RA: 31942407
     
     
# Função que carrega a matriz da imagem para uma matriz no código
def carregaImagem():
    # Abre o arquivo txt
    arquivo = open('imagem.txt', 'r')
    texto = []
    matriz = []
    matrix = []
    # Lê as linhas do arquivo
    texto = arquivo.readlines()

    for i in range(len(texto)):
        matriz.append(texto[i].split())

    for x in range(len(matriz)):
        oficial = []
        for y in range(9):
            oficial.append(matriz[x][0][y])
        matrix.append(oficial)

    # Fecha o arquivo txt
    arquivo.close()

    return matrix

def printaMatriz(matrix, texto):
    print("\n\nMatriz da imagem:\n ")

    for c in range(9):
        print(matrix[c])

def criaPadrao():
    matrizPadrao = [["0", "1", "0"], ["1", "1", "1"], ["0", "1", "0"]]
    print("\n\nMatriz padrao: \n")
    for i in range(0, 3):
        print(matrizPadrao[i])
    return matrizPadrao

def detectaPadrao(matrix, matrizPadrao):
    cont = 0

    for y in range(1, len(matrix) - 1):  # linhas
        for z in range(1, len(matrix[0]) - 1):  # colunas
            # Verifica se o elemento central é igual
            if (matrix[y][z] == matrizPadrao[1][1]):
                # Verifica todas as poições ao redor do elemento
                if (matrix[y - 1][z - 1] == matrizPadrao[0][0]):
                    cont += 1
                if (matrix[y - 1][z] == matrizPadrao[0][1]):
                    cont += 1
                if (matrix[y - 1][z + 1] == matrizPadrao[0][2]):
                    cont += 1
                if (matrix[y][z - 1] == matrizPadrao[1][0]):
                    cont += 1
                if (matrix[y][z + 1] == matrizPadrao[1][2]):
                    cont += 1
                if (matrix[y + 1][z - 1] == matrizPadrao[2][0]):
                    cont += 1
                if (matrix[y + 1][z] == matrizPadrao[2][1]):
                    cont += 1
                if (matrix[y + 1][z + 1] == matrizPadrao[2][2]):
                    cont += 1

            if (cont == 8):
                print("\n\nO padrão se encontra na matriz:\n")
                return True
            else:
                cont = 0
    if (cont == 0):
        print("\n\nO padrão se encontra na matriz:\n")
        return False

def main():
    matrix = carregaImagem()
    printaMatriz(matrix, 9)
    matrizPadrao = criaPadrao()
    print(detectaPadrao(matrix, matrizPadrao))

main()