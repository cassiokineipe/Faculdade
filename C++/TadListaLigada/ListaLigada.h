#include <iostream>
#include <string.h>
#include "Celula.h"

using namespace std;

class ListaLigada {
	
	//= privado
	private:
	Celula * prim;
	int qtdCelulas;
	
	//= publico
	public:
	ListaLigada();
	bool vazia();
	int tamanho();
	void insereInicio(int i);
	Celula * removeInicio();
	int localiza(int v); // retorna a posicao em que se encontra o elemento, ou -1 se nao estiver na lista
	string insereEmN(Celula * c, int pos);
	void imprime();
	// ... outros métodos ...
	
};
