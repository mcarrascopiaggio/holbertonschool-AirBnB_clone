# Python - AirBnB clone --> The console:
<img src="https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png" />

## Description of the project:

This is the first of seven parts of the AirBnB clone project, which will result in a clone
of the AirBnB website (front-end and back-end).
In this first part we are going to use Python programming language in orther to build
a command interpreter, this is very similar to a shell but limited to a specific use case.
In our case we want to manage the objects that we are going to create in this project.
The piece is mainly to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.
This abstraction will also allow us to change the type of storage easily without updating all of our codebase.
The console will be a tool to validate this storage engine.
Below is a diagram showing the complete project. In this instance we will cover only the console and the storage engine.

<img src="https://github.com/agusfl/holbertonschool-AirBnB_clone/blob/master/Diagram.png" />

## Learning objectives:

* How to create a Python package.
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Environment:

* Language: Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/)
* Interpreter: python3 (version 3.8.5)

## Installation steps:

Clone the repo:

```
git clone https://github.com/agusfl/holbertonschool-AirBnB_clone.git
```
Move to the repo:
```
cd holbertonschool-AirBnB_clone
```

## Execution:

Interactibe Mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-Interactive Mode:

```
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
```
```

## Description of each command:

| Command          |Desription                      |
|:----------------|:-------------------------------:|
| create         | Creates a new instance of a class, saves it (to the JSON file) and prints the id.
| all            | Prints all string representation of all instances based or not on the class name.
| show           | Prints the string representation of an instance based on the class name and id.
| destroy        | Deletes an instance based on the class name and id (save the change into the JSON file).
| update         | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file.

### Usage & Examples:
* create Usage:

```bash
create <class>
```

```bash
(hbnb) create User
38f22813-2753-4d42-b37c-57a17f1e4f88
(hbnb)
```
* all Usage:

```bash
all <class>
```

```bash
(hbnb) all City                                                                                                                                 
["[City] (07062be7-fd57-4791-88a6-6a78806398c9) {'id': '07062be7-fd57-4791-88a6-6a78806398c9', 
'created_at': datetime.datetime(2022, 7, 1, 16, 6
, 54, 356353), 'updated_at': datetime.datetime(2022, 7, 1, 16, 6, 54, 356365)}"]                                                                
(hbnb)
```
* show Usage:

```bash
show <class> id
```

```bash
(hbnb) show City 07062be7-fd57-4791-88a6-6a78806398c9
[City] (07062be7-fd57-4791-88a6-6a78806398c9) {'id': '07062be7-fd57-4791-88a6-6a78806398c9', 'created_at': datetime.datetime(2022, 7, 1, 16, 6, 54, 356353), 'updated_at': datetime.datetime(2022, 7, 1, 16, 6, 54, 356365)}
(hbnb) 
```
* destroy Usage:

```bash
destroy <class> id
```

```bash
(hbnb) show City 07062be7-fd57-4791-88a6-6a78806398c9                                                                                           
[City] (07062be7-fd57-4791-88a6-6a78806398c9) {'id': '07062be7-fd57-4791-88a6-6a78806398c9', 'created_at': datetime.datetime(2022, 7, 1, 16, 6, 
54, 356353), 'updated_at': datetime.datetime(2022, 7, 1, 16, 6, 54, 356365)}                                                                    
(hbnb) destroy City 07062be7-fd57-4791-88a6-6a78806398c9                                                                                        
(hbnb) show City 07062be7-fd57-4791-88a6-6a78806398c9                                                                                           
** no instance found **
```
* update Usage:

```bash
update <class name> <id> <attribute name> "<attribute value>
```

```bash
(hbnb) all Review                                                                                                                               
["[Review] (904fd94e-2872-4f7f-8160-446eb41b49e4) {'id': '904fd94e-2872-4f7f-8160-446eb41b49e4', 'created_at': datetime.datetime(2022, 7, 1, 16,
 7, 8, 819977), 'updated_at': datetime.datetime(2022, 7, 1, 16, 7, 8, 819989)}"]                                                                
(hbnb) update Review 904fd94e-2872-4f7f-8160-446eb41b49e4 id 2222                                                                               
(hbnb) all Review                                                                                                                               
["[Review] (2222) {'id': 2222, 'created_at': datetime.datetime(2022, 7, 1, 16, 7, 8, 819977), 'updated_at': datetime.datetime(2022, 7, 1, 16, 7,
 8, 819989)}"]                                                                                                                                  
```

## Test
* unittest module
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```

### run test in interactive mode

```bash
echo "python3 -m unittest discover tests" | bash
```

### run test in non-interactive mode

```bash
python3 -m unittest discover tests
```

## Authors :pen:

* [Agustin Flom](https://www.linkedin.com/in/agustin-f/)
* [Marcela Carrasco](https://github.com/mcarrascopiaggio)
