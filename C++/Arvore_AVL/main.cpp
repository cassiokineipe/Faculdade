// Cassio Kineipe - 31929265
// Rafael Lua - 31948571  


#include <iostream>

#include "AVLNode.h"
#include "AVLTree.h"


using namespace std;

int main() {
    cout << "\033c";
    AVLTree a1;
    a1.inserir(5);
    a1.inserir(15);
    a1.inserir(46);
    a1.inserir(39);
    a1.inserir(11);
    a1.inserir(3);
   
 

    int opc;
    
   while(true){
     
     cout<<"\nArvore AVL: \n";
     cout<<"\n";
     cout<<"--------------------------------\n";
     cout << "0 - Parar programa: \n";
     cout << "1 - Inserir elemento na arvore:\n";

     cout << "2 - REMOVER ELEMENTO:\n";

     cout<<  "3 - Altura da arvore: \n";
     cout<<  "4 - Arvore em ordem: \n";
     cout<<  "5 - Arvore pós ordem: \n";
     cout<<  "6 - Arvore pré ordem: \n";
     cout<<  "7 - Arvore reversa: \n";
     cout<<"--------------------------------\n\n\n";


     cin>>opc;

     if(opc==0){break;}

     if(opc==1){
       int n;
       cout<<"\nDigite o elemento a inserir:\n";
       cin>>n;
       a1.inserir(n);
     
     }
     if(opc==2){
       // REMOVER ELEMENTO
       int n;
       cout<<"\nDigite o elemento a remover:\n";
       cin>>n;
       a1.remover(n);

     




     
     }
      
      if(opc==3){
        cout<<"\n";
       cout<<a1.height();
       
     }
      if(opc==4){
        cout<<"\n";
       a1.inOrder();
     }
      if(opc==5){
       cout<<"\n";
       a1.posOrder();
      
     }
      if(opc==6){
        cout<<"\n";
        a1.preOrder();

     }
      if(opc==7){
        cout<<"\n";
        a1.reverseOrder();
     }



   }
    

    
    return 0;
}