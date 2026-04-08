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

