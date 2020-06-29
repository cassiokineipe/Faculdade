
#include <stdio.h>
#include <iostream>
using namespace std;
# include "jogo.h"


int main()
{
 
  int opc,escolha,tentativas = 0 ;
  Pilha P1,P2,P3;

  P1.definir();// gera os valores na primeira pilha

  



  cout<<"  Torre de Hanoi";

 while(true){
       // limpa a tela
 system("clear");
 cout<<"\n";
   
   cout<<"\n\n P1 = ";
  P1.imprime();
  cout<<"\n\n P2 = ";
  P2.imprime();
  cout<<"\n\n P3 = ";
  P3.imprime();
  cout<<"\n\n\n Numero de tentativas = "<<tentativas;

   P2.verifica();// verifca se o jogador ganhou
   P3.verifica();
  
  /// menu de opcoes
  cout << "\n\n";
 
  cout <<"0-encerrar programa\n";
  cout <<"1-Mover elemneto \n";

  
  
  
  /// pega a escolha do usuario
  cin>> opc;


  if(opc == 0)break; // termina o jogo

 else if (opc == 1){ // vai mover os elementos
  int escolha;
 cout<< "Escolha a pilha para ser movimentada(1/2/3):"; // escolher a pilha inicial
 cin>>escolha;

 int x,y,z,opc2;

 if(escolha == 1){
   if (P1.ehvazia() == false){

     

     P1.top(x);
     
     cout<<"Em qual pilha deseja posicionar(2/3):\n"; // escolher a pilha final
     cin>>opc2;
     if (opc2 == 2){
       if (P2.ehvazia() == true){
         P2.push(x);
         P1.pop();
         tentativas++;
       }else{
         P2.top(y);
          if(y>x){

            P2.push(x);
            P1.pop();
            tentativas++;
          }
         
       }

     }
          if (opc2 == 3){
       if (P3.ehvazia() == true){
         P3.push(x);
         P1.pop();
         tentativas++;
       }else{
         P3.top(y);
          if(y>x){

            P3.push(x);
            P1.pop();
            tentativas++;
          }
         
       }

     }




   }
 }

 if(escolha == 2){
   if (P2.ehvazia() == false){

     

     P2.top(x);
     
     cout<<"Em qual pilha deseja posicionar(2/3):\n";
     cin>>opc2;
     if (opc2 == 1){
       if (P1.ehvazia() == true){
         P1.push(x);
         P2.pop();
         tentativas++;
       }else{
         P1.top(y);
          if(y>x){

            P1.push(x);
            P2.pop();
            tentativas++;
          }
         
       }

     }
          if (opc2 == 3){
       if (P3.ehvazia() == true){
         P3.push(x);
         P2.pop();
         tentativas++;
       }else{
         P3.top(y);
          if(y>x){

            P3.push(x);
            P2.pop();
            tentativas++;
          }
         
       }

     }




   }
 }
    if(escolha == 3){
   if (P3.ehvazia() == false){

     

     P3.top(x);
     
     cout<<"Em qual pilha deseja posicionar(2/3):\n";
     cin>>opc2;
     if (opc2 == 2){
       if (P2.ehvazia() == true){
         P2.push(x);
         P3.pop();
         tentativas++;
       }else{
         P2.top(y);
          if(y>x){

            P2.push(x);
            P3.pop();
            tentativas++;
          }
         
       }

     }
          if (opc2 == 1){
       if (P1.ehvazia() == true){
         P1.push(x);
         P3.pop();
         tentativas++;
       }else{
         P1.top(y);
          if(y>x){

            P1.push(x);
            P3.pop();
            tentativas++;
          }
         
       }

     }




   }

 }
 


 }


 }



 }
