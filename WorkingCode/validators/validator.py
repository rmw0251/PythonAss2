import re
import sys

try:
    from errors import ErrorHandler as Err
except NameError and ModuleNotFoundError and ImportError:
    print("Fatal Error - Errors.py not found.")
    sys.exit()

try:
    from washers.washer import Washer as Wa
except NameError and ModuleNotFoundError and ImportError:
    print(Err.get_error_message(404, "washer.py"))
    sys.exit()


class Validator(object):
    # Graham
    @staticmethod
    def is_within_length(min_length, max_length, data):
        """
        >>> Validator.is_within_length(1, 3, '12')
        True
        >>> Validator.is_within_length(1, 3, '1234')
        False
        >>> Validator.is_within_length(1, 3, '')
        False
        >>> Validator.is_within_length(1, 3, '1')
        True
        >>> Validator.is_within_length(1, 3, '123')
        True
        >>> Validator.is_within_length(-5, 9999999, '1234')
        True
        >>> Validator.is_within_length(2, 2, '12')
        True
        >>> Validator.is_within_length(2, 2, '100')
        False
        """
        result = False

        if min_length <= len(data) <= max_length:
            result = True

        return result

    # Graham
    @staticmethod
    def is_correct_pattern(target_pattern, data):
        """
        >>> Validator.is_correct_pattern('\D\d\d\d', "A123")
        True
        >>> Validator.is_correct_pattern('\d\d\d\d', "0123")
        True
        >>> Validator.is_correct_pattern('\D\d\d\D', "A22Z")
        True
        >>> Validator.is_correct_pattern('\D\d\d\D', "1AB2")
        False
        """
        result = False

        if re.match(target_pattern, data):
            result = True

        return result

    # Graham
    @staticmethod
    def has_this_many_numbers(count, data):
        """
        >>> Validator.has_this_many_numbers(3, "A123")
        True
        >>> Validator.has_this_many_numbers(0, "ABC")
        True
        >>> Validator.has_this_many_numbers(0, "")
        True
        >>> Validator.has_this_many_numbers(9, "123456789")
        True
        >>> Validator.has_this_many_numbers(5, "23")
        False
        """
        number_count = sum(a_number.isdigit() for a_number in data)

        return number_count == count

    # Graham
    def has_this_many_letters(count, data):
        """
        >>> Validator.has_this_many_letters(1, "A123")
        True
        >>> Validator.has_this_many_letters(3, "ABC")
        True
        >>> Validator.has_this_many_letters(0, "")
        True
        >>> Validator.has_this_many_letters(9, "A2B2C2D2E2F2G2H2I")
        True
        >>> Validator.has_this_many_letters(0, "23")
        True
        """
        letter_count = sum(a_character.isalpha() for a_character in data)

        return letter_count == count

    # Claye
    @staticmethod
    def is_in_list(data, listed):
        """
        >>> Validator.is_in_list("Hi", ['Hi', 'Bye'])
        True
        >>> Validator.is_in_list("Hi", ['One', 'Two'])
        False
        """
        if any(data in s for s in listed):
            result = True
        else:
            result = False
        return result

    # Rochelle
    @staticmethod
    def is_minimum(data, minimum):
        """
        >>> Validator.is_minimum(10, 1)
        True
        >>> Validator.is_minimum(1, 1)
        True
        >>> Validator.is_minimum(0, 1)
        False
        """
        result = False
        if int(data) >= minimum:
            result = True
        return result

    # Rochelle
    @staticmethod
    def check_valid(num, min_num, min_length, max_length):
        if isinstance(num, int):
            num = Wa.to_string(num, min_length)
            if Validator.is_minimum(num, min_num):
                result = Validator.is_within_length(min_length,
                                                    max_length,
                                                    str(num))
        else:
            isinstance(int(Wa.keep_only_nums(num)), int)
            Wa.strip_string(num)
            num = Wa.keep_only_nums(num)
            num = Wa.to_string(num, min_length)
            result = Validator.is_within_length(min_length,
                                                max_length,
                                                str(num))
        return num, result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
