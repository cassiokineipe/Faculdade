// Jogo da Vida Conway

// Cassio Kineipe - 31929265
// Rafael Lua     - 31948571




// Regras gerais:
    // Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
    // Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
    // Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
    // Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração


// Estrutura do código:
  // aplica as regras no real
  // modifica o estado deixando-o na geração seguinte
  // igualar real e estado


#include <stdio.h>
#include<stdlib.h>
#include <unistd.h>   // Tempo




int estado[25][250] = {0};
int real[25][25] = {0};


int vizinhos(int x){

    //                Vizinhos e suas posições na matriz

    //           [Y - 25 - 1]      [Y - 25]       [Y - 25 + 1] 
    //             [Y - 1]           [Y]            [Y + 1]
    //           [Y + 25 - 1]      [Y + 25]       [Y + 25 + 1]





  int cont = 0;
  
  // calculo vetor transformado em matriz
  int linha = x / 25;
  int coluna = x % 25;


  // Contando numero de vizinhos
  if (coluna + 1 < 25){
    if (real[linha][coluna + 1] == 1){
      cont += 1;
    }
  }

  if (coluna - 1 >= 0){
    if (real[linha][coluna - 1] == 1){
      cont += 1;
    }
  }

  if (linha + 1 < 25){
    if (real[linha + 1][coluna] == 1){
      cont += 1;
    }
  }

  if (linha - 1 >= 0){
    if (real[linha - 1][coluna] == 1){
      cont += 1;
    }
  }

  if (linha + 1 < 25 && coluna - 1 >= 0){
    if (real[linha + 1][coluna - 1] == 1){
      cont += 1;
    }
  }

  if (linha + 1 < 25 && coluna + 1 < 25){
    if (real[linha + 1][coluna + 1] == 1){
      cont += 1;
    }
  }

  if (linha - 1 >= 0 && coluna - 1 >= 0){
    if (real[linha - 1][coluna - 1] == 1){
      cont += 1;
    }
  }

  if (linha - 1 >= 0 && coluna + 1 < 25){
    if (real[linha - 1][coluna + 1] == 1){
      cont += 1;
    }
  }





  return cont;
  
}


// Printar tabuleiro
void tabuleiro(){ 
  printf("\033c");
  //printf("\n\n\n");
  
  for(int i=0;i<25;i++){
      
      for(int c=0;c<25;c++){

        printf("%d ",real[i][c]);
    
    }
    printf("\n");

    
  }
  


}

// Verificar Regras ja listadas para o elemento em questão
int regras(int cont,int x){

  int momento = 0;

  int l = x/25;
  int c = x%25;
      
  if(real[l][c] == 1){

    momento = 1;
  }
    if(real[l][c] == 0){

    momento = 0;
  }

  int estado = 0;

  if(momento == 1){
    if (cont < 2){
      estado = 0;
    }
    else if (cont > 3){
      estado = 0;
    }
    else if (cont == 2 ){
      estado = 1;
    }
    else if (cont == 3 ){
      estado = 1;
    }
  }

  if(momento == 0){
    if (cont==3){
      estado = 1;
    }
    
    
  }

  return estado;


}
  


// Principal
int main(void) {

  
  // Adicionar as posições digitadas pelo usuário no tabuleiro
  while(1){

    int num;
    printf("Digite um valor de 0 a 624 (999 quando desejar encerrar): ");


    scanf("%d", &num);
    
    // Se for = a 999 finalizar while e começar a execução do programa
    if (num == 999){
      break;

    }

    // Calculo vetor transformado em matriz
    int l = num/25;
    int c = num%25;

    real[l][c] = 1;
    estado[l][c] = 1;


  }
  // Mostrar tabuleiro
  tabuleiro();
  
  
  
  while(1){
    
    
    // Atualizar Estado com base nas regras
    for (int x = 0; x < 625; x++){
        

        
        int linha = x / 25;
        int coluna = x % 25;

        int viz = vizinhos(x);
        estado[linha][coluna] = regras(viz,x);


        
      
    }

        
    sleep(3);    // Tempo de 3 segundos
    

    // Igualar Real com Estado 
    for(int x = 0; x < 625; x++){

          int l = x / 25;
          int c = x % 25;
          
        
          if(estado[l][c] == 1){
            real[l][c] = 1;
          }
          if(estado[l][c] == 0){
            real[l][c] = 0;
          }


    }
        tabuleiro();

        
        
    }

    

  return 0;
}
