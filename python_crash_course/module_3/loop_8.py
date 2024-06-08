# greeting = "hello"
#
# index = 0
#
# while index < len(greeting):
#     print(greeting[index:index+1])
#     index += 1


input = "Four score and seven years ago"

for c in input:
  if c.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(c)


#print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])

