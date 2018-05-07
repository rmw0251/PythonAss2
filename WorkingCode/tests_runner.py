import unittest
import tests_graham
import tests_rochelle_calc_data
import tests_rochelle_validators
import tests_rochelle_database
import tests_rochelle_calc_data_charts

loader = unittest.TestLoader()
all_my_tests = unittest.TestSuite()

all_my_tests.addTests(loader.loadTestsFromModule(tests_graham))  # not my tests
all_my_tests.addTests(loader.loadTestsFromModule(tests_rochelle_calc_data))  # switch case smell
all_my_tests.addTests(loader.loadTestsFromModule(tests_rochelle_validators))  # duplicated code smell
all_my_tests.addTests(loader.loadTestsFromModule(tests_rochelle_database))  # shotgun surgery smell
all_my_tests.addTests(loader.loadTestsFromModule(tests_rochelle_calc_data_charts))  # long method smell

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(all_my_tests)