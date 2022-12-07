# PYTHON 2022

[🐍 PYTHON DOCS 🐍](https://www.python.org/)

`Current Version: 3.11.0`

- Interpreter running `cpython` language on a virtual machine...🤔

```py
# Alias command: 
p3 == python3
```

## Resources

[🐍 Python Cheat Sheet Github 🐍](https://github.com/aneagoie/ztm-python-cheat-sheet)

[Math Functions](https://docs.python.org/3/library/math.html)

[String Methods](https://www.w3schools.com/python/python_ref_string.asp)

[List Methods](https://www.w3schools.com/python/python_ref_list.asp)

[Dictionary Methods](https://www.w3schools.com/python/python_ref_dictionary.asp)

[Set Methods](https://www.w3schools.com/python/python_ref_set.asp)

[List of Keywords](https://www.w3schools.com/python/python_ref_keywords.asp)

[Built in Functions](https://docs.python.org/3/library/functions.html)

[Errors! Built in Exemptions](https://docs.python.org/3/library/exceptions.html)

[UNITTEST PACKAGE](https://docs.python.org/3/library/unittest.html)

[🗄 Python Modules 🗄](https://docs.python.org/3/py-modindex.html)

[🗂 Python Package Index 🗂](https://pypi.org/)

[PythonAnywhere w/ FLASK: Hosting](https://help.pythonanywhere.com/pages/Flask/)

[🐛 Debugger 🐛](https://docs.python.org/3/library/pdb.html)

[🛣 Filepaths 🛣](https://docs.python.org/3/library/pathlib.html)

[REGEX](https://www.w3schools.com/python/python_regex.asp)

[Python Exercises Github](https://github.com/darkprinx/break-the-ice-with-python)

[Asyncio Docs ⏯](https://docs.python.org/3/library/asyncio.html?highlight=asyncio#module-asyncio)

[Selenium Testing](https://selenium-python.readthedocs.io/)

### Variable naming

- snake_case
- starts with lowercase or _ (private var)
- letters, numbers, underscores
- case sensitive
- constants all uppercase (convention)
- don't use a keyword! 🤦‍♀️

----------------

`print(string[::-1])  # reverse a string`

`list methods modify mostly in place so 1. modify, 2. reassign aka -> None`

`Keyword in is cool: print(3.14 in pi)`

```python
# unpacking a list:

a, b, c, *other, d = [1, 2, 3, 4, 5, 6]

print(a, c, b, d, other)
# 1 3 2 6 [4, 5]
``` 

`dict method .items() returns items in a tuple`

```py
# docstrings
def test(a):
  '''
  Info: this func prints param A
  '''
  print(test.__doc__)
  ```
 
  ```py
  # walrus operator :=
walrus = "walrussdaffsdf"

if ((n := len(walrus)) > 10):
    print(f"too long a walrus {n}")

  # too long a walrus 14
  ```

  `list(map(lambda item: item * 100, [4, 5, 6]))`

  ```py
  # Fizz Buzz in list comprehension
  ['fizz_buzz' if i % 3 == 0 and i % 5 == 0 else 'fizz' if i % 3 == 0 else 'buzz' if i % 5 == 0 else i for i in range(1, 100)]
  ```

  [Performance Decorator Example](https://replit.com/@ArtieFischer/decorators#main.py)

  [@auth decorator example](https://replit.com/@ArtieFischer/decorators-1#main.py)
