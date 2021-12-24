from datetime import datetime
# STRING FORMATTING


err = 50159747054
name = "John Doe"

# old style
print('Hello %s' % name)

# convert an int to a string hex number
print('%x' % err)

# use them together
print('Hey %s, there is a 0x%x error!' % (name, err))
# so complex
print('Hey %(name)s, there is a 0x%(err)x error!' % {"name": name, "err": err})

# New style String Formatting
print('Hello {}'.format(name))
# a bit different
print('Hey {name}, there is a 0x{err} error!'.format(name=name, err=err))

# Literal String Interpolation (Python 3.6 + )
print(f'Hello {name}')

born=1881
died=1938
print(f'Ataturk died when he was {died-born} and from {datetime.now().year-died} years have passed since his death')

# Template Strings
from string import Template
t_obj=Template('Hey, $name')
data=t_obj.substitute(name=name)
print(data)

temp_str='Hey $name, there is a $error error!'
data2=Template(temp_str).substitute(name=name,error=hex(err))
print(data2)