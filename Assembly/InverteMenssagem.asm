# Trabalho da faculdade

# inverte completamente a menssagem que for digitada


.data  
    palavra:  .space 30      
    inverte: .asciiz "                                                                              "
    novalinha: .asciiz "\n" 
    mens: .asciiz "Digite uma palavra: "

.text


    li $v0, 4     
    la $a0, mens 
    syscall  


    li $v0 ,8
    la $a0, palavra
    li $a1,30
    syscall
   

     la $t0, palavra 
     la $t3, inverte 
     lb $t5, ($t3) # para trocar
  
  inicio:  
     lb $t2, ($t0)   
    beqz $t2, end   
   
    li $t1, 'A'     
    bge $t2, $t1, teste2  
        
    
   teste2: 
  
    li $t1, 'Z'  
    ble $t2, $t1, maiusculo  
    
    j minusculo     
  continue:  
  
    add $t0,$t0, 1     
    add $t4,$t4,1   
    j inicio 
    
    
  minusculo:
 
   subi $t2, $t2, 32  
   sb $t2, ($t0)   
    j continue   
     
   maiusculo :  
  
  addi $t2, $t2, 32  
   sb $t2, ($t0)    
    j continue        
 
  end:
  
    
    li $t1, 1  
    ble $t1, $t4, troca   
    j fim
  
       troca:
      sub $t0,$t0, 1     
     lb $t2, ($t0)     
     move $t5, $t2
     sb $t5, ($t3)
     add $t3,$t3, 1
     lb $t5, ($t3)
   
    
      sub $t4,$t4, 1
      j end
      
          
       fim:         
    li $v0, 4    
    la $a0, inverte   
    syscall  
      
    li $v0, 4      
    la $a0, novalinha  
    syscall  
      
    
    li $v0, 10  
   syscall 
   
