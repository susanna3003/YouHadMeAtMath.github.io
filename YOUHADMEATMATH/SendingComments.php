<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $comment = $_POST["comment"];

    // Open a file to append comments
    $file = fopen("comments.txt", "a");

    // Save the comment to the file
    fwrite($file, "Name: " . $name . "\n");
    fwrite($file, "Email: " . $email . "\n");
    fwrite($file, "Comment: " . $comment . "\n\n");

    // Close the file
    fclose($file);
}
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Comment Submitted</title>
</head>
<body>
    <h1>Your comment has been submitted. Thank you!</h1>
</body>
</html>
