smoothies = ['coconut', 'strawberries', 'banana', 'pineapple', 'acai berry']
print(len(smoothies))
print(smoothies[4])
print(smoothies)
smoothies[1] = 'not a smoothie anymore'
print(smoothies)

smoothies.append('mango')
smoothies.reverse()

print(smoothies)
smoothies[4] = 'strawberries again'
print(smoothies)
print(smoothies[3:])
print(smoothies[0:1])
print(smoothies[-1])
print(smoothies[-3:])
