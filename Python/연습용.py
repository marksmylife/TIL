python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))

index = python.index('n')
print(index)
index = python.index('n', index+1)
print(index)

print(python.find('i'))

print(python.count('n'))