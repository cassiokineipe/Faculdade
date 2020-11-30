// Cassio Kineipe - 31929265
// Rafael Lua - 31948571


//---------------------------------------
#include<iostream>    // "cout e cin"
#include<fstream>     // ler arquivo
using namespace std;  // string


string bicicleta1 ;
string bicicleta2;



class No
{
private:
	No *esq, *dir; //Ponteiros para esquerda e direita
  //Informacao mantida em cada no
	
  // 13 variáveis para definir as 13 colunas do arquivo
  string nome; 
  string dex;
  string tipo1;
  string tipo2;
  string total;
  string hp;
  string atack;
  string defesa;
  string atacksp;
  string defesasp;
  string velocidade;
  string geracao;
  string legendary;


public:
  // Passar as 13 variáveis pelo nó 
	No(string nome, string dex, string tipo1,string tipo2,string total,string hp,string atack,string defesa,string atacksp, string defesasp,string velocidade,string geracao,string legendary){

    // Associar cada uma delas ao seu respectivo ponteiro
    this->nome = nome; 
    this->dex = dex;
    this->tipo1 = tipo1;
    this->tipo2 = tipo2 ;
    this->total = total;
    this->hp = hp;
    this->atack = atack;
    this->defesa = defesa;
    this->atacksp = atacksp;
    this->defesasp = defesasp;
    this->velocidade = velocidade;
    this->geracao = geracao;
    this->legendary = legendary;

    
		esq = NULL;
		dir = NULL;
	}

  // 13 funções para conseguir pegar cada uma das 13 colunas se necessário

	void setnew(string x1,string x2,string x3,string x4,string x5,string  x6,string x7,string x8,string x9,string x10,string x11,string x12,string x13)
	{
		nome = x1; 
    dex = x2;
    tipo1 = x3;
    tipo2 = x4 ;
    total = x5;
    hp = x6;
    atack = x7;
    defesa = x8;
    atacksp = x9;
    defesasp = x10;
    velocidade = x11;
    geracao = x12;
    legendary = x13;
	}

	string getnome()
	{
		return nome;
	}
	string getdex()
	{
		return dex;
	}
  	string gettipo1()
	{
		return tipo1;
	}
	string gettipo2()
	{
		return tipo2;
	}
	string gettotal()
	{
		return total;
	}
	string gethp()
	{
		return hp;
	}
	string getatack()
	{
		return atack;
	}
	string getdefesa()
	{
		return defesa;
	}
	string getatacksp()
	{
		return atacksp;
	}
	string getdefesasp()
	{
		return defesasp;
	}
	string getvelocidade()
	{
		return velocidade;
	}
	string getgeracao()
	{
		return geracao;
	}
	string getlegendary()
	{
		return legendary;
	}



  // Percorrer caminho esquerda
	No* getEsq()
	{
		return esq;
	}

  // Percorrer caminho direita
	No* getDir()
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
    int cont = 0;

  public:
    Arvore(){
      raiz = NULL;
    }

    // Função inserir para todas as variáveis
    void inserir(string nome, string dex, string tipo1,string tipo2,string total,string hp,string atack,string defesa,string atacksp, string defesasp,string velocidade,string geracao,string legendary)
    {
      if(raiz == NULL) 
        raiz = new No(nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary); 
      else{

          inserirAux(raiz, nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);

          cont += 1;
      } 
    }



    // Função inserir em uma nova árvore baseando-se na coluna "total"
    void inserirtotal(string nome, string dex, string tipo1,string tipo2,string total,string hp,string atack,string defesa,string atacksp, string defesasp,string velocidade,string geracao,string legendary)
    {
      if(raiz == NULL) 
        raiz = new No(nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary); 
      else
        {
          inserirAuxtotal(raiz, nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);

        cont += 1;
    }
    }



    void inserirAuxtotal(No *no,string nome, string dex, string tipo1,string tipo2,string total,string hp,string atack,string defesa,string atacksp, string defesasp,string velocidade,string geracao,string legendary){

      if(total < no->gettotal())
      {
        if(no->getEsq() == NULL)
        {
          No *novo_no = new No(nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);
          no->setEsq(novo_no); 
        }
        else
        {				
          inserirAuxtotal(no->getEsq(),nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);
        }
      }
      else if(total > no->gettotal())
      {
        if(no->getDir() == NULL)
        {
          No *novo_no = new No(nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);
          no->setDir(novo_no);
        }
        else
        {
          inserirAuxtotal(no->getDir(),nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);
        }
      }

    }
    
    

