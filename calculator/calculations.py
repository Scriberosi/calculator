# calculator/calculations.py
"""
This module provides basic arithmetic operations.

Functions:
    add(a: int | float, b: int | float) -> float:
        Adds two numbers.
    subtract(a: int | float, b: int | float) -> float:
        Subtracts the second number from the first number.
    multiply(a: int | float, b: int | float) -> float:
        Multiplies two numbers.
    divide(a: int | float, b: int | float) -> float:
        Divides the first number by the second number.

Examples:
    >>> add(1, 2)
    3.0
    >>> subtract(5, 3)
    2.0
    >>> multiply(2, 3)
    6.0
    >>> divide(6, 3)
    2.0
"""


def add(a: int | float, b: int | float) -> float:
    """Adds two numbers.

    Args:
        a : The first number.
        b : The second number.

    Returns:
        The sum of the two numbers.

    Examples:
        >>> add(1, 2)
        3.0
        >>> add(1.5, 2.5)
        4.0
    """
    return float(a + b)


def subtract(a: int | float, b: int | float) -> float:
    """Subtracts the second number from the first number.

    Args:
        a : The first number.
        b : The second number.

    Returns:
        The difference of the two numbers.

    Examples:
        >>> subtract(5, 3)
        2.0
        >>> subtract(5.5, 2.5)
        3.0
    """
    return float(a - b)


def multiply(a: int | float, b: int | float) -> float:
    """Multiplies two numbers.

    Args:
        a : The first number.
        b : The second number.

    Returns:
        The product of the two numbers.

    Examples:
        >>> multiply(2, 3)
        6.0
        >>> multiply(2.5, 4)
        10.0
    """
    return float(a * b)


def divide(a: int | float, b: int | float) -> float:
    """Divides the first number by the second number.

    Args:
        a : The first number.
        b : The second number.

    Returns:
        The quotient of the two numbers.

    Raises:
        ValueError: If the second number is zero.

    Examples:
        >>> divide(6, 3)
        2.0
        >>> divide(7.5, 2.5)
        3.0
        >>> divide(1, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: Can't divide by zero

    Tests:
        >>> try:
        ...     divide(2, 0)
        ... except ZeroDivisionError:
        ...     pass
    """
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return float(a / b)
