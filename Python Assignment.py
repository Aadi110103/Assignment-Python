# Q-1 : check whether a given key already exists in a dictionary.
dic = {1: 10, 2: 20, 3: 30}
def is_key_present(x):
  if x in dic:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(3)


# Q-2 : Python script to merge two Python dictionaries.
  #1st way:
def Merge(dict1, dict2):
    return(dict2.update(dict1))
     
dict1 = {'a': 1, 'b': 2}
dict2 = {'d': 2, 'c': 4}
 
print(Merge(dict1, dict2))
 
print(dict2)

  #2nd way:
d1 = {'a': 1, 'b': 2}
d2 = {'x': 3, 'y': 4}
d = d1.copy()
d.update(d2)
print(d)


#Q-3 : sum all the items in a dictionary.
Marks = {
    "M1" : 10,
    "M2" : 20,
    "M3" : 50
}
sum = 0
for i in Marks.values() :
    sum = sum +i

print("Sum = ",sum)


# Q-4 : add a key to a dictionary.

Dic1 = {
    0:1,1:2
}
print("Dictionary : ")
print(Dic1)
print("Add a key to a dictionary :")
((Dic1.update({2 : 3}))) 
print(Dic1)


# Q-5 :  concatenate following dictionaries to create a new one.


dic1={
    1:10,
    2:20
}
dic2={
    3:30,
    4:40
}
dic3={
    5:50,
    6:60
}
print("Dictionary :")
print(dic1)
print(dic2)
print(dic3)
print(" Result :",dic1|dic2|dic3)


# Q-1 : add member in a set and clear a set

set = {4,5,6,'Aadi',(1,2,3)}
print(set)
set.add('single') 
print(set)
set.update(['123','learning'])
print(set)
a=set.clear()
print(a)



# Q-2 : remove an item from a set if it is present in the set.

set={'Aadi',6,4,'ABCXYZ',44}
print(set)
set.remove(10)
print(set)
set.remove('Aadi')
print("Updated set : ", set)


# Q-3 : create an intersection, Union, difference of sets.

a = {1,2,3,4,5,6}
b = {1,2,5,8,10,11}

print("a U b = ", a.union(b))
print("a ∩ b = ", a.intersection(b))
print("a - b = ", a.difference(b))



# Q-4 : find maximum and the minimum value in a set.

set = {1 , 2 , 3 , 4 , 5 , 9 , 100 , 99 , 8 , 44 }
print(set)
print("Maximum value :",max(set))
print("Minimum value :",min(set))



# Q-5 :  find the most common elements and their counts from list, tuple, dictionary.

#list
def most_frequent(List):
    return max(set(List), key = List.count)
List = [82, 33, 10, 82, 82, 10, 100, 10]
a=most_frequent(List)
print(a,List.count(a))

#tuple
def most_frequent(List):
    return max(set(List), key = List.count)
List = list((82, 19, 39, 29, 49, 22, 82, 82 ))  
a=most_frequent(List)
print(a,List.count(a))

#dictionary
def most_frequent(List):
    return max(set(List), key = List.count)
dict={1:11,2:22,3:33,4:11}
List = list(dict.values())
a=most_frequent(List)
print(a,List.count(a))



# Q-1 :  create a tuple with different data types.

tpl = ("Tuple",1,True,1.11)
print(type(tpl))
print(tpl)



# Q-2 : create a tuple with numbers and print one item.

tpl = (1,2,3,4,5,6,7,8)
print(tpl[0])
print(tpl[2])
print(tpl[4])
print(tpl[8])



# Q-3 : add an item in a tuple.

# tuple
a=(11,22,33,44,55,66,77,88)
print(a)
# List
b=list(a)
print(b)
# list add one item
b.append(100)
print(b)
# list to tuple...
c=tuple(b)
print(c)

#Q-4 : Convert a tuple to a string.

tpl = ('10', '5', 'A', 'a', 'D', 'I')
str = ''.join(tpl)
print(str)



#Q-5 :  find the length of a tuple.

tpl = ('10', '5', 'A', 'a', 'D', 'I')
print(tpl)
print(len(tpl))