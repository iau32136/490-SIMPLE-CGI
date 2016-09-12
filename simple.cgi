#!/usr/bin/perl

print "Content-type: text/html\n\n";

print "";

$requestURI =  $ENV{'REQUEST_URI'};

$foo = "
<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>490 - Simple - CGI </title>
  </head>
  <body>
  	Hey cool guy this is my project! <br>
  	my name is Ibram Uppal and my <br>
  	project is better than your project <br>
  </body>
</html>
";

print "$foo";