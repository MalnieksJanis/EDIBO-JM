<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
 <a class="exportCSV" href="downloadcsv.php">Export to CSV</a>


    <form  method="post" action="post">
    <input type="submit" name="xport" value="export CSV"> <br>

    <?php

  include_once ('conection.php');
  include_once ('csvdownload.php');
  include_once ('sort.php');

  include_once ('paging.php');


  if ($resultSet ->num_rows > 0){


  ?>  <table border="1"> <?php
    echo"

        <tr>
          <th> <a href ='?order=DayTime&&sort=$sort'> Date </th>
          <th> <a href ='?order=Email&&sort=$sort'> Email </th>
          <th> Delete  </th>
          <th> Checkbox </th>";

  while($rows = mysqli_fetch_array ($result)  ){
      echo "
      <tr>
  	 <td>".$rows['DayTime']."</td>
  	 <td>".$rows['Email']."</td>
     <td>  <a href=\"delete.php?id=".$rows['id']."\">delete</a></td>
    <td> <input type='checkbox' name='export[]' value='".$rows['id']."' </td>
  	 	 </tr> ";
          }
?>  </table> <?php
          }  else {
        echo "No records returnet."; }
      if ($total_no_of_pages <= 10){
        for ($counter = 1; $counter <= $total_no_of_pages; $counter++){
        if ($counter == $page_no) {
        echo " <a>$counter</a>";echo "<br>";
                }else{
              echo "<a href='?page_no=$counter'>$counter</a>";
            echo "<br>";
                      }  } }
 echo $page_no." of ".$total_no_of_pages;

?>

  </body>
</html>
