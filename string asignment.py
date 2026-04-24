"""
#String Programming Questions 
#Basic 
#1. Write a program to count the number of vowels in a string.
st=input("enter text:")
count=0
for i in st:
    if i in "aeiouAEIOU":
        count=count+1
print( "count vowels",count)        
#2. Reverse a string without using built-in functions.
st=input("enter text:")
rev=""
for ch in st:
     rev=ch+rev
print("reversed string",rev)

#3. Check whether a string is a palindrome.
st=input("enter a string:")
rev=""
for ch in st:
    rev=ch+rev
if st==rev:
    print("palindrome")
else:
    print("not palindrome")
    

#4. Count uppercase and lowercase letters in a string.
st=input("enter text:")
upper=0
lower=0
for ch in st:
    if ch.islower():
        lower=lower+1
    elif ch.isupper():
        upper=upper+1
print("uppercase",upper)
print("lowercase",lower)
    
    
    
#5. Replace all spaces in a string with _.
st=input("enter string:")
result=""
for ch in st:
    if ch==" ":
        result=result+"_"
    else:
        result=result+ch
print("modify string:",result)

#Intermediate 
#6. Find the frequency of each character in a string.
st=input("enter string:")
freq={}
for ch in st:
    if ch in freq:
       freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print("frequency:",freq)        
    

#7. Remove duplicate characters from a string.
st=input("enter text:")
result=""
for ch in st:
    if ch not in result:
        result=result+ch
print("after removing duplicates:",result)        
    
#8. Find the first non-repeating character in a string.

9. Check if two strings are anagrams. 
10. Convert "hello world" → "Hello World" (title case without using .title()). 
Tricky 
11. Find the longest word in a sentence. 
12. Compress a string like "aaabbc" → "a3b2c1". 
13. Count words, characters, and digits in a string. 
14. Rotate a string left by n positions. 
15. Find all substrings of a given string. 
Set Programming Questions 
#Basic 
#1. Create a set and add elements dynamically.
s=set()
n=int(input("enter elements you want to add:"))
for i in range(n):
    val=int(input("entre element:"))
    s.add(val)
print("final set:",s) 


#2. Find the union and intersection of two sets.
set1={1,2,3,4}
set2={4,5,6,7,8}
union_set=set1|set2
print("union:",union_set)
#3. Remove duplicate elements from a list using a set.
li=[1,2,1,3,8,3,4,1,2,4,5,6,7,8,9,7,5]
remove_duplicate=set(li)
print(remove_duplicate)
#4. Check if an element exists in a set.
set1={1,2,3,4,5,6}
element=5
if element in set1:
    print("element exist in set1")
else:
    print("element not exist in set1")
#5. Find the difference between two sets.
set1={1,2,3,4,5}
set2={4,5,6,7,8}
differnce=set1-set2
print("difference:",differnce)
Intermediate 
#6. Find common elements in two lists using sets.
li1=[1,2,3,4]
li2=[2,3,5,6]
common=set(li1)&set(li2)
print("common element:",common)

#7. Check whether one set is a subset of another.
set1={1,2}
set2={1,2,3,4}
if set1.issubset(Set2):
    print("set1 is subset of set2:")
else:
    print("set1 is not subset of set2:")
#8. Find symmetric difference of two sets.
set1{1,2,3,4}
set2{4,5,6,8}
sym_diff=set1^set2
print("symmetric differnce:",sym_diff)
#9. Count unique elements in a list using a set.
li=[1,2,3,1,2,4,5,6,5,6,7,8,9]
unique_element=set(li)
print("unique element",unique_element)
print("count of unique elements:",len(unique_elements))

#10. Remove all common elements from two sets.
li1=[1,2,3,4,5,6]
li2=[2,3,6,7,8]
common=set(li1)&set(li2)
li1=[x for x in li1 if x not in common]
li2=[x for x in li2 if not in common]
print("list1 after removal common:",li1)
print("list2 after removal common:",li2)
Tricky 
11. Find missing numbers from 1 to n using sets. 
#12. Check if two lists have any common elements.
li1=[1,2,3,4,5,6]
li2=[3,4,5,6,7,8,9]
common=set(li1)&set(li2)
if common:
    print("common elements exist")
else:
    print("not common elements")
    
#13. Convert a set of strings into uppercase.
s={"hello","dolly","good","night"}
upper_set={x.upper()for x in s}
print("upperstring:",upper_Set)

#14. Identify unique vowels in a given string using a set.

s={"hello","dolly", "and","vivek"}
vowels={'a','e','i','o','u'}
result=set()
for word in s:
    for ch in word:
        if ch in vowels:
            result.add(ch)
print(result)
"""

#15. Find elements that appear only once in a list.

#Dictionary Programming Questions 
#Basic 
#1. Create a dictionary and print all keys and values.
d={"name":"dolly","Age":20,"course":"python"}
for key,value in d.items():
    print(key,":",value)
d={"name":"dolly","Age":20,"course":"python"}
print(d)


#2. Count frequency of each word in a sentence.
sentence="this is a test this is very easy"
words=sentence.split()
freq={}
for word in words:
    if word in freq:
        freq[word]=freq[word]+1
    else:
        freq[word]=1
print(freq)
  

#3. Merge two dictionaries.
d1={"a":1,"b":2,"c":3}
d2={"d":4,"d":5,"e":6}
d1.update(d2)
print(d1)

#4. Find the length of a dictionary.
d={"a":1,"b":2,"c":3}
print(len(d1))

#5. Check if a key exists in a dictionary.
d={"name":"dolly","Age":20}
key="age"
if key in d:
    print("key exists")
else:
    print("key not exists")

#Intermediate

#6. Sort a dictionary by values.
d={"a":12,"b":14,"c":89}
sorted_dict=dict(sorted(d.items(),key=lambda x:X[1]))

#7. Find the key with the maximum value.
d={"a":12,"b":14,"c":89}
max_key=max(d,key=d.get)
print("key with maximum value:",max_key)

#8. Remove a key from a dictionary.
d={"name":"doll","age":21,"course":"bcom"}
d.pop("age")
print(d)
#9. Convert two lists into a dictionary
keys=["a","b","c","d","e"]
values=[7,8,9,10,11]
d=dict(zip(keys,values))
print(d)

#10. Count character frequency using a dictionary.

Tricky 
11. Invert a dictionary (swap keys and values). 
12. Group elements by frequency using a dictionary. 
13. Find duplicate values in a dictionary. 
14. Create a nested dictionary for student records. 
15. Flatten a nested dictionary. 
Mixed (String + Set + Dictionary) 
1. Count unique words in a sentence. 
2. Find common characters between two strings. 
3. Find the most frequent character in a string.

4. Remove duplicate words from a sentence. 
5. Find words with the same letters (anagram groups).

"""""
