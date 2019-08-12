# Stubs for engineering_notation.engineering_notation (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Union
import decimal


class EngUnit:
    unit: Optional[str] = ...
    eng_num: 'EngNumber' = ...
    def __init__(self, value: Union[str, int, float],
                 precision: int = ..., significant: int = ...) -> None: ...

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __add__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngUnit': ...
    def __radd__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngUnit': ...
    def __sub__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngUnit': ...
    def __rsub__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngUnit': ...
    def __mul__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngUnit': ...
    def __rmul__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngUnit': ...
    def __truediv__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngUnit': ...
    def __rtruediv__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngUnit': ...
    def __lt__(
        self, other: Union['EngNumber', str, int, float]) -> bool: ...
    def __gt__(
        self, other: Union['EngNumber', str, int, float]) -> bool: ...
    def __le__(
        self, other: Union['EngNumber', str, int, float]) -> bool: ...
    def __ge__(
        self, other: Union['EngNumber', str, int, float]) -> bool: ...
    def __eq__(
        self, other: object) -> bool: ...


class EngNumber:
    precision: int = ...
    significant: int = ...
    number: decimal.Decimal = ...
    def __init__(self, value: Union[str, int, float],
                 precision: int = ..., significant: int = ...) -> None: ...

    def to_pn(self, sub_letter: Optional[str] = ...) -> str: ...
    def __repr__(self) -> str: ...
    def __str__(self, eng: bool = ..., context: Any = ...) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __add__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngNumber': ...
    def __radd__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngNumber': ...
    def __sub__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngNumber': ...
    def __rsub__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngNumber': ...
    def __mul__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngNumber': ...
    def __rmul__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngNumber': ...
    def __truediv__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngNumber': ...

    def __rtruediv__(
        self, other: Union['EngNumber', str, int, float]) -> 'EngNumber': ...

    def __lt__(self, other: Union['EngNumber', str, int, float]) -> bool: ...
    def __gt__(self, other: Union['EngNumber', str, int, float]) -> bool: ...
    def __le__(self, other: Union['EngNumber', str, int, float]) -> bool: ...
    def __ge__(self, other: Union['EngNumber', str, int, float]) -> bool: ...
    def __eq__(self, other: object) -> bool: ...