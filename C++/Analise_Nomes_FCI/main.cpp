// Cassio Kineipe - 31929265
// Rafael Lua - 31948571
// Irvin Ken - 31947476
// Guilherme Reis - 31920918

//---------------------------------------
#include <iostream> // "cout e cin"
#include <fstream>  // ler arquivo
#include <chrono>
#include <map>
#include <string>
#include <iterator>
#include <bits/stdc++.h>

using namespace std; // string

/// Ordenar map -----------------não tem como ordenar uma arvore, por isso a necessidade de se utilizar um map

bool cmp(pair<string, int> &a,
         pair<string, int> &b)
{
    return a.second < b.second;
}

void sort(map<string, int> &M)
{

    // Declarar vetores em pares
    vector<pair<string, int>> A;

    for (auto &it : M)
    {
        A.push_back(it);
    }

    // função de comparação
    sort(A.begin(), A.end(), cmp);

    // Mostrar valor ordenado
    for (auto &it : A)
    {
        cout << it.first << ' '
             << it.second << endl;
    }
}

/// Ordenar map -----------------^^^^^^

class AVLNode
{
public:
    AVLNode();
    AVLNode(string);
    virtual ~AVLNode();
    string getData();
    int getqtd();
    int getHeight();
    void setData(string);
    void setqtd(int);
    void setHeight(int);
    AVLNode *getLeft();
    AVLNode *getRight();
    void setRight(AVLNode *);
    void setLeft(AVLNode *);

protected:
private:
    AVLNode *left, *right;
    string data;
    int qtd;
    int height;
};

AVLNode::AVLNode()
{
    left = NULL;
    right = NULL;
    height = 0;
    qtd = 0;
}

AVLNode::AVLNode(string valor)
{
    left = NULL;
    right = NULL;
    right = NULL;
    qtd = 0;
    data = valor;
    height = 0;
}
AVLNode::~AVLNode()
{
    //dtor
}
void AVLNode::setData(string d)
{
    data = d;
}
string AVLNode::getData()
{
    return data;
}

void AVLNode::setqtd(int x)
{
    qtd = x;
}
int AVLNode::getqtd()
{
    return qtd;
}

void AVLNode::setLeft(AVLNode *n)
{
    left = n;
}
AVLNode *AVLNode::getLeft()
{
    return left;
}

void AVLNode::setRight(AVLNode *n)
{
    right = n;
}
AVLNode *AVLNode::getRight()
{
    return right;
}

void AVLNode::setHeight(int h)
{
    height = h;
}

int AVLNode::getHeight()
{
    return height;
}

class AVLTree
{
public:
    AVLTree();
    virtual ~AVLTree();
    AVLNode *getRoot();
    bool isEmpty();
    int height();
    int qtNodes();
    void inserir(string x);
    void preOrder();
    void posOrder();
    void inOrder();
    void remover(string x);
    void reverseOrder();
    int getcomparacoes2();
    void printqtd2();
    map<string, int> nomes;

protected:
private:
    int comparacoes2;
    AVLNode *root;
    int localizar(AVLNode *no, string x);
    int height(AVLNode *);
    int qtNodes(AVLNode *);
    AVLNode *inserir(AVLNode *, string);
    void preOrder(AVLNode *no);
    void posOrder(AVLNode *no);
    void inOrder(AVLNode *no);

    AVLNode *rotateLL(AVLNode *);
    AVLNode *rotateRR(AVLNode *);
    AVLNode *rotateLR(AVLNode *);
    AVLNode *rotateRL(AVLNode *);
    void reverseOrder(AVLNode *);
    int maximo(int, int);
};

AVLTree::AVLTree()
{
    //ctor
    root = NULL;

    comparacoes2 = 0;
}

AVLTree::~AVLTree()
{
    //destrutor
    //TODO - Implementar destrutor
}

int AVLTree::getcomparacoes2()
{
    return comparacoes2;
}

bool AVLTree::isEmpty()
{
    return root == NULL;
}

int AVLTree::height()
{
    return height(root); //altura da �rvore � a altura do seu n� raiz
}

