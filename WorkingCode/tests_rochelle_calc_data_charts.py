import unittest
from charts.calc_chart_data import CalcData


class TestsCalcDataCharts(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def tearDown(self):
        # be executed after each test case
        pass

    # Calc Chart Data  CHART FUNCTIONS Testing

    def test_line_chart_empty(self):
        test_name = "Calc Chart Data Line CHart Test #01"
        data_to_test = None
        class_to_test = CalcData()
        expected_result = None
        # Action
        result = class_to_test.line_chart()
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

    def test_line_chart_values(self):
        test_name = "Calc Chart Data Line Chart Test #02"
        data_to_test = None
        class_to_test = CalcData()
        expected_result = None
        class_to_test.calc_line('age', 50)
        class_to_test.calc_line('salary', 500)
        # Action
        result = class_to_test.line_chart()
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

    def test_bar_chart_birthday(self):
        test_name = "Calc Chart Data Bar Chart Birthday Test #03"
        data_to_test = None
        class_to_test = CalcData()
        expected_result = None
        class_to_test.calc_bar_birthday("12/12/12")
        class_to_test.calc_bar_birthday("12/10/12")
        # Action
        result = class_to_test.bar_chart("birthday")
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

    def test_bar_chart_bmi(self):
        test_name = "Calc Chart Data Bar Chart BMI Test #04"
        data_to_test = None
        class_to_test = CalcData()
        expected_result = None
        class_to_test.calc_bar_bmi("Overweight")
        class_to_test.calc_bar_bmi("Underweight")
        # Action
        result = class_to_test.bar_chart("bmi")
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

    def test_bar_chart_false(self):
        test_name = "Calc Chart Data Bar Chart FALSE Test #05"
        data_to_test = "testing"
        class_to_test = CalcData()
        expected_result = None
        class_to_test.calc_bar_bmi("Overweight")
        class_to_test.calc_bar_bmi("Underweight")
        # Action
        result = class_to_test.bar_chart(data_to_test)
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

    def test_pie_chart_gender(self):
        test_name = "Calc Chart Data Pie Chart Gender Test #06"
        data_to_test = None
        class_to_test = CalcData()
        expected_result = None
        class_to_test.calc_pie_gender("M")
        class_to_test.calc_pie_gender("F")
        # Action
        result = class_to_test.pie_chart("gender")
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

    def test_pie_chart_sales(self):
        test_name = "Calc Chart Data Pie Chart Sales Test #07"
        data_to_test = None
        class_to_test = CalcData()
        expected_result = None
        class_to_test.calc_pie_sales(150)
        class_to_test.calc_pie_sales(500)
        # Action
        result = class_to_test.pie_chart("sales")
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

    def test_pie_chart_false(self):
        test_name = "Calc Chart Data Pie Chart FALSE Test #08"
        data_to_test = "testing"
        class_to_test = CalcData()
        expected_result = None
        class_to_test.calc_pie_sales(150)
        class_to_test.calc_pie_sales(250)
        # Action
        result = class_to_test.pie_chart(data_to_test)
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