    void inserirAux(No *no,string nome, string dex, string tipo1,string tipo2,string total,string hp,string atack,string defesa,string atacksp, string defesasp,string velocidade,string geracao,string legendary){

      
      if(nome < no->getnome())
      {
        if(no->getEsq() == NULL)
        {
          No *novo_no = new No(nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);
          no->setEsq(novo_no); 
        }
        else
        {				
          inserirAux(no->getEsq(),nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);
        }
      }
      else if(nome > no->getnome())
      {
        if(no->getDir() == NULL)
        {
          No *novo_no = new No(nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);
          no->setDir(novo_no);
        }
        else
        {
          inserirAux(no->getDir(),nome, dex, tipo1,tipo2,total,hp,atack,defesa,atacksp, defesasp,velocidade,geracao,legendary);
        }
      }
    
    }


    No* getRaiz()
    {
      return raiz;
    }

    // Percorrer a árvore em ordem alfabetica pela coluna nomes
    void emOrdem(No* no)
    {
      if(no != NULL)
      {
        emOrdem(no->getEsq());
        cout << no->getnome()<<" | "<<no->gethp()<<" | "<<no->getatack()<<" | "<<no->getdefesa()<<" | "<<no->gettipo1()<<" | "<<no->gettipo2() <<" | "<<no->gettotal() << "\n";
        
        
        emOrdem(no->getDir());
      }
    }

     void maisforte(No* no)
    {
      if(no != NULL)
      {

       
  
        maisforte(no->getEsq());
 
         if(no->gettotal() > bicicleta1 ){
           bicicleta1 = no->gettotal();
           bicicleta2 = no->getnome();
         }
        
        maisforte(no->getDir());
      }
    }


    


    int localizar(string n,No* no){
      
      while(no != NULL)
      {
              if(n == no->getnome()){

                          cout << "\n\n\nPokedéx | Nome | Geração | Atributo1 | Atributo2 | Lendário | Hp | Ataque | Defesa  |  Ataque SP | Defesa SP | Total  \n";
          
                  cout << no->getdex()<<" | " << no->getnome()<<" | "<<no->getgeracao()<<" | "<<no->gettipo1()<<" | "<<no->gettipo2() << " | "  << no->getlegendary()<<" | " << no->gethp()<<" | "<<no->getatack()<<" | "<<no->getdefesa()<<" | " << no->getatacksp()<<" | " << no->getdefesasp()<<" | " << no->gettotal();
            return 1;
        }

        if(n < no->getnome()){
        
        no =  no->getEsq();

        }else{
        no =  no->getDir();
        }
      }
      return 0;
	}

    // Transferir Pokémon
 

    No * remove_nome (No *n, string nome) {
      if(getRaiz() == NULL) 
        return n;

      if (nome < n->getnome()){ 
        n->setEsq(remove_nome(n->getEsq(), nome)); 
      }

      else if (nome > n->getnome()){ 
        n->setDir(remove_nome(n->getDir(), nome)); 
      }

      else{ 
        if (n -> getEsq() == NULL) { 
          No *temp = n->getDir();
          free(n);                 
          return temp;             
        } 

        else if (n->getDir() == NULL) { 
          No* temp = n->getEsq();
          free(n); 
          return temp;           
        }

       
             No* var = n->getDir();
      while (var -> getEsq() != NULL) 
        var = var->getEsq();
      No* temp = var;

        n->setnew(temp -> getnome(), temp -> getdex(),temp -> gettipo1(),temp -> gettipo2(),temp -> gettotal(),temp -> gethp(),temp -> getatack(),temp -> getdefesa(),temp -> getatacksp(),temp -> getdefesasp(),temp -> getvelocidade(),temp -> getgeracao(),temp -> getlegendary()); 

        n -> setDir(remove_nome(n->getDir(), temp->getnome())); 
      }
      return n; 
    }

    // Função mostrar todos os elementos (colunas e valores)
    void todos(No* no)
    {
      if(no != NULL)
      {
        todos(no->getEsq());


     

        cout << no->getdex()<<" | " << no->getnome()<<" | "<<no->getgeracao()<<" | "<<no->gettipo1()<<" | "<<no->gettipo2() << " | "  << no->getlegendary()<<" | " << no->gethp()<<" | "<<no->getatack()<<" | "<<no->getdefesa()<<" | " << no->getatacksp()<<" | " << no->getdefesasp()<<" | " << no->gettotal();
        
        todos(no->getDir());
      }
    }

 





  };


 






