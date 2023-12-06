<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'];
    $name = $_POST['name'];
    $inquiry = $_POST['inquiry'];
    $comment = $_POST['comment'];

    // Validate and sanitize data as needed.

    // Write data to a CSV file (you can use a text file if you prefer).
    $file = 'comments.csv';
    $data = array($email, $name, $inquiry, $comment);
    $handle = fopen($file, 'a');
    fputcsv($handle, $data);
    fclose($handle);

    // Send the email with the file attached.
    $to = 'quayles5806@student.faytechcc.edu';
    $subject = 'New Comment Submission';
    $message = 'A new comment has been submitted.';
    $headers = 'From: webmaster@example.com' . "\r\n" .
               'Reply-To: webmaster@example.com' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();

    // Attach the CSV file to the email.
    $file_attachment = chunk_split(base64_encode(file_get_contents($file)));
    $boundary = md5(uniqid(time()));
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: multipart/mixed; boundary = $boundary\r\n";
    $message = "This is a multi-part message in MIME format.\r\n\r\n" .
               "--$boundary\r\n" .
               "Content-Type: text/plain; charset=ISO-8859-1\r\n" .
               "Content-Transfer-Encoding: 7bit\r\n\r\n" .
               $message . "\r\n\r\n" .
               "--$boundary\r\n" .
               "Content-Type: application/octet-stream;\r\n" .
               "name=\"$file\"\r\n" .
               "Content-Transfer-Encoding: base64\r\n" .
               "Content-Disposition: attachment\r\n\r\n" .
               $file_attachment . "\r\n" .
               "--$boundary--";

    mail($to, $subject, $message, $headers);
}
?>
