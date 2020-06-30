#include <cstdlib>
#include <iostream>
#include <sstream>
#include "Celula.h"
#include "ListaLigada.h"

using namespace std;


ListaLigada::ListaLigada() {
	prim = NULL;
	qtdCelulas = 0;
}

bool ListaLigada::vazia() {
	return prim == NULL;
}

int ListaLigada::tamanho() {
	return this->qtdCelulas;
}

void ListaLigada::insereInicio(int i) {
	Celula * c = new Celula(i);
	c->setProx(prim);
	prim = c;
	qtdCelulas++;
}

Celula * ListaLigada::removeInicio() {
	if (vazia()) return NULL;
	Celula * aux = prim;
	prim = prim->getProx();
	aux->setProx(NULL);
	qtdCelulas--;
	return aux;
}

string ListaLigada::insereEmN(Celula * c, int pos) {

	stringstream ss;

	while (true) {

		// int x = 2;

		if (pos < 1) {
			ss << "A posicao deve ser maior ou igual a 1";
			break;
		}

		if (pos > qtdCelulas + 1) {
			ss << "Nao existe esta posicao. A fila esta' com " << qtdCelulas << " elemento(s)";
			break;
		}

		if (pos == 1) {
			insereInicio(c->getInfo()); // o metodo insereInicio ja' estava implementado; aqui foi feita uma adaptacao.
			ss << "Inserido no inicio";
			break;
		}

		Celula * cursor = this->prim;
		for (int i = 1; i < pos - 1; i++) {
			cursor = cursor->getProx();
		}

		c->setProx(cursor->getProx());
		cursor->setProx(c);

		qtdCelulas++;

		ss << "Inserido na posicao " << pos;

		break;




	}




	return ss.str();

}


void ListaLigada::imprime() {
	Celula * cursor = prim;
	cout << "[ ";
	while (cursor != NULL) {
		cout << cursor->getInfo() << " ";
		cursor = cursor->getProx();
	}
	cout << "]\n";
}


int ListaLigada::localiza(int v){
	
	
	return 0;
	
}



