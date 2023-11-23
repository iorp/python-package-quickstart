 

# Developer notes

## AfterEdit
1. Navigate to the root of your project in the terminal and run:

   ```bash
   python setup.py sdist
   ```

2. Install the updated package locally using pip:

   ```bash
   pip install . --force-reinstall
   ```



# Replication

1. Update the package directory structure:

   ```plaintext
   mypackage/
   ├── mypackage/
   │   ├── __init__.py
   │   └── hello.py
   └── setup.py
   ```

   Now, the `mypackage` directory contains an `__init__.py` file and a `hello.py` module.

2. Update `mypackage/hello.py`:

   ```python
   def hello(name="World"):
       return f"Hello, {name} from mypackage!"
   ```

3. Update `mypackage/__init__.py` to import the `hello` function:

   ```python
   from .hello import hello
   ```

4. Update `setup.py` to include the new module:

   ```python
   from setuptools import setup, find_packages

   setup(
       name="mypackage",
       version="0.1.0",
       packages=find_packages(),
       entry_points={
           'console_scripts': [
               'mypackage_hello = mypackage.hello:hello',
           ],
       },
   )
   ```

5. Navigate to the root of your project in the terminal and run:

   ```bash
   python setup.py sdist
   ```

6. Install the updated package locally using pip:

   ```bash
   pip install .
   ```

7. Test the installed package:

   ```python
   $ python
   >>> from mypackage import hello
   >>> hello()
   'Hello, World from mypackage!'
   >>> hello("John")
   'Hello, John from mypackage!'
   ```

   You can also test the console script:

   ```bash
   $ mypackage_hello
   Hello, World from mypackage!
   ```

Now, the "hello world" functionality is encapsulated in the `hello` module within the `mypackage` package.