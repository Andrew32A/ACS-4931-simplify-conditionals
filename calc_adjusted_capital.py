# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace nested conditional with guard clauses.

ADJ_FACTOR = 0.7

def get_adjusted_capital(capital, rate, duration, income):
    if capital <= 0:
        return 0
    if rate <= 0 or duration <= 0:
        return 0
    return (income / duration) * ADJ_FACTOR

adjusted_capital = get_adjusted_capital(50000, 4, 10, 10000)
print(adjusted_capital)
