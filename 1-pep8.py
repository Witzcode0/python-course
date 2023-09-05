"""
link : https://peps.python.org/pep-0008/

What is PEP8?
    PEP 8 is a document that provides various guidelines to write the readable in Python.


source(developer) > bytecode(compile) > machine-code(low-level)

How to compile python code?
    use the py_compile module in Python to compile a Python file from the command line. 
    >>> python -m py_compile your_script.py

    The dis module in Python is used to disassemble Python bytecode. It allows you to inspect the low-level operations performed by your Python code. Here's how you can use the dis module from the command line:

    Open your command prompt or terminal.

    Navigate to the directory containing your Python script that you want to disassemble.

    Run the python -m dis command followed by the name of your Python script:
    >>> python -m dis your_script.py

"""