import unittest
from charts.calc_chart_data import CalcData


class TestsCalcData(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def tearDown(self):
        # be executed after each test case
        pass

    # Calc Chart Data Testing

    def test_file_contents_are_valid(self):
        test_name = "Calc Chart Data Test #1"
        data_to_test = "A001,gender M,age 52,sales 123,bmi Overweight,"\
                       "salary 50,birthday 23/10/1998,valid 1,"
        class_to_test = CalcData()
        expected_result = True
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_file_contents_are_not_valid(self):
        test_name = "Calc Chart Data Test #2"
        data_to_test = "a001,M,52,123,Overweight,50,23-10-1998 Z005,F,"\
                       "18,624,Normal,85,25-04-1158 C078,F,35"
        class_to_test = CalcData()
        expected_result = False
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_line_age(self):
        test_name = "Calc Chart Data Test #3"
        data_to_test = "age"
        class_to_test = CalcData()
        expected_result = [50]
        # Action
        class_to_test.calc_line(data_to_test, 50)
        result = class_to_test.age_list
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_line_salary(self):
        test_name = "Calc Chart Data Test #4"
        data_to_test = "salary"
        class_to_test = CalcData()
        expected_result = [500]
        # Action
        class_to_test.calc_line(data_to_test, 500)
        result = class_to_test.salary_list
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_line_false(self):
        test_name = "Calc Chart Data Test #5"
        data_to_test = "salad"
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calc_line(data_to_test, 500)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_gender_m(self):
        test_name = "Calc Chart Data Test #6"
        data_to_test = "M"
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_pie_gender(data_to_test)
        result = class_to_test.count_gender_m
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_gender_f(self):
        test_name = "Calc Chart Data Test #7"
        data_to_test = "F"
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_pie_gender(data_to_test)
        result = class_to_test.count_gender_f
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_gender_false(self):
        test_name = "Calc Chart Data Test #8"
        data_to_test = "T"
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calc_pie_gender(data_to_test)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_sales_group1(self):
        test_name = "Calc Chart Data Test #9"
        data_to_test = 150
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_pie_sales(data_to_test)
        result = class_to_test.count_sales_group1
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_sales_group2(self):
        test_name = "Calc Chart Data Test #10"
        data_to_test = 300
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_pie_sales(data_to_test)
        result = class_to_test.count_sales_group2
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_sales_group3(self):
        test_name = "Calc Chart Data Test #11"
        data_to_test = 650
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_pie_sales(data_to_test)
        result = class_to_test.count_sales_group3
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_sales_group4(self):
        test_name = "Calc Chart Data Test #12"
        data_to_test = 850
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_pie_sales(data_to_test)
        result = class_to_test.count_sales_group4
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_sales_false(self):
        test_name = "Calc Chart Data Test #13"
        data_to_test = 9999
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calc_pie_sales(data_to_test)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_bmi_ov(self):
        test_name = "Calc Chart Data Test #14"
        data_to_test = 'Overweight'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_bmi(data_to_test)
        result = class_to_test.count_bmi_ov
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_bmi_ob(self):
        test_name = "Calc Chart Data Test #15"
        data_to_test = 'Obesity'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_bmi(data_to_test)
        result = class_to_test.count_bmi_ob
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_bmi_un(self):
        test_name = "Calc Chart Data Test #16"
        data_to_test = 'Underweight'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_bmi(data_to_test)
        result = class_to_test.count_bmi_un
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_bmi_no(self):
        test_name = "Calc Chart Data Test #17"
        data_to_test = 'Normal'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_bmi(data_to_test)
        result = class_to_test.count_bmi_no
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_bmi_false(self):
        test_name = "Calc Chart Data Test #18"
        data_to_test = 'Overweight and Underweight'
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calc_bar_bmi(data_to_test)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_jan(self):
        test_name = "Calc Chart Data Test #19"
        data_to_test = '10/01/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_jan
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_feb(self):
        test_name = "Calc Chart Data Test #20"
        data_to_test = '10/02/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_feb
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_mar(self):
        test_name = "Calc Chart Data Test #21"
        data_to_test = '10/03/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_mar
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_apr(self):
        test_name = "Calc Chart Data Test #22"
        data_to_test = '10/04/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_apr
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_may(self):
        test_name = "Calc Chart Data Test #23"
        data_to_test = '10/05/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_may
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_jun(self):
        test_name = "Calc Chart Data Test #24"
        data_to_test = '10/06/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_jun
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_jul(self):
        test_name = "Calc Chart Data Test #25"
        data_to_test = '10/07/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_jul
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_aug(self):
        test_name = "Calc Chart Data Test #26"
        data_to_test = '10/08/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_aug
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_sep(self):
        test_name = "Calc Chart Data Test #27"
        data_to_test = '10/09/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_sep
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_oct(self):
        test_name = "Calc Chart Data Test #28"
        data_to_test = '10/10/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_oct
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_nov(self):
        test_name = "Calc Chart Data Test #29"
        data_to_test = '10/11/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_nov
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_dec(self):
        test_name = "Calc Chart Data Test #30"
        data_to_test = '10/12/97'
        class_to_test = CalcData()
        expected_result = 1
        # Action
        class_to_test.calc_bar_birthday(data_to_test)
        result = class_to_test.count_birth_dec
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_bar_birth_false(self):
        test_name = "Calc Chart Data Test #31"
        data_to_test = '10/13/97'
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calc_bar_birthday(data_to_test)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_pie_sales_value_error(self):
        test_name = "Calc Chart Data Test #32"
        data_to_test = 'testing'
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calc_pie_sales(data_to_test)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calc_is_valid_type_error(self):
        test_name = "Calc Chart Data Test #33"
        data_to_test = 1234
        class_to_test = CalcData()
        expected_result = False
        # Action
        result = class_to_test.is_valid(data_to_test)
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calculate_false(self):
        test_name = "Calc Chart Data Test #34"
        data_to_test = "test"
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calculate(data_to_test, "line")
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calculate_gender(self):
        test_name = "Calc Chart Data Test #35"
        data_to_test = ['', 'A001,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,',\
        'Q001,gender M,age 45,sales 999,bmi Underweight,salary 725,birthday 31/12/1971,valid 1,',\
         'A002,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,']
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calculate(data_to_test, 'gender')
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calculate_line(self):
        test_name = "Calc Chart Data Test #36"
        data_to_test = ['', 'A001,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,',\
        'Q001,gender M,age 45,sales 999,bmi Underweight,salary 725,birthday 31/12/1971,valid 1,',\
         'A002,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,']
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calculate(data_to_test, 'line')
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calculate_sales(self):
        test_name = "Calc Chart Data Test #37"
        data_to_test = ['', 'A001,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,',\
        'Q001,gender M,age 45,sales 999,bmi Underweight,salary 725,birthday 31/12/1971,valid 1,',\
         'A002,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,']
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calculate(data_to_test, 'sales')
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calculate_birthday(self):
        test_name = "Calc Chart Data Test #38"
        data_to_test = ['', 'A001,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,',\
        'Q001,gender M,age 45,sales 999,bmi Underweight,salary 725,birthday 31/12/1971,valid 1,',\
         'A002,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,']
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calculate(data_to_test, 'birthday')
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))

    def test_calculate_bmi(self):
        test_name = "Calc Chart Data Test #39"
        data_to_test = ['', 'A001,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,',\
        'Q001,gender M,age 45,sales 999,bmi Underweight,salary 725,birthday 31/12/1971,valid 1,',\
         'A002,gender F,age 21,sales 001,bmi Normal,salary 12,birthday 01/01/1996,valid 1,']
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.calculate(data_to_test, 'bmi')
        # Assert
        try:
            self.assertTrue(
                result == expected_result)
        except AssertionError:
            print("{} Failed - Should be {}, but was {}.".format(
                test_name,
                expected_result,
                result))
        else:
            print("{} Passed".format(test_name))


if __name__ == '__main__':
    unittest.main()