///////////////////////////////////////////////

// Iniciar uma matriz que armanezará todos os valores
string matriz[800][13];

int main(){

    // Criação de duas árvores, uma para ordenar por nomes e outra para o valor da coluna"total"
    Arvore arv;
    Arvore arvtotal;

   
    int menu;

    cout << "\033c";
    ifstream myfile;
    myfile.open("pokemon.csv"); // Nome do arquivo, deve estar baixado na mesma pasta do código.

    int cont1 = -1;
    int cont2 = 0;
    while(myfile.good()){  // Enquanto o arquivo estiver aberto
      
      string line;
      getline(myfile,line,',');
      
      if(line == ""){
        line = "0";
      }

      ///cout  << line << " ";
      cont1++;
      
      
      if(cont1 == 13){  // Quebra de linhas para armazenar na matriz
        
        cont1 = 0;
        cont2++;
      }


      
      matriz[cont2][cont1] = line; // Armazenar valor lido na matriz

  
      
    }

    
    // // Mostrar matriz
    // cout << " \n\n\n\n\n\n";
    // for(int x = 0; x < 800; x++){
    //   cout << " ";
    //   for(int y = 0; y < 13; y++){
    //     cout << "   ";
    //     cout << matriz[x][y];
    //    }
    //  }
    
    myfile.close(); // Fechar Arquivo


    

    for(int x = 0; x < 800; x++){
      arv.inserir(matriz[x][1],matriz[x][0],matriz[x][2],matriz[x][3],matriz[x][4],matriz[x][5],matriz[x][6],matriz[x][7],matriz[x][8],matriz[x][9],matriz[x][10],matriz[x][11],matriz[x][12]);
    }
    
    
    for(int x = 0; x < 800; x++){
      arvtotal.inserirtotal(matriz[x][1],matriz[x][0],matriz[x][2],matriz[x][3],matriz[x][4],matriz[x][5],matriz[x][6],matriz[x][7],matriz[x][8],matriz[x][9],matriz[x][10],matriz[x][11],matriz[x][12]);
    }


    // Menu
    while(true){
        cout << "\n\n---------------------------------------------\n";
        cout<<" 0	- sair	do	programa \n";
        cout<<" 1	- Printar Pokémons Em Ordem Alfabetica  \n";
        cout<<" 2	- Todas as informações pokémons (tabela)\n";     
        cout<<" 3  - Achar pokemon por Nome\n";
        cout<<" 4  - Ordenar por mais forte\n";
        cout<<" 5  - Achar mais forte\n";    
        cout<<" 6  - Excluir pokemon por nome\n";      
        cout<<"";
        



        cout << "---------------------------------------------\n";


        cout<<"\nDigite: ";
        cin>>menu;
        cout << "\033c";
        


        if(menu == 0){ 
          break; 
        }

        else if(menu == 1){ // Percorrer arvore em Ordem alfabetica
          
          cout << "Nome | Hp | Ataque | Defesa | Atributo | Atributo2 | Total\n\n";
          arv.emOrdem(arv.getRaiz());

        }

        
        else if(menu == 2){ // Mostrar todas as informações do csv 
          
          cout << "Pokedéx | Nome | Geração | Atributo1 | Atributo2 | Lendário | Hp | Ataque | Defesa  |  Ataque SP | Defesa SP | Total  \n";
          arv.todos(arv.getRaiz());
          
        }
        
        else if(menu == 3){ // Achar pokémon por nome

          string pok;
          
          cout << "Digite o nome do pokémon que deseja buscar (Pikachu, Charizard, etc): ";
          cin >> pok;

          
          arv.localizar(pok,arv.getRaiz());
          



        }

        else if(menu == 4){ // Ordenar por mais forte

          cout << "Nome | Hp | Ataque | Defesa | Atributo | Atributo2| Total\n\n";
          
          
          arvtotal.emOrdem(arvtotal.getRaiz());
          

        }

        else if(menu == 5){ // Mostrar pokémon mais forte

          cout << "Pokémon mais Forte: ";
          arvtotal.maisforte(arvtotal.getRaiz());
          arv.localizar(bicicleta2,arv.getRaiz());

        }
        else if(menu == 6){ // Remover ou transfeir

          string pok;
          
          cout << "Digite o nome do pokémon que deseja excluir (Pikachu, Charizard, etc): ";
          cin >> pok;

          
          arv. remove_nome(arv.getRaiz(),pok);

        }

       

    }
  


}
