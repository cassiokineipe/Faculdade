// Cássio Kineipe - 31929265
// Rafael Lua - 31948571

#include <stdio.h>
#include <math.h>

// PARA ALTERAR O NUMERO DE DISCOS, MUDE O NÚMERO DO VETOR 
//      ABAIXO E OS NUMEROS DENTRO DO VETOR

int p1[7] = {7,6,5,4,3,2,1}; /// Pilha inicial 
int p2[(sizeof(p1)/4)];
int p3[sizeof(p1)/4];


int var1,var2,var3 = 0; // Variáveis usadas para mostrar as posições


int hanoi(cont){ // Função para resolver a torre de hanoi 
  
  int ultimo = 0; // Não permite que o ultimo elemento que foi trocado de pilha seja colocado nela mesma logo em seguida

  int qtd2,qtd3 =0; /// Quantidade de elementos em cada pilha

  int qtd1 = (sizeof(p1)/4-1);
  

  int o = (pow(2,qtd1+1)) - 1; // Cálculo para o numero exato de vezes que o loop precisa ocorrer (2^n)-1

  

if(qtd1%2 == 0){// SE FOR PAR, LER PARA A DIREITA


  while(cont < o){ // Único loop
  

    cont += 1; // Conta o número de passos 

    if(qtd2==-1){ 
      qtd2 = 0;
    }
     if(qtd3==-1){
      qtd3 = 0;
    }
     if(qtd1==-1){
      qtd1 = 0;
    }

    // Condições para validação do movimento de peças para duas pilhas

     if(p3[qtd3] < p2[qtd2] && ultimo != 3){
      p2[qtd2+1] = p3[qtd3];
      p3[qtd3] = 99999;
      qtd3--;
      qtd2++;
      ultimo = 2;

    } else if(p3[qtd3] < p1[qtd1] && ultimo != 3){
      p1[qtd1+1] = p3[qtd3];
      p3[qtd3] = 99999;
      qtd3--;
      qtd1++;
      ultimo = 1;

    }
     else if(p2[qtd2] < p1[qtd1] && ultimo != 2){
      
      p1[qtd1+1] = p2[qtd2];
      p2[qtd2] = 99999;
      qtd2--;
      qtd1++;
      ultimo = 1;
    }   else if(p2[qtd2] < p3[qtd3] && ultimo != 2){
      p3[qtd3+1] = p2[qtd2];
      p2[qtd2] = 99999;
      qtd2--;
      qtd3++;
      ultimo = 3;

    }   else if(p1[qtd1] < p3[qtd3] && ultimo != 1){

      if(p3[0] == 99999){
        p3[0] = p1[qtd1];
        qtd3 = 0;
      }
      else{
        p3[qtd3+1] = p1[qtd1];
        qtd3++;

      }
    
      
      p1[qtd1] = 99999;
      qtd1--;
     
      ultimo = 3;
    }else  if(p1[qtd1] < p2[qtd2] && ultimo != 1){ // Verifica se o ultimo valor da pilha 1 é menor que o ultimo da pilha 2 para desloca-lo

      if(p2[0] == 99999){
        p2[0] = p1[qtd1];
        qtd2 = 0;
      }
      else{
        p2[qtd2+1] = p1[qtd1];
        qtd2++;

      }
      
      p1[qtd1] = 99999;
      qtd1--;
      
      ultimo = 2;
    }

    // Interface gráfica da torre de Hanoi, base esta em cima
    printf("\n%d",cont);
    printf("\n  P1    P2    P3\n-----------------\n");
    for(int i=0; i < sizeof(p1)/4; i++){

        int var1,var2,var3;
        if (p1[i] == 99999){
          var1 = 0;
        }
        else{
          var1 = p1[i];
        }
        if (p2[i] == 99999){
          var2 = 0;
        }
        else{
          var2 = p2[i];
        }
        if (p3[i] == 99999){
          var3 = 0;
        }
        else{
          var3 = p3[i];
        }

        printf("  %d   ",var1);
        printf("  %d   ",var2);
        printf("  %d   ",var3);
        printf("\n");
      }

  }




}
else{ // SE FOR IMPAR O NUMERO DE DISCOS, LER PARA A ESQUERDA




  while(cont < o){ // Único loop
  

    cont += 1; // Conta o número de passos 

    if(qtd2==-1){ 
      qtd2 = 0;
    }
     if(qtd3==-1){
      qtd3 = 0;
    }
     if(qtd1==-1){
      qtd1 = 0;
    }

    // Condições para validação do movimento de peças para duas pilhas

    if(p1[qtd1] < p2[qtd2] && ultimo != 1){ // Verifica se o ultimo valor da pilha 1 é menor que o ultimo da pilha 2 para desloca-lo

      if(p2[0] == 99999){
        p2[0] = p1[qtd1];
        qtd2 = 0;
      }
      else{
        p2[qtd2+1] = p1[qtd1];
        qtd2++;

      }
      
      p1[qtd1] = 99999;
      qtd1--;
      
      ultimo = 2;
    }
    else if(p1[qtd1] < p3[qtd3] && ultimo != 1){

      if(p3[0] == 99999){
        p3[0] = p1[qtd1];
        qtd3 = 0;
      }
      else{
        p3[qtd3+1] = p1[qtd1];
        qtd3++;

      }
    
      
      p1[qtd1] = 99999;
      qtd1--;
     
      ultimo = 3;
    }
    else if(p2[qtd2] < p3[qtd3] && ultimo != 2){
      p3[qtd3+1] = p2[qtd2];
      p2[qtd2] = 99999;
      qtd2--;
      qtd3++;
      ultimo = 3;

    }
    else if(p2[qtd2] < p1[qtd1] && ultimo != 2){
      
      p1[qtd1+1] = p2[qtd2];
      p2[qtd2] = 99999;
      qtd2--;
      qtd1++;
      ultimo = 1;
    }
    else if(p3[qtd3] < p1[qtd1] && ultimo != 3){
      p1[qtd1+1] = p3[qtd3];
      p3[qtd3] = 99999;
      qtd3--;
      qtd1++;
      ultimo = 1;

    }
    else if(p3[qtd3] < p2[qtd2] && ultimo != 3){
      p2[qtd2+1] = p3[qtd3];
      p3[qtd3] = 99999;
      qtd3--;
      qtd2++;
      ultimo = 2;

    }

    // Interface gráfica da torre de Hanoi, base esta em cima
    printf("\n%d",cont);
    printf("\n  P1    P2    P3\n-----------------\n");
    for(int i=0; i < sizeof(p1)/4; i++){

        int var1,var2,var3;
        if (p1[i] == 99999){
          var1 = 0;
        }
        else{
          var1 = p1[i];
        }
        if (p2[i] == 99999){
          var2 = 0;
        }
        else{
          var2 = p2[i];
        }
        if (p3[i] == 99999){
          var3 = 0;
        }
        else{
          var3 = p3[i];
        }

        printf("  %d   ",var1);
        printf("  %d   ",var2);
        printf("  %d   ",var3);
        printf("\n");
      }

  }
}

  return cont;
}



int main(void) {

  for(int i=0; i < sizeof(p1)/4; i++){ // Inicializa as duas pilhas com um valor  maior que todos os outros presentes na pilha 1
    p2[i] = 99999;
  }

  for(int i=0; i < sizeof(p1)/4; i++){
    p3[i] = 99999;
  }



  int cont = 0;
  printf("\n\n%d movimentos",hanoi(cont)); //Chama a função


}





