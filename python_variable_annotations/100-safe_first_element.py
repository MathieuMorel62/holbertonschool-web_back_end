#!/usr/bin/env python3
""" Function safe_first_element """

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None


safe_first_element.__annotations__['return'] = 'typing.Optional[typing.Any]'
