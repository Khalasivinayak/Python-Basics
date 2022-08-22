#list comprehensions:-
#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Syntax:-newlist = [expression for item in iterable if condition == True]

#normal way for loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print("this is a older version",newlist)

#using list_C

new_list_v2=[x for x in fruits if "a" in x]

print("this is a newer version",new_list_v2)


#EX2

list_digits=[1,2,34,55.3,223.4,2,56,7,3,5,6,323]

evenumber=[x for x in list_digits if x%2==0]
oddnumber=[x for x in list_digits if x%2!=0]

print("even number is :", evenumber)
print("odd number is ", oddnumber)

# Use for the questions below:

nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

#Find all of the numbers from 1–1000 that are divisible by 8
list_digits_eight=[x for x in nums if x%8==0]
#print("the list of number divisible by 8", list_digits_eight)


#Find all of the numbers from 1–1000 that have a 6 in them

sixindigit=[x for x in nums if "6" in str(x)]
#print("the list digit contain 6",sixindigit)

#Count the number of spaces in a string (use string above)
count_space=len([x for x in string if x==" "])
print("count space is ",count_space) 

#Remove all of the vowels in a string (use string above)
onlyapha=[x for x in string if x!='a' if x!='e' if  x!='i'  if x!='o' if x!='u' in string]
print("only alphabasic",onlyapha)
#Find all of the words in a string that are less than 5 letters (use string above)