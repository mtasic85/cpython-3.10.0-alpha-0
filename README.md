# Python 3.10 alpha 0

*Python 3.10 alpha 0* with *PEP 622* implementation. This is good start, if you would like to test Python with *Structural Pattern Matching* using *match* and *case* keywords. Once Python 3.10 is officially published, this build will become obsolete and whould not be used in production. Anyway, do not use this version in production.

PEP 622: https://www.python.org/dev/peps/pep-0622

Source is fetched from https://github.com/brandtbucher/cpython

# Example

*example1.py*:
```
from dataclasses import dataclass

@dataclass
class A:
    x: int
    y: int

a = A(10, 20)

match a:
    case A(x, y):
        print(f'A({x}, {y})')
    case _:
        print('Something else')
```

In terminal run:
```
docker run -it -v $PWD:/code mtasic85/cpython-3.10.0-alpha-0:latest python example1.py
```

Output:
```
A(10, 20)
```
