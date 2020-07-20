from copy import deepcopy
from functools import wraps
from dataclasses import dataclass
from typing import TypeVar, Union, Callable
#
# Result / Ok / Err
#
T = TypeVar('T')


class ResultType(type):
    def __getitem__(cls, item: type) -> 'Result[T]':
        cls = deepcopy(cls)
        cls.T = item
        return cls


@dataclass
class Result(metaclass=ResultType):
    T: type = None


class Ok(Result):
    __match_args__ = ['v']
    v: T


    def __init__(self, v: T):
        self.v = v


    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} v: {self.v}>'


class Err(Result):
    __match_args__ = ['e']
    e: Exception


    def __init__(self, e):
        self.e = e


    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} e: {self.e}>'


def wrap_result(f: Callable) -> Callable:
    @wraps(f)
    def wrapper(*args, **kwargs) -> Result[T]:
        r: Result[T]

        try:
            v = f(*args, **kwargs)
            r = Ok[T](v)
        except Exception as e:
            r = Err[T](e)

        return r

    return wrapper


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
