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

    <link rel='stylesheet' type='text/css' href='http://bouncybuzz.com/HelloWorld/styles.css'>
  </head>
  <body>

  	<div id='internal'>
  	Hey cool guy this is my project! <br>
  	my name is Ibram Uppal <br>
";
###############################################################
# my style sheets are not located on the same server as my simple.cgi
# i own the website bouncybuzz.com for one of my iOS apps.
# i created a folder on their that is currently hosting the CSS stylesheets


###############################################################


print "$htmlStart";
print "<br>";

print "
	<p> Give me site to retrieve in the format www.DOMAIN_NAME.TOP_LEVEL_DOMAIN </p>
	<br>
	  	 <form action='simple.cgi' method='GET'>
  		site to retrieve: <input type='text' name='passedurl'><br>
  		<input type='submit' value='OK cool show me plz'>
  	</form>
";

## Get the passed url Param
$passedurl = "0";
if ($lengthofquery > 0) {
	for ($i = 0; $i < $lengthofquery; $i = $i + 1) {
		$currString = $queryparts[$i];
		@currentQueryItem = split(/\=/, $queryparts[$i]);
		if ($currentQueryItem[0] eq "passedurl") {
			$passedurl = $currentQueryItem[1];
		}
	}
}

print "</div>";

if ($passedurl eq "0") {
	#nothing
} else {
	system "/usr/bin/curl $passedurl";
}


$htmlEnd = "
  </body>
</html>
";

print "$htmlEnd";





