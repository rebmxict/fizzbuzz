from typing import List

def fizzbuzz(start: int, end: int) -> List[str]:
    """
    Generate a list of strings based on the FizzBuzz game rules.

    Parameters:
    - start (int): The starting integer.
    - end (int): The ending integer.

    Returns:
    List[str]: A list of strings representing the FizzBuzz game output.
    """
    if not (1 <= start <= 100) or not (1 <= end <= 100):
        raise ValueError("Both numbers should be between 1 and 100 inclusive.")
    if start > end:
        raise ValueError("Start number is greater than end number.")

    result = []
    for num in range(start, end + 1):
        output = str(num)
        if num % 3 == 0:
            output += ' fizz'
        if num % 5 == 0:
            output += ' buzz'
        result.append(output)
    return result