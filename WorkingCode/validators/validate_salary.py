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


class ValidateSalary(object):
    def __init__(self):
        self.min_salary = 0
        self.min_length = 2
        self.max_length = 3

    def is_valid(self, salary):
        result = False
        try:
            if isinstance(salary, int):
                salary = Wa.to_string(salary, self.min_length)
                if Va.is_minimum(salary, self.min_salary):
                    result = Va.is_within_length(self.min_length,
                                                 self.max_length,
                                                 str(salary))
            else:
                isinstance(int(Wa.keep_only_nums(salary)), int)
                Wa.strip_string(salary)
                salary = Wa.keep_only_nums(salary)
                salary = Wa.to_string(salary, self.min_length)
                result = Va.is_within_length(self.min_length,
                                             self.max_length,
                                             str(salary))
            return salary, result
        except ValueError:
            result = False
            return salary, result


if __name__ == "__main__":  # pragma: no cover
    import doctest
    doctest.testmod(verbose=True)
