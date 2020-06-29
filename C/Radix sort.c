// RaddixSort usando Bubble Sort

// Cassio Kineipe - 31929265
// Rafael Lua - 31948571

# include <stdio.h> 
# include <stdlib.h> 
#include <math.h>




int main(void){
  int n;

  
  printf("\nDigite o numero de elementos: ");
  scanf("%d", &n);
  int vet[n]; // Criar vetor com base no tamanho escolhido
  for(int c=0; c<n;c++){
    int b;
    printf("Digite o elemento de index %d : ",c); // Qualquer tamanho
    scanf("%d", &b);
    vet[c] = b;
  }
  
  
  
  
  
  int tam = sizeof(vet)/4;  // Calcular tamanho oficial


  
  printf("\n\nOriginal: ");
  for(int t = 0; t < tam; t++){
    printf("%d ",vet[t]);
    
  }

  printf("\n");


  int maior = vet[0]; // Definir maior elemento como primeiro




  for (int d = 0; d < tam; d++ ){ // Identificar maior elemento real
    if (vet[d] > maior){
      maior = vet[d];

    }
  }

  // Identificar numero de casas do maior elemento
  int casasMaior = 0;
  int val = maior;
  while (val >= 1){  
    val = val/10;
    casasMaior += 1;
  }


          
  int fim[tam][casasMaior]; // Inicializar vetor final

  for (int v = 0; v < tam; v++){ // Zerar e inicializar vetor
    for(int w = 0; w < casasMaior; w++){
      fim[v][w] = 0;

    }


  }

  // Print para testes

  // printf("\ntam: %d",tam);
  // printf("\ncasas: %d\n\n\n",casasMaior);


  for (int ya = 0; ya < tam; ya++){ // Repetição. Percorrer a lista e salvar numeros
  
    int num = vet[ya];
    int aux = num;
    int cont = 0;

    while (aux >= 1){  // Identifica tamanho do numero
      aux = aux/10;
      cont += 1;
    }
      
    int var;
    int var2;
    int cont2 = 1;

    int varHelp = 0;

    int oficial[cont]; // Vetor que vai armazenar o numero invertido
    
    int helpOficial = 0;

    for (int x = 0; x < cont; x++){
      
      int pot = pow(10,cont2);  // Gerar potencia do resto

      
      if (pot == 0){            // Para evitar erros, se for 0 definir como 1
        pot = 1;
      }
      
      int var = num%(pot);        // Calcular o valor da casa(10Dezena = 10, 1724Centena = 724, etc)
      
      int pot2 = pow(10,cont2-1); // Gerar segunda potencia
      
      if (pot2 == 0){             // Para evitar erros, se for 0 definir como 1
        pot2 = 1;
      }
      
      int var2 = (var - varHelp)/pot2;   
      // Calcular o valor da casa naquela posição (10 Dezena = 1, 170 Centena = 1, etc)
      

      varHelp = var; // Variavel auxiliar para fazer a proxima casa
      
      oficial[helpOficial] = (var2); // Adicionar o numero no vetor oficial
      fim[ya][helpOficial] = var2;   // Adicionar valor no fim
      
      helpOficial += 1;


      cont2 += 1;
      
      }
        
  }

  // Printar vetor invertido antes de ordena-lo

  // printf("\n\n\n\n\nInvertido:\n");
  // for (int p = 0; p < tam; p++){
  //   printf("\n");
  //   for (int g = 0; g < casasMaior;g++){
  //     printf("%d ",fim[p][g]);      
  //   }
  // }
  


  printf("\n-------------\n\nOrdenado por RaddixSort: ");





  int maior2 = casasMaior;
  
  int guard[maior2]; // Vetor auxiliar 
   
  int tam2 = sizeof(fim)/4;
  tam2 = tam2/maior2;

 
 
  for(int i=0;i<tam2;i++){
   for(int b=0;b<tam2;b++){ // Realizacao do Bubble Sort
    for(int c=0;c<tam2-1;c++){
    

    if(fim[c][i] > fim[c+1][i] ){ // Compara cada posicao
 
     
      for(int x=0;x<maior2;x++){ //  Troca os elementos 
        guard[x] = fim[c][x];
        fim[c][x] = fim[c+1][x];
        fim[c+1][x] = guard[x];
          
      }
      
    }
    
    }
  }
  
  }
  



  
  for (int p = 0; p < tam; p++){ // Printar os elementos em ordem
    printf(" ");
    int var = 0;
    for (int g = casasMaior-1; g >=0 ;g--){
     


      if(fim[p][g] != 0 || var == 1){
        printf("%d",fim[p][g]);
        var =1;
      }
      
    
    
    }


  }
  printf("\n\n");
    
}

