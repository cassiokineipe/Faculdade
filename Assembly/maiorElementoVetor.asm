#Localiza o maior valor do vetor


.data
c: .word 3, 0, 1, 2, -6, -2, 4, 10, 3, 7, 8, -9, -15, -20, 87, 0 ,5 ,67 ,12 ,6
fim: .asciiz "\n O maior valor : "
espaco: .asciiz " "

.text
la $s2, c                

addi $t3,$zero,20 
lw $t2, 0($s2) 
move $s5,$t2
loop:
lw $t2, 0($s2) 

addiu $s2,$s2,4 

 slt $s6,$s5,$t2
 bne $s6,$zero,troca
 
 
 j exit
 troca:
 move $s5,$t2

exit:
subi $t3,$t3,1 
bne $t3,$zero,loop


li $v0, 4 
la $a0, fim
syscall

li $v0, 1 
move $a0, $s5
syscall
