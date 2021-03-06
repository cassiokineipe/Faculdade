#include <iostream>
#include <stdlib.h>

using namespace std;
struct Node{
  public:
	int info;
	Node *proximo,*anterior;
	Node() {
	  proximo=anterior=NULL;
	}
	Node(int e1, Node *a=NULL,Node*p=NULL){
		info=e1;proximo=p,anterior=a;
	}
};

class ListaDuplamente{
  private:
	Node *primeiro, *ultimo;

  public:
	ListaDuplamente(){
		primeiro=ultimo=NULL;
	}
	~ListaDuplamente();
	bool vazia(){
		return primeiro==NULL;
	}
	bool insereinicio(int);
	bool inserefinal(int);
	bool insere(int);
	bool removeprimeiro(int &);
	bool removeultimo(int &);
	bool remove(int);
//	int isInList(int) const;
	void printList();
	void inverseprintList();
};

ListaDuplamente::~ListaDuplamente(){
  int x;                                    
  while(!vazia())
    removeprimeiro(x);
// ultimo = NULL;
}
bool ListaDuplamente::insereinicio(int el){
   Node *novo = new Node(el,NULL,primeiro);
   if (novo==NULL) return false;
   if(primeiro!=NULL){
      primeiro->anterior = novo;
      primeiro = novo;
   }
   else
	ultimo = primeiro = novo;
   return true;
}

bool ListaDuplamente::inserefinal(int el){
 Node *novo = new Node(el,ultimo,NULL);
 if (novo == NULL) return false;
 if(ultimo!=NULL){
	ultimo->proximo=novo;
    ultimo=novo;
 }
 else{
	primeiro = ultimo = novo;
 }
 return true;
}

bool ListaDuplamente::insere(int el){
  Node *novo;
  novo = new Node(el,NULL,NULL);
  if (novo == NULL) return false;
  if(ultimo==NULL){//primeiro no
     ultimo = primeiro = novo;
  }
  else{
     Node *aux=primeiro;
     while(aux!=NULL && el>aux->info){
        aux = aux->proximo;
     }
     if(el<=primeiro->info){
       novo->proximo = primeiro;
       primeiro->anterior = novo;
       primeiro = novo;
     }
     else if(aux==NULL){//inserir depois do ultimo
        ultimo->proximo = novo;
        novo->anterior = ultimo;
        ultimo = novo;
     }
     else{//inserir no meio
        aux->anterior->proximo=novo;
        novo->anterior = aux->anterior;
        novo->proximo=aux;
        aux->anterior = novo;
     }
  }
  return true;
}

bool ListaDuplamente::removeprimeiro(int &el){
 if(vazia()) return false;    
 el = primeiro->info;
 Node *tmp = primeiro;
 if(primeiro == ultimo)
	primeiro = ultimo = NULL;
 else {
  primeiro = primeiro->proximo;
  primeiro->anterior=NULL;
 }
 delete tmp;
 return true;
}

bool ListaDuplamente::removeultimo(int &el){
 if(vazia()) return false;     
 el = ultimo->info;
 if(primeiro==ultimo){
	delete primeiro;
	primeiro = ultimo = NULL;
 }
 else {
	ultimo = ultimo->anterior;
	delete ultimo->proximo;
	ultimo->proximo = NULL;
 }
 return true;
}

bool ListaDuplamente::remove(int el){
 if(vazia()) return false;
 if(primeiro==ultimo &&el==primeiro->info){
		delete primeiro;
		primeiro = ultimo = NULL;
	}
 else if(el==primeiro->info){
		Node *tmp=primeiro;
		primeiro = primeiro->proximo;
		primeiro->anterior = NULL;
		delete tmp;
 }
 else {
		Node *ant, *tmp;
		ant = primeiro;
		tmp = primeiro->proximo;
		while(tmp!=NULL && tmp->info !=el){
                        ant = tmp;
                        tmp = tmp->proximo;
        }
	    if(tmp == NULL) return false;

        ant->proximo=tmp->proximo;
		if(tmp==ultimo){
    		ultimo=ant;}
        else{
          tmp->proximo->anterior = ant;
          }
	delete tmp;
 }
  return true;
}


void ListaDuplamente::printList()
{
  Node *tmp;
  cout<<"\nLista: ";
  for(tmp=primeiro;tmp!=NULL;tmp=tmp->proximo)
	cout<<tmp->info<<" ";

}

void ListaDuplamente::inverseprintList()
{
     Node *tmp = ultimo;
     cout<<"\nLista inversa: ";
     while(tmp!=NULL){
      	cout<<tmp->info<<" ";
      	tmp = tmp->anterior;
     }
}

int main()
{
     int n;
     ListaDuplamente L;
     cout<<"Digite o numero a ser inserido";
     cin>>n;
     while(n!=-1){
      L.insere(n);
      L.printList();
      L.inverseprintList();
      cout<<"Digite o numero";
      cin>>n;
     };
     system("PAUSE");
     cout<<"Digite o numero a ser removido";
     cin>>n;
     while(n!=-1){
      L.remove(n);
      L.printList();
      L.inverseprintList();
      cout<<"Digite o numero";
      cin>>n;
     };
    system("PAUSE");
    return 0;

}