# Python for JavaScript Developers — Personal Cheat Sheet

> My reference. Will Updated as I learn. Not a tutorial - my actual notes.

## Printing output

# Python

print("Hello World)

// JS equivalent

console.log("Hello World")

## Comments

# Python

#comments

# JS equivalent

//single-line comment
/\* multi-line comments \*/

## Variables & Types

# Python

name = "Rahul" # no const/let — Python is dynamically typed
age: int = 28 # type hint — optional but use it
items = [1, 2, 3] # list = array
person = {"name": "R"} # dict = object

// JS equivalent
const name = "Rahul";
const age: number = 28;
const items = [1, 2, 3];
const person = { name: "R" };

---

## Functions

# Python

def greet(name: str, greeting: str = "Hello") -> str:
return f"{greeting}, {name}!"

// JavaScript
function greet(name: string, greeting: string = "Hello"): string {
return `${greeting}, ${name}!`;
}

# Python

list - []
// Js
Array -[]

# Python-unpacking lists

numbers = [1,2,3,4]
first,last,second,third = numbers

// JS - destructing
let numbersArr = [1,2,3,4,5]
let [first,second,third,fourth,fifth] = numbersArr

# Python - rest operator

It is denoted by *
first,*last = numbers

// JS
It is denoted by ...
let [first,...last] = numbersArr

# Python - spread operator

It is denoted by \*

// JS
it is denoted by ...
