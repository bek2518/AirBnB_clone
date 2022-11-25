This project is the first step towards building a full web application: the AirBnB clone. This first project will be used to build the other following projects which use HTML/CSS templating, database storage, API, front-end integration..


The Command Interpreter will be exactly the same like Shell but limited to a specific use-case.
The Command Interpreter will be able to manage the objects of our project:
* Create a new object like new User or new Place
* Retrieve an object from a file, a database
* Do operation on objects (count, compute stats ...)
* Update attributes of an object
* Destroy an object

On interactive mode the shell should work like:

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

In non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

