import re


def generator_numbers(text: str):
    pattern = r"[-+]?(?:\d*\.*\d+)"
    salaries = re.findall(pattern, text)

    for salary in salaries:
        yield float(salary)


def sum_profit(text: str, func):
    total_income = 0.0

    for salary in func(text):
        total_income += salary

    return total_income
