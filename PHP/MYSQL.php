<?php
//////////////////////// CONECTA NO BANCO DE DADOS

$con = mysqli_connect("localhost", "root", "", "quality");

// Check connection
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}


//// Select


      $result10  =  mysqli_query($con, "SELECT * FROM tabela  WHERE ANO = '$ANO' AND MES = 10 AND CRITICO != 'SIM'");
      
      while ($linha = mysqli_fetch_array($result10)) {
     
      
          $DURACAO  = $linha["DURACAO"];
      
       
      }


//// Update



  mysqli_query($con, "UPDATE manutencao SET COMENTARIO='$COMENTARIO' WHERE ID = '$ID' "); 
  
  
//// Delete
  
  
  mysqli_query($con, "DELETE FROM historico_funcionario_dcc WHERE ID = '$ID' ");




?>