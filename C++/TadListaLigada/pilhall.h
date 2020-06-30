
#ifndef TADPILHALL_H
#define TADPILHALL_H

#include "ListaLigada.h"

class TadPilhaLL {

	private:
	ListaLigada * lista;

	public:
	TadPilhaLL();
	bool push(int v);
	int pop();
	int procura(int v);
	int quantidade();
	void imprime();
	
};


#endif