int AVLTree::height(AVLNode *no)
{ /*Se o n� for NULL retorna -1, sen�o retorna o que vier do m�todo getHeight()*/

    return no == NULL ? -1 : no->getHeight();
}

int AVLTree::maximo(int lhs, int rhs)
{
    return lhs > rhs ? lhs : rhs;
}

int AVLTree::qtNodes()
{
    return qtNodes(root);
}

int AVLTree::qtNodes(AVLNode *no)
{
    if (no == NULL)
        return 0;
    int qtleft = qtNodes(no->getLeft());
    int qtright = qtNodes(no->getRight());
    return qtleft + qtright + 1;
}
/*Inserir polimorfico. o Metodo publico pra inserir na arvore. Esse metodo invoca o metodo privado, que é recursivo*/
void AVLTree::inserir(string x)
{

    root = inserir(root, x);

    int n = localizar(root, x);

    nomes.insert(pair<string, int>(x, 1));
}

AVLNode *AVLTree::inserir(AVLNode *node, string valor)
{

    /*Se uma arvore ou subarvore vazia, cria 1 novo no e retorna*/
    if (node == NULL)
    {
        return new AVLNode(valor);
    }

    if (valor < node->getData())
    {
        node->setLeft(inserir(node->getLeft(), valor));
        if (height(node->getRight()) - height(node->getLeft()) == -2)
        {
            if (valor < node->getLeft()->getData())
            {
                node = rotateLL(node);
            }
            else
            {
                node = rotateLR(node);
            }
        }
    }
    else
    {
        if (valor > node->getData())
        {
            node->setRight(inserir(node->getRight(), valor));
            if (height(node->getRight()) - height(node->getLeft()) == 2)
            {
                if (valor > node->getRight()->getData())
                    node = rotateRR(node);
                else
                    node = rotateRL(node);
            }
        }
    }
    node->setHeight(maximo(height(node->getLeft()), height(node->getRight())) + 1);

    return node;
}

AVLNode *AVLTree::rotateLL(AVLNode *node)
{
    AVLNode *leftSubTree = node->getLeft();
    node->setLeft(leftSubTree->getRight());
    leftSubTree->setRight(node);
    node->setHeight(maximo(height(node->getLeft()), height(node->getRight())) + 1);
    leftSubTree->setHeight(maximo(height(leftSubTree->getLeft()), height(node) + 1));
    return leftSubTree;
}

AVLNode *AVLTree::rotateRR(AVLNode *node)
{
    AVLNode *rightSubTree = node->getRight();
    node->setRight(rightSubTree->getLeft());
    rightSubTree->setLeft(node);
    node->setHeight(maximo(height(node->getLeft()), height(node->getRight())) + 1);
    rightSubTree->setHeight(maximo(height(rightSubTree->getRight()), height(node) + 1));
    return rightSubTree;
}

AVLNode *AVLTree::rotateLR(AVLNode *node)
{
    node->setLeft(rotateRR(node->getLeft()));
    return rotateLL(node);
}

AVLNode *AVLTree::rotateRL(AVLNode *node)
{
    node->setRight(rotateLL(node->getRight()));
    return rotateRR(node);
}

void AVLTree::preOrder()
{
    preOrder(root);
}

void AVLTree::inOrder()
{
    inOrder(root);
}

void AVLTree::posOrder()
{
    posOrder(root);
}
void AVLTree::reverseOrder()
{
    reverseOrder(root);
}
void AVLTree::preOrder(AVLNode *no)
{
    if (no != NULL)
    {
        cout << no->getData() << endl;
        preOrder(no->getLeft());
        preOrder(no->getRight());
    }
}

void AVLTree::posOrder(AVLNode *no)
{
    if (no != NULL)
    {
        posOrder(no->getLeft());
        posOrder(no->getRight());
        cout << no->getData() << endl;
    }
}

void AVLTree::inOrder(AVLNode *no)
{
    if (no != NULL)
    {
        inOrder(no->getLeft());
        cout << no->getData() << " Qtd: " << no->getqtd() << endl;
        inOrder(no->getRight());
    }
}

