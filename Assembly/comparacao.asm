# Coloca os elementos em ordem

.data

	N1: .asciiz "Digite o 1o numero: "
	N2: .asciiz "Digite o 2o numero: "
	N3: .asciiz "Digite o 3o numero: "
	maior: .asciiz "O Maior numero : "
	meio: .asciiz "    O intermediario e : "
	menor: .asciiz "   O menor numero : "

.text


	li $v0,4
	la $a0,N1
	syscall 


	li $v0,5
	syscall

	
	move $t0, $v0

	li $v0,4
	la $a0,N2
	syscall 

		
	li $v0,5
	syscall
		
	move $t1, $v0
	
	li $v0,4
	la $a0,N3
	syscall 

	
	li $v0,5
	syscall

		
	move $t3, $v0
	
	slt $t2,$t0,$t1 
	beq $t2,$zero,t0_maior_t1
	
        slt $t2,$t0,$t3 
	beq $t2,$zero,t0_maior_t3
	move $t4, $t0

        slt $t2,$t1,$t3 
	beq $t2,$zero,t1_maior_t3

	move $t6, $t3
	move $t5, $t1
	move $t4, $t0
	
	
	j resposta
t0_maior_t1:
	slt $t2,$t0,$t3 
	beq $t2,$zero,t0_maior_t3_maior_t1
	
	slt $t2,$t1,$t3 
	beq $t2,$zero,t0_maior_t3_maior_t1_
	move $t6, $t0
	move $t5, $t3
	move $t4, $t1
	j resposta


t0_maior_t3:
	slt $t2,$t1,$t3 # t0 < t3, se SIM, $t2 = 1
	beq $t2,$zero,t0_maior_t3_maior_t1_
move $t6, $t0
move $t5, $t3
move $t4, $t1
j resposta

t1_maior_t3:
move $t6, $t0
move $t5, $t1
move $t4, $t3
j resposta

t0_maior_t3_maior_t1:
	
        slt $t2,$t1,$t3 
	beq $t2,$zero,t1_maior_t3
	move $t6, $t0
	move $t5, $t3
	move $t4, $t1
  j resposta


t0_maior_t3_maior_t1_:

move $t6, $t1
move $t5, $t0
move $t4, $t3
j resposta



resposta:


#IMPRIMIR A MSG Resposta NA TELA		
	li $v0,4
	la $a0,maior
	syscall 

#IMPRIMIR O RESULTADO NA TELA		
	li $v0, 1
	move $a0, $t6
	syscall 

#IMPRIMIR A MSG Resposta NA TELA		
	li $v0,4
	la $a0,meio
	syscall 

#IMPRIMIR O RESULTADO NA TELA		
	li $v0, 1
	move $a0, $t5
	syscall 
	
#IMPRIMIR A MSG Resposta NA TELA		
	li $v0,4
	la $a0,menor
	syscall 

#IMPRIMIR O RESULTADO NA TELA		
	li $v0, 1
	move $a0, $t4
	syscall 