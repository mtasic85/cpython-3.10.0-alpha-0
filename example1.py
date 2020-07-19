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
