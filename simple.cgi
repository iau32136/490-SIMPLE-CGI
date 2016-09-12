#!/usr/bin/perl

print "Content-type: text/html\n\n";

print "";

$requestURI =  $ENV{'QUERY_STRING'};


@uriparts = split(/&/, "$requestURI");
$lengthofquery = scalar @uriparts;

print $lengthofquery;
if ($lengthofquery > 0) {
	print $uriparts[0];
}

$html = "
<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>490 - Simple - CGI </title>

  </head>
  <body>
  	Hey cool guy this is my project! <br>
  	my name is Ibram Uppal <br>

  </body>
</html>
";

print "$html";