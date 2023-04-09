# how to enforce constraints from derived class to base class
# 1. using via __built_class__ (least common approach)
# 2. using metaclass (complex syntax, clumsy to use)
# 3. using _init_subclass
# TODO: complete this (from 47.00 mins)
class Base():
    def foo(self):
        return self.bar()
    def __init_subclass__(cls,*a,**kw) -> None:
        print('__init__subclass',a,kw)
        return super().__init_subclass__(cls,*a,**kw)