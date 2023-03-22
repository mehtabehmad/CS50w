# Create an empty set
s = set()

# add elements to the set
s.add(1)
s.add(2)
s.add(4)
s.add(3)
s.add(4)

print(s)

s.remove(3)
print(s)

print(len(s))
# s.add(['a', 'b', 'c']) -> error
# set element cannot be a mutable entity
