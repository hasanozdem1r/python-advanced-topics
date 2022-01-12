"""
This script is created to show fundamental of testing
@Hasan Özdemir 01/13/2022
"""

"""
Tips for Testing
1. Just one thing per test : A testing unit should focus on one tiny bit of functionality and
prove it correct.
2.Independence is imperative: Each test unit must be fully independent, able to run
alone, and also within the test suite, regardless of the order they are called.
3. Precision is better than parsimony: Use long and descriptive names for testing functions.
4. Speed counts : Try hard to make tests that are fast.
5. RTMF (Read the manual, friend!). Learn your tools and learn how to run a single test or
a test case. 
6.Test everything when you start—and again when you finish. 
7.Version control automation hooks are fantastic. It is a good idea to implement a hook
that runs all tests before pushing code to a shared repository.
8. Write a breaking test if you want to take a break :  If you are in the middle of a develop‐
ment session and have to interrupt your work, it is a good idea to write a broken unit
test about what you want to develop next.
9. In the face of ambiguity, debug using a test.
10. If the test is hard to explain, good luck finding collaborators
11. If the test is easy to explain, it is almost always a good idea.
"""
import unittest

def fun(x):
    return x+1

class FunTest(unittest.TestCase):

    def test_that_fun_adds_one(self):
        self.assertEqual(fun(3), 4)

    def test_that_fun_fails_when_not_adding_number(self):
        self.assertRaises(TypeError, fun, "multiply six by nine")



