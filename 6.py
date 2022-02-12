input = int(input())
words = [] 

for _ in range(input):
  str = input()
  words.append(str)

temp1 = set(words)
count = []

for _ in temp1:
  number = words.count(_)
  count.append(number) 
  
print(len(temp1))
print(count)