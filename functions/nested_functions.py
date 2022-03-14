"""
https://python-istihza.yazbel.com/ileri_fonksiyonlar.html#ic-ice-nested-fonksiyonlar
def fun1(): # enclosing function
    def fun2(): # nested function
        #things
    fun2_result=fun2()
"""


def print_hello():
    def hello():
        print("Hello")

    return hello()


print_hello()
