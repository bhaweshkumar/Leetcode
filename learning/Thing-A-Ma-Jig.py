# characters = ['t', 'a', 'c', 'o']
characters = ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c']

output = ''
length = len(characters)
i = 0
while i < length:
    output = output + characters[i]
    i = i + 1
length = length * -1
print(output)
print("length", length)
i = -2

while i >= length:
    output = output + characters[i]
    i = i - 1

print(output)



