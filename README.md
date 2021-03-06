# Python Course

## Table of contents

- [01 - History, Why Python?, Installation, IDE's and a Hello World (Syntax)](/01-Essentials/01-Essentials.ipynb)
- [02 - Data types (primitive data types) variables](/02-Variables/02-Variables.ipynb)
- [03 - Strings](/03-Strings/03-Strings.ipynb)
- [04 - Aritmetic and Logic Operators](/04-Arithmetic-and-Logic-Operators/04-Arithmetic-and-Logic-Operators.ipynb)
- [05 - Lists and Dictionaries](/05-Lists-and-Dictionaries/05-Lists-and-Dictionaries.ipynb)
- [06 - If Else Statements](/06-If-Else-Statements)
- [07 - Loops (for, while and List comprehensions)](/07-Loops)
- [08 - Functions](/08-Functions)
- [09 - OOP - Object Oriented Programming](/09-OOP)
- [10 - IO - Operations with files](/10-IO)
- [11 - REGEX - Regular Expressions](/11-Regex)
- [12 - Error handling and Exceptions](/12-Error-handling-and-exceptions)

## Prerequisites

Python 3 (3.X, 3.7, 3.8, 3.9, 3.10)
Basics libraries installed with the command bellow:

```bash
 pip3 install --upgrade pip3
 pip3 install -r requirements.txt
```

## General instructions

Every module has a the following structure:

```bash
 00-Module-Name               -> This is the name of the module
    ├── __init__.py           -> This is usefull to declare a module in Python
    ├── 00-Module-Name.ipynb  -> Here is the Jupyter notebook with the contents and challenges of the module
    └── test_script.py        -> This is the test script file with the challenges tests
```

To run the code, you can use the command bellow:

```bash

    # run "jupyter notebook" command to navigate and choose the ipynb file in the browser
    jupyter notebook

    #open the notebook file directly
    jupyter notebook 00-module-name/00-module-name.ipynb

```

Note: If for some reason the page appears blank in your browser, just refresh the page untill the notebook is correctly displayed


To test your code and pass the challenge, run the cells that calls the test script inside the Jupyter notebook.