int AVLTree::localizar(AVLNode *no, string x)
{
    while (no != NULL)
    {
        comparacoes2++;
        if (x == no->getData())
        {

            no->setqtd(no->getqtd() + 1);
            nomes.find(x)->second = no->getqtd();

            return 1;
        }

        if (x < no->getData())
        {

            no = no->getLeft();
        }
        else
        {
            no = no->getRight();
        }
    }
    return 0;
}

void AVLTree::reverseOrder(AVLNode *no)
{

    sort(nomes);
}

class No
{
private:
    No *esq, *dir; //Ponteiros para esquerda e direita
    //Informacao mantida em cada no

    string nome;
    int qtd;

public:
    No(string nome)
    {

        // Associar cada uma delas ao seu respectivo ponteiro
        this->nome = nome;
        qtd = 1;

        esq = NULL;
        dir = NULL;
    }

    string getnome()
    {
        return nome;
    }
    int getqtd()
    {
        return qtd;
    }

    void setqtd(int x)
    {

        qtd = x;
    }

    // Percorrer caminho esquerda
    No *getEsq()
    {
        return esq;
    }

    // Percorrer caminho direita
    No *getDir()
    {
        return dir;
    }

    // Definir esquerda
    void setEsq(No *no)
    {
        esq = no;
    }

    // Definir direita
    void setDir(No *no)
    {
        dir = no;
    }
};

class Arvore
{

private:
    No *raiz;
    
    

    map<string, int> nomes; // printar em ordem de frequencia sem precisar criar uma nova arvore para isso, armazenar duas variaveis 

    // em vez de usar map, teria de criar uma nova arvore com novas regras. Em tese, teria de alterar o node e criar uma nova arvore.

    // 1 map para cada arvore
public:
    int comparacao1 = 0;
    Arvore()
    {
        raiz = NULL;
    }

    // Função inserir para todas as variáveis
    void inserir(string nome)
    {
        nomes.insert(pair<string, int>(nome, 1)); // inserir novo nome e definir frequencia como 1, o localizar atualiza essa frequencia

        if (raiz == NULL)
        {
            raiz = new No(nome);
        }
        else
        {

            int qtdx = localizar(nome, raiz); // altera a sequencia, não vai mostrar mais de dois nomes

           

            if (qtdx == 1)
            {
                cout << "";
            }
            else
            {
                inserirAux(raiz, nome);
            }
        }
    }

    void inserirAux(No *no, string nome)
    {

        if (nome < no->getnome())
        {
            if (no->getEsq() == NULL)
            {
                No *novo_no = new No(nome);
                no->setEsq(novo_no);
            }
            else
            {
                inserirAux(no->getEsq(), nome);
            }
        }
        else if (nome > no->getnome())
        {
            if (no->getDir() == NULL)
            {
                No *novo_no = new No(nome);
                no->setDir(novo_no);
            }
            else
            {
                inserirAux(no->getDir(), nome);
            }
        }
    }

    No *getRaiz()
    {
        return raiz;
    }

   

    void emOrdem(No *no)
    {
        if (no != NULL)
        {

            emOrdem(no->getEsq());

            cout << no->getnome() << " Qtd: " << no->getqtd() << "\n";
            emOrdem(no->getDir());
        }
    }

    void printqtd() // Mostrar ordenado com base no map
    {
        sort(nomes);
    }

    int localizar(string n, No *no)
    {

        while (no != NULL)
        {// Deve comparar o valor inserido com a arvore inteira
        
            comparacao1++;  // contar comparações
            
            if (n == no->getnome())
            {

                no->setqtd(no->getqtd() + 1); // incrementa a frequencia, altera a quantidade no nó do valor desejado       
                nomes.find(n)->second = no->getqtd(); // atualiza em seu correspondente do map (1 de cada nome, variando a quantidade)

                return 1;
            }

            if (n < no->getnome())
            {

                no = no->getEsq();
            }
            else
            {
                no = no->getDir();
            }
        }
        return 0;
    }

