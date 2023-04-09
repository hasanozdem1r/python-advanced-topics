# metaclasses and problem of writing safe library code

# how do you make sure user of this code doesn't screw up ?
# you can't control what your users write so how to make sure your user doesn't fail your code
# python is protocol oriented language
# from dis import dis # disassamble
# how to enforce constraints from derived class to base class
class Base:
    def foo(self):
        return self.bar()

old_bc=__build_class__

def my_bc(fun,name,base=None,**kw):
    if base is Base:
        print('check if bar method defined')
    if base is not None:
        return old_bc(fun,name,base,**kw)
    return old_bc(fun,name,**kw)

import builtins
builtins.__build_class__=my_bc

# run for test
# python -i user.py 

