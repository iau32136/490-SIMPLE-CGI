# 490-SIMPLE-CGI
# IBRAM UPPAL

#git url:
https://github.com/iau32136/490-SIMPLE-CGI.git

#student name for <uid>:
iau32136

#full address:
http://www.csun.edu/~iau32136/

Usage:
You use the page by typing in a web adress in the form input and then the web adress is requested and displayed at the bottom of the page, using curl 

Log:
For this project I setup a simple redirect to the simple.cgi script.
This script was written in perl and outputs (very) simple html that includes my name in a welcome message and a form.

the form takes text input and sends it to simple.cgi again as GET parameter.
the id of the get parameter for the url is "passedurl"

so queries will take the form of ?passedurl=<web address>

ten this is parsed using URL::entities to get the excape characters processed

and then curl is used from a system call to execute a request to that specific
page.
