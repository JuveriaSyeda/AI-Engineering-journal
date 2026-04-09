#import math
import random
print("Hello World")
print("*" * 10)

# Strings
#learning = 10
#learning = True
#learn = False
# learn = "Hello There"
#learn = "Hello ! I'm learning python"
#firstName = "Syeda"
#lastName = "Syed"
# learn = f"{firstName} {lastName} is trying to learn python"
#countLearn = len(learn)
#print(learn,countLearn)
# print(learn[12:32])
# print(learn.lower())
# print(learn.strip())
# print(learn.title())
# print(learn.find('try'))
# print(learn.replace('y','j'))
# print('try' in learn )
# print('pro' not in learn)

''' Numbers '''

# num = 10. #integer
# num = 10.1 #float
# num = 10 + 1j #realNumber + imaginaryNumber

# print(round(10.1))
# print(abs(-10.5))
# print(math.ceil(10.2))

# x = input("num:")
# y = int(x)+1
# print(y)

# fruit = "Apple"
# print(fruit[1:-1])

#conditional operators
# temperture = 25;
# if temperture > 40:
#     print("It's very hot 🤯🥵")
#     print("Summer Season")
# elif temperture >= 20:
#     print("Warm and feels lil good")
# else:
#     print("It's winter 🥶")
# print("It's Done Now 😀")

#Ternary Opertor
# age = 17
# message = "Eligible" if age >= 18 else "Not Eligible"
#message = age >= 18 "Eligible" : "Not Eligible"
# print(message)

#logical operators
#or
#and
#Not

# credit_score = True
# high_income = False
# age = 68;
# student = True

# if (credit_score or high_income) and age >= 18 and not student:
#     print("Eligible for funds")
# else:
#     print('Not Eligible for funds')
    
#logical operators are short-circuted


## chaining comparasion operators

# if age >=18 and age <60:
#     print("Eligible")

# if 18 <= age < 65:
#     print("Eligible")



# loops
# for loop
#for number in range(1,4):
 #   print('Hello',number,"." * (number))
    
#for number in range(1,10,2):
 #   print("Hello There !!",number, number * ".")
    
# for-if loop

#successful = True;
#for number in range(3):
 #   print("Attempted")
  #  if successful :
   #     print('successful')
    #    break
#else:
 #   print(f"Attempted {number+1} times, Try Again {(number+1) * '!'}")
    
# nested loops
#for i in range(4):
 #   for j in range(3):
  #   print(f"({i},{j})")
    
#print(type(5))
#print(type(range(5)))

#While loop
#number = 100
#while number > 0:
#    print(number)
#    number //=2
    
#command = ""
#while command.lower() != "quit":
#    command = input(">")
#    print("Try something,",command)

#command = command.lower()
#while True:
 #command = input(">")
 #print("ECHO",command)
 #if command.lower() == "quit":
 #    break

#count = 0
#for x in range(2,10,2):
#    print(x)
#    count += 1
   
#print(f"We have {count} even numbers")
#count = 0
#for x in range(1,10):
#    if x%2 == 0:
#        print(x)
#        count +=1
#print(f"We have {count} even Numbers")

# Functions
#def greet(name):
#    print(f"Hello {name}!!")
#    print("Welcome to python Programming")


#greet("Syeda")

# Perform a task
# Return a value

#def greet(name):
#    return f"Hello {name}"
    
#message = greet("Syeda") 
#print(message)

#def increment(number,by):
#    return number + by
    
#print(increment(2,by=4))

#def multiply(*num):
#    print(num)
#    total = 1
#    for i in num:
#        total *= i
#    return(total)
    
#print(multiply(2,3,4,5,6))

#reverse string in python
# simpleStr = "Python Programming"
# reversedStr = simpleStr[::-1]
# print(reversedStr)

#loops
# finalReversedStr = ""
# for value in simpleStr:
#   finalReversedStr = value+finalReversedStr

# print(finalReversedStr) 

#Scoping
# message = "Hello"

