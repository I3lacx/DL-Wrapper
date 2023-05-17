"""This file has the add function which adds two numbers"""
from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    This function adds two numbers

    Parameters
    ----------
    a : Union[int, float]
        first number to add
    b : Union[int, float]
        second number to add

    Returns
    -------
    result : Union[int, float]
        result of the addition

    Raises
    ------
    TypeError
        if a or b are not numbers
    """

    # check if a and b are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    # compute the sum
    result = a + b
    return result
