# Rochelle

import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    from validators.validator import Validator as Va
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "validator.py"))
    sys.exit()

try:
    from washers.washer import Washer as Wa
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "washer.py"))
    sys.exit()


class ValidateSales(object):
    def __init__(self):
        self.min_sales = 0
        self.min_length = 3
        self.max_length = 3

    def is_valid(self, sales):
        result = False
        try:
            values = Va.check_valid(sales, self.min_sales, self.min_length, self.max_length)
            sales = values[0]
            result = values[1]
            return sales, result
        except ValueError:
            print("Input Value Error!")
            return sales, result


if __name__ == "__main__":  # pragma: no cover
    import doctest
    doctest.testmod(verbose=True)
