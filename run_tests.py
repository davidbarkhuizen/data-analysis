import unittest

testRunner = unittest.runner.TextTestRunner()

loader = unittest.TestLoader()
tests = loader.discover('tests')
print(tests)

testRunner.run(tests)