# Multiple Inheritance
"""
class Combined(Super1, Super2, Super3):
    def __init__(self, something, something else):
        Super1.__init__(self, ......)
        Super2.__init__(self, ......)
        Super3.__init__(self, ......)
calls to the super class __init__ are optional and case dependent
"""


# The Diamond Problem
# https://uwpce-pythoncert.github.io/SystemDevelopment/_images/Diamond_inheritance.png
class A(object):

    def do_your_stuff(self):
        print("doing A's stuff")


class B(A):

    def do_your_stuff(self):
        A.do_your_stuff(self)
        print("doing B's stuff")


class C(A):

    def do_your_stuff(self):
        A.do_your_stuff(self)
        print("doing C's stuff")


class D(B, C):

    def do_your_stuff(self):
        B.do_your_stuff(self)
        C.do_your_stuff(self)
        print("doing D's stuff")


if __name__ == "__main__":
    # a instance
    a_obj = A()
    a_obj.do_your_stuff()
    print("*" * 50)
    # b instance
    b_obj = B()
    b_obj.do_your_stuff()
    print("*" * 50)
    # c instance
    c_obj = C()
    c_obj.do_your_stuff()
    print("*" * 50)
    # d instance
    d_obj = D()
    d_obj.do_your_stuff()
