/**
 * Exercicio TAD PILHA com estrutura de armazenamento em LISTA LIGADA
 *                      prof. Marcio Feitosa
 */

#include <iostream>
#include <stdlib.h>

#include "pilhall.h"

#define VISIVEL 0 //1 = pode ver o conteudo da pilha; 0 = nao pode ver

using namespace std;

int main() {

	TadPilhaLL * pilhall;
	pilhall = new TadPilhaLL();

	while (true) {
		system("cls");
		cout << "------------------------------------------------------------------";
		cout << "\n   PROGRAMA PARA ESTUDO DO TAD PILHA UTILIZANDO LISTA LIGADA";
		cout << "\n------------------------------------------------------------------";
		cout << "\n0 - sair";
		cout << "\n1 - inserir";
		cout << "\n2 - remover";
		cout << "\n3 - verificar se um elemento esta' na pilha (retorna a posicao)";
		cout << "\n4 - quantidade de elementos na pilha";
		cout << "\n5 - imprimir a pilha";
		cout << "\n\nOpcao: ";
		int opc;
		cin >> opc;
		if (opc == 0) {
			break;
		} else if (opc == 1) {
			cout << "\nValor do novo elemento: ";
			int opc2;
			cin >> opc2;
			if (pilhall->push(opc2)) {
				cout << "\nInclusao bem sucedida. ";
			} else {
				cout << "\nERRO: falha na inclusao. ";
			}
		} else if (opc == 3) {
			if (VISIVEL == 0) {
				cout << "\n*** Opcao nao disponivel. ";
				system("pause");
				continue;
			}
		} else if (opc == 5) {
			if (VISIVEL == 0) {
				cout << "\n*** Opcao nao disponivel. ";
				system("pause");
				continue;
			}
			pilhall->imprime();
		}

		system("pause");


	}

	cout << "\n\n--- Fim de execicao. Ate' a proxima vez. ---\n\n";

	return 0;
}
