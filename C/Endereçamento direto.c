#include <stdio.h>
#include <stdlib.h>


/// endereçamento direto, ordena em O(N)

int vetor[] = {1,2,1,6,2,2,9,1,6};



int main(void) {
   int  tam = sizeof(vetor);
 int maior = vetor[0];



 
  for(int i = 0;i<tam;i++){
    if(maior<vetor[i]){
      maior = vetor[i];
    }
  }
   maior++;
   
         printf("\n Vetor inicial:");
     for(int i = 0;i<maior;i++){
   printf("%d",vetor[i]);
    
    }


    int *aux;
    aux = malloc (maior * sizeof (int));
    
     for(int i = 0;i<maior;i++){
    aux[i] = 0;
    }
 for(int i = 0;i<maior-1;i++){
    aux[vetor[i]] = aux[vetor[i]] + 1;
    }
    int cont = 0;
     for(int i = 0;i<maior;i++){
    
         for(int c = 0;c<aux[i];c++){
    vetor[cont] = i;
    cont++;
    
    }
    }
    printf("\n \n \n Vetor ordenado:");
     for(int i = 0;i<maior;i++){
   printf("%d",vetor[i]);
    
    }
  
  return 0;
}