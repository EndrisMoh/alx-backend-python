#!/usr/bin/env python3
'''Given the parameters and the return values, add type annotations to the
   function uUsing  Duck typing - first element of a sequence
   Hint: look into TypeVar
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Retrieves the first element of a sequence if it exists.
    '''
    if lst:
        return lst[0]
    else:
        return None
