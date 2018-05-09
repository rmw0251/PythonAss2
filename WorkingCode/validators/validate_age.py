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


class ValidateAge(object):
    def __init__(self):
        self.min_age = 1
        self.min_length = 2
        self.max_length = 2

    def is_valid(self, age):
        result = False
        try:
            values = Va.check_valid(age, self.min_age, self.min_length, self.max_length)
        except ValueError:
            print("Input Value Error!")
            # result = False
            return age, result


if __name__ == "__main__":  # pragma: no cover
    import doctest
    doctest.testmod(verbose=True)
