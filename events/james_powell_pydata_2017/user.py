# metaclasses and problem of writing safe library code
# from library1 import Base # __built_class__ approach
# from library2 import Base # metaclass approach
from library3 import Base # __built_class__ approach

"""
Assume that you don't have control over library code and you are the only user
How the following code fail ? If foo method doesn't exist
Write code to check whether it's exist or not so you won't have problem
"""
# enforce constraint
assert hasattr(Base,'foo'), 'You broke it, you fool'
class Derived(Base):
    def bar(self):
        return 'bar'