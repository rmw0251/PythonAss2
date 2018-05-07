import unittest
import io
import sys
from unittest.mock import patch
from file_reader import FileReader


class TestsDatabase(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def tearDown(self):
        # be executed after each test case
        pass

    # Write to database function

    def test_write_to_database_without_display_data(self):
        # Arrange
        test_name = "Write to Database without displaying data Test #01"
        insert = "N"  # don't see data saved to database
        data_to_test = {'A001': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                                 'birthday': '01/01/1996', 'valid': '1'},
                        'Q001': {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                                 'birthday': '31/12/1971', 'valid': '1'},
                        'A002': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                                 'birthday': '01/01/1996', 'valid': '1'},
                        'A05': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                                'birthday': '01/01/1996', 'valid': '0'}}
        class_to_test = FileReader()
        expected_result = "3 persons added! Congratulations!"

        # Action
        cmd_output = io.StringIO()
        sys.stdout = cmd_output
        with patch('builtins.input', side_effect=insert):
            result = class_to_test.write_to_database(data_to_test)
            sys.stdout = sys.__stdout__

        # Assert
        try:
            self.assertTrue(expected_result in cmd_output.getvalue())
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_write_to_database_with_display_data(self):
        # Arrange
        test_name = "Write to Database with displaying data Test #02"
        insert = "Y"  # see data saved to database
        expected_result = "['A001', 'F,', '21,', '001,', 'Normal,', '12,', '01/01/1996,', '1']"
        data_to_test = {'A001': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                                 'birthday': '01/01/1996', 'valid': '1'},
                        'Q001': {'gender': 'M', 'age': '45', 'sales': '999', 'bmi': 'Underweight', 'salary': '725',
                                 'birthday': '31/12/1971', 'valid': '1'},
                        'A002': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                                 'birthday': '01/01/1996', 'valid': '1'},
                        'A05': {'gender': 'F', 'age': '21', 'sales': '001', 'bmi': 'Normal', 'salary': '12',
                                'birthday': '01/01/1996', 'valid': '0'}}
        class_to_test = FileReader()

        # Action
        cmd_output = io.StringIO()
        sys.stdout = cmd_output
        with patch('builtins.input', side_effect=insert):
            result = class_to_test.write_to_database(data_to_test)
        sys.stdout = sys.__stdout__

        # Assert
        try:
            self.assertTrue(expected_result in cmd_output.getvalue())
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

if __name__ == '__main__':
    unittest.main()
