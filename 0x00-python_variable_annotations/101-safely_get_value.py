#!/usr/bin/env python3
'''Given the parameters and the return values, add type annotations
   to the function uUsing  Duck typing - first element of a sequence
   Hint: look into TypeVar
'''
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    '''Retrieves a value from a dict using a given key.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