    void buscar(No *no, string nome)
    {

        while (no != NULL)
        {

            if (nome == no->getnome())
            {

                cout << no->getnome() << " - " << no->getqtd();
            }

            if (nome < no->getnome())
            {

                no = no->getEsq();
            }
            else
            {
                no = no->getDir();
            }
        }
    }


 int comparacaoshow()
    {
    
        return comparacao1;
    }


};

int main()
{

    cout << "\033c";
    // Criação de duas árvores, uma para ordenar por nomes e outra para o valor da coluna"total"
    Arvore arv; // Binaria
    AVLTree avl;


    int elementos = 0;
    int menu;
    int duracao1 = 0;
    int duracao2 = 0;

    cout << "\033c"; // Limpara a tela

    // Leitura de arquivos ---------------------
    ifstream myfile;
    myfile.open("nomeFci.txt"); // Nome do arquivo, deve estar baixado na mesma pasta do código.

    // Analisar o tempo de inicio e fim das duas arvores e contabiliza o tempo de execução
    auto t1 = chrono::high_resolution_clock::now();
    while (myfile.good())
    { // Enquanto o arquivo estiver aberto

        string line;
        getline(myfile, line, '\n');

        elementos++;
        arv.inserir(line);
    }
    auto t2 = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();

    duracao1 = duration;

    myfile.close();

    ifstream myfile2;
    myfile2.open("nomeFci.txt"); // Nome do arquivo, deve estar baixado na mesma pasta do código.

    auto t3 = chrono::high_resolution_clock::now();
    while (myfile2.good())
    { // Enquanto o arquivo estiver aberto

        string line;
        getline(myfile2, line, '\n');

        avl.inserir(line);
    }
    auto t4 = chrono::high_resolution_clock::now();
    auto duration2 = chrono::duration_cast<chrono::microseconds>(t4 - t3).count();

    duracao2 = duration2;

    myfile2.close();
  

    while (true)
    {

        cout << "\n\n================ Nomes da FCI ===================\n\n";
        cout << "0-Sair:\n";
        cout << "1-Imprimir dados da (BST):\n";
        cout << "2-Imprimir nomes em ordem alfabetica (BST):\n";
        cout << "3-Imprimir nomes ordenados por frequencia (BST):\n";
        cout << "4-Imprimir dados (AVL):\n";
        cout << "5-Imprimir nomes em ordem alfabetica (AVL):\n";
        cout << "6-Imprimir nomes ordenados por frequencia (AVL):\n";
        cout << "7-Buscar por nome:\n";
         cout << "\n===================================================\n\n";

        cout << "Digite: ";
        cin >> menu;

        if (menu == 0)
        {
            break;
        }

        if (menu == 1)
        {
            cout << "\033c";
            cout << "\n\nArvore BST: ";
            cout << "\nElementos : " << elementos;
            cout << "\nComparações : " << arv.comparacaoshow();
            cout << "\nTempo de execuão : " << duracao1 <<" Microsegundos"<< "\n\n";
        }
        if (menu == 2)
        {
            cout << "\033c";

            arv.emOrdem(arv.getRaiz());
        }
        if (menu == 3)
        {
            cout << "\033c";

            arv.printqtd();
        }

        if (menu == 4)
        {
            cout << "\033c";
            cout << "\n\nArvore AVL: ";
            cout << "\nElementos: " << elementos;
            cout << "\nComparações: " << avl.getcomparacoes2();
            cout << "\nTempo de execução: " << duracao2 <<"  microsegundos"<<"\n\n";
        }
        if (menu == 5)
        {
            cout << "\033c";

            avl.inOrder();
        }

        if (menu == 6)
        {
            cout << "\033c";

            avl.reverseOrder();
        }

        if (menu == 7) // Avl Busca
        {
            string nome;
            cout << "\033c";
            cout << "Digite o nome que deseja buscar: \n";
            cin >> nome;
            cout << "\n\n";

            arv.buscar(arv.getRaiz(), nome);
        }
    }
}


// AVL Balanceada, logo precisa de menos comparações para encontrar o valor.