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