# def greet(name):
#     message = "Hi There"
#     return f"{name} message"

# print(greet('syeda'))
# print(message)

# def fizz_buzz(input):
#     result = "" 
#     #if input is divisible by 3 return fizz
#     if input%3 == 0 and input%5 == 0:
#         result = "FizzBuzz"
#     # elif input is divisible by 5 return buzz
#     elif input%5 == 0:
#         result = "Buzz"
#     # elif input is divisible by 3 and 5 return fizzbuzz
#     elif input%3 ==0:
#         result = "Fizz"
#     # else return input value
#     else:
#         result = int(input)
#     return result

# print(fizz_buzz(37))

#Data Structures (list,tuples,sets,dictionaries)
# letters = ["a","b","c","d"]
# matrix = [[0,1],[2,3]]
# zeros = [0] * 5
# combined = zeros+letters
# numbers = list(range(10))
# print(zeros,combined)
#convert string into list/array what we call in js
# chars = list("Hello World")
# Array.from("Hello World") # In js or we can use split('')
# print(numbers)
# print(chars)
# letters[2] = "j"
# print(letters)
# print(letters[:3],letters[:],letters[0:])
# numbers = list(range(10))
# #reverse the list
# print(numbers[::-1])
# #items at even indexes
# print(numbers[::2])

#unpacking list what we call destructing in js
# numbersList = [1,2,3,4]
# first,second,third,fourth = numbersList
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# four = numbers[3]
# print(second)
# destructing in js
# let numberArr = [1,2,3,4]
# let [first,second,third,four] = numberArr

#rest in python
# first,second,*rest = numbersList
# print(first,rest)
#rest operator in js
# let [first,second,...rest] = numberArr

# first,*other,last = numbers
# print(first,other,last)

#looping over list

# for letter in enumerate(letters):
#     print(letter[0],letter[1])

# for index,letter in enumerate(letters):
#     print(index,letter)
# we can use for loop to iterate over list and if we need index we can use enumerate function, this return enumerate object which is iterable, in each iteration it will return tuple and we can unpack tuple with the help of index

#add/remove items in list
# adds d at last
# letters.append("d")
#adds - at 1 position
# letters.insert(1,"-")
#removes last item from list
# letters.pop()
#removes 2 item from list
# letters.pop(2)
#removes first occurance of b
#if we want to remove all occurances of b we have to loop over list
# letters.remove("b")
#removes items/slice from list
# del letters[0:2]
#remove all items in list
# letters.clear()
# print(letters)

#Finding index of items in list
# print(letters.count('d'))
# if 'e' in letters:
#     print(letters.index('e'))

#sorting list
# numbers = [3,51,2,8,6]
# numbers.sort(reverse=True)
# print(numbers)
# sortedList = sorted(numbers)
# print(sortedList,numbers)

# items = [
#     ("Product1", 85),
#     ("Product2", 24),
#     ("Product3", 44)
# ]

# def sortedPrice(item):
#      return item[1]

# sortedPrice(items[0])
# items.sort(key =sortedPrice)

#lambda function
# items.sort(key= lambda item:item[1] )
# print(items)

#Map Function
# prices = []
# for item in items:
#     prices.append(item[1])
# prices = list(map(lambda item:item[1],items))

# print(prices)

#Filter
# filtered = list(filter(lambda item:item[1] >= 60 ,items))
# print(filtered)

#comprehension List
# prices = [item[1] for item in items]
# print(prices)
# filteredList = [item for item in items if item[1] > 40]
# print(filteredList)

#Zip function
# list1 = (5,1,8)
# list2 = (26,18,56)
# zippedList = list(zip(list1,list2))
# zippedList = list('abc',zip(list1,list2))

# print(zippedList)
#
#stacks-LIFO-LastIn FirstOut
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# browsing_session.pop()
# print(browsing_session)
# if not browsing_session:
#     print('redirect', browsing_session[-1])

#Queues- FIFO - FirstIn FirstOut
# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# queue.popleft()
# print(queue)
# if not queue:
#     print('empty')
