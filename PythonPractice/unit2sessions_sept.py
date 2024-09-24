cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
for count, cereal in enumerate(cereals, start=1):
  print(count, cereal)

# dictionary methods
d = {'a': 1, 'b':2, 'c': 3}
d['d'] = 4          # Adds a new key 'd' with value 4
print(d)            # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d['a'] = 10
print(d)
print(d['a']) # direct access by key, or use the get() method next which is considered safer since it won't raise an error if none is found
print(d.get('z'))
print(d.get('c'))
print(d.get('z', 'Not Found'))