#!/usr/bin/env python3
""" Safely Get Value """


from typing import Any, Mapping, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key, or the default
        value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default


safely_get_value.__annotations__['default'] = 'typing.Optional[~T]'
