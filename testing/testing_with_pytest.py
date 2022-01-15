"""
This script is created to show fundamental of pytest library
@Hasan Özdemir 01/13/2022
"""
# pip install pytest to install
import pytest
# check the version -> pytest --version
"""
pytest is a no-boilerplate alternative to Python’s standard unittest module, meaning it
doesn’t require the scaffolding of test classes, and maybe not even setup and teardown
methods
"""
# mathematical method
def increment(x):
    return x + 1

# mathematical method
def decrement(x:int):
    return x-1

# system method
def f_exit():
    raise SystemExit()

# TEST CASES

# group multiple tests in a class

class TestMathCases:
    def test_increment(self):
        assert increment(3) == 4

    def test_decrement(self):
        assert decrement(3) == 2

class TestSystem:
    def test_f_exit(self):
        with pytest.raises(SystemExit):
            f_exit()