#!/usr/bin/perl

print "Content-type: text/html\n\n";

print "";

$request =  $ENV{'QUERY_STRING'};


@queryparts = split(/&/, "$request");
$lengthofquery = scalar @queryparts;

$htmlStart = "
<!DOCTYPE html>
<html>
  <head>
    <meta charset='UTF-8'>
    <title>490 - Simple - CGI </title>

  </head>
  <body>
  	Hey cool guy this is my project! <br>
  	my name is Ibram Uppal <br>

";

$htmlEnd = "
  </body>
</html>
";



###############################################################


print "$htmlStart";

$passedurl = "0";
if ($lengthofquery > 0) {
	print "<br>";
	for ($i = 0; $i < $lengthofquery; $i = $i + 1) {
		$currString = $queryparts[$i];
		@currentQueryItem = split(/\=/, $queryparts[$i]);

		if ($currentQueryItem[0] eq "passedurl") {

			$passedurl = $currentQueryItem[1];
		}
	}
}

if ($passedurl eq "0") {
	#nothing
} else {
	print "<iframe src='$passedurl'></iframe>";
}


print "$htmlEnd";





