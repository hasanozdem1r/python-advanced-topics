# how to enforce constraints from derived class to base class
# 1. using via __built_class__ (least common approach)
# 2. usinng metaclass
class BaseMeta(type):

    def __new__(cls, name, bases, body):
        if not 'bar' in body:
            raise TypeError('bad user class')
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):

    def foo(self):
        return self.bar()
