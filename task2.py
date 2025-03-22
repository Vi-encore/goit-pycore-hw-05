from typing import Callable, Generator
import re


# We can use typing Iterator[float] instead of Generator[] for same purposes
# (we do not send or return any value)
def generator_numbers(text: str) -> Generator[float, None, None]:
    # Find all numeric values in text using regex
    numbers = re.findall(r"\b\d+(?:\.\d+)?\b", text)

    # Transform numeric values into floats and yield them for further use
    for num in numbers:
        yield float(num)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Calculate sum of all all numeric values and return it
    return sum(func(text))


# Example of use
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
