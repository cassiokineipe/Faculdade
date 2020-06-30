
#include "pilhall.h"


TadPilhaLL::TadPilhaLL(){
	lista = new ListaLigada();
}


bool TadPilhaLL::push(int v){
	lista->insereInicio(v);
	return true;
}


void TadPilhaLL::imprime(){
	lista->imprime();
}