<?php
include 'header.php';
?>

<h1>Search page</h1>
<div class="article-container">
    <?php
    if (isset($_POST['submit-search'])) {
        $search = mysqli_real_escape_string($conn, $_POST['search']);
        $sql = "SELECT * FROM article WHERE a_title LIKE '%$search%' OR a_text LIKE '%$search%' OR a_author LIKE '%$search%' OR a_yearmonth LIKE '%$search%' OR a_keyword LIKE '%$search%'";
        $result = mysqli_query($conn, $sql);
        $queryResult = mysqli_num_rows($result);

        echo "There are ".$queryResult." results!";

        if ($queryResult > 0) {
            while ($row = mysqli_fetch_assoc($result)) {
#                echo "<a href='".$row['a_url']."' target='_blank'><div class='article-box'>
#                    <h3>".$row['a_title']."</h3>
                echo "<div>
                    <h3><a href='".$row['a_url']."' target='_blank'>".$row['a_title']."</a></h3>
                    <p>".$row['a_text']."</p>
                    <p>".$row['a_yearmonth']."</p>
                    <p>".$row['a_author']."</p>
                </div></a>";
            }
        } else {
            echo "There are no results matching your search!";
        }
    }
    ?>
</div>
</body>
</html>

