# Python 3.10 alpha 0

*Python 3.10 alpha 0* with *PEP 622* implementation. This is good start, if you would like to test Python with *Structural Pattern Matching* using *match* and *case* keywords. Once Python 3.10 is officially published, this build will become obsolete and whould not be used in production. Anyway, do not use this version in production.

PEP 622: https://www.python.org/dev/peps/pep-0622


# Examples

## Class Pattern

*example1.py*:
```python
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
```bash
docker run -it -v $PWD:/code mtasic85/cpython-3.10.0-alpha-0:latest python example1.py
```

Output:
```
A(10, 20)
```


## Error Handling 

*example2.py*:
```python
...

#
# user code
#
@wrap_result
def f1(x: Union[int, float], y: Union[int, float]) -> float:
    return x / y

#
# ok
#
r0: Result[float] = f1(1, 2)

match r0:
    case Ok(v):
        print(f'r0 Ok v: {v}')
    case Err(e):
        print(f'r0 Err e: {e}')

#
# err
#
r1: Result[float] = f1(1, 0)

match r1:
    case Ok(v):
        print(f'r1 Ok v: {v}')
    case Err(e):
        print(f'r1 Err e: {e}')
```

In terminal run:
```bash
docker run -it -v $PWD:/code mtasic85/cpython-3.10.0-alpha-0:latest python example2.py
```

Output:
```
r0 Ok v: 0.5
r1 Err e: division by zero
```
