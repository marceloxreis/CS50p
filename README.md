## :label: **About CS50P**

**[CS50P]([https://pll.harvard.edu/course/cs50-introduction-computer-science?delta=0](https://pll.harvard.edu/course/cs50s-introduction-programming-python))**  is an online introductory course focused exclusively on programming with Python. It teaches foundational Python concepts such as functions, variables, conditionals, and loops, alongside practical programming skills like handling exceptions, writing unit tests, using third-party libraries, regular expressions, and object-oriented programming.

---

<br>

## :computer: **About the Repository**

An important part of the course, it's submitting the problem sets, as well as the final project for feedback. This repository contains the solutions I've come up with for the problem sets.

Also down below are links and short descriptions for each of the projects. If you'd like to read more about the implementation requirements, there's a link in each folder that will lead to them.

---

<br>

## :closed_book: **Academic Honesty**

Keep in mind the course's [academic honesty](https://cs50.harvard.edu/x/2024/honesty/). You should try figuring out a solution yourself before looking at other implementations. Also, bear in mind that I am a beginner, I've taken the course to learn, so the solutions might not be the best implementations.

---

<br>

## :book: **Content**

---

### :arrow_forward: **Notes**

<br>

![PNG Badge](https://img.shields.io/badge/File-PNG-lightgrey?style=for-the-badge)

- **[Notes](notes)** - _contains notes I took from various sources, mostly from each week's notes section._

---
### :arrow_forward: **Week 0 - Functions, Variables**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Indoor Voice](week%200/indoor.py)** - _ Converts user input to lowercase and prints it. _
 
- **[Playback Speed](week%200/playback.py)** - _Replaces spaces in user input with "..." and prints the modified string._

- **[Making Faces](week%200/faces.py)** - Replaces text emoticons :) with 🙂 and :( with 🙁 in user input, then prints.

- **[Einstein](week%200/einstein.py)** - _Calculates the energy (E) from mass (m) using Einstein's mass-energy equivalence formula (E=mcˆ2), where c is the speed of light._
 
- **[Tip Calculator](week%200/tip.py)** - _Calculates a tip amount based on user-provided meal cost and percentage, then prints the formatted tip._

---

### :arrow_forward: **Week 1 - Conditionals**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Deep Thought](week%201/deep.py)** - _Checks if user input, after normalization, matches "42" or "fortytwo" and prints "yes" or "no"._

- **[Home Federal Savings Bank](week%201/bank.py)** - _Determines a monetary value ($0, $20, or $100) based on the initial characters of a normalized user-provided greeting._

- **[File Extensions](week%201/extensions.py)** - _Determines and prints the MIME type for a user-provided filename based on its extension, defaulting to application/octet-stream if unknown._

- **[Math Interpreter](week%201/interpreter.py)** - _Evaluates a basic arithmetic expression (addition, subtraction, multiplication, or division) provided by the user and prints the floating-point result, handling division by zero._

- **[Meal Time](week%201/meal.py)** - _dentifies and prints "breakfast time", "lunch time", or "dinner time" based on user-provided input, converting the time to a 24-hour float._

---

### :arrow_forward: **Week 2 - Loops**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Camel Case](week%202/camel.py)** - _Converts a user-provided string from camelCase to snake_case by inserting underscores before uppercase letters and converting them to lowercase._

- **[Coke Machine](week%202/coke/coke.py)** - _Simulates a vending machine transaction, prompting the user to insert specific coin denominations until a $50 amount is paid, then calculates and prints change owed._

- **[Just setting up my twttr](week%202/twttr/twttr.py)** - _Removes all vowels (case-insensitive) from user input and prints the resulting string.

- **[Vanity Plates](week%202/plates/plates.py)** - _Validates if a user-provided license plate adheres to specific rules: length (2-6 characters), starting with two letters, no numbers before letters, first number not '0', and only alphanumeric characters allowed._

- **[Nutrition Facts](week%202/nutrition/nutrition.py)** - _Retrieves and prints the calorie count for a user-specified fruit by looking it up in a predefined dictionary._


---

### :arrow_forward: **Week 3 - Exceptions**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Fuel Gauge](week%203/fuel/fuel.py)** - _Calculates a fuel tank's percentage full from a user-provided fraction, displaying "E" for 1% or less, "F" for 99% or more, or the percentage otherwise._

- **[Felipe's Taqueria](week%203/taqueria/taqueria.py)** - _Calculates and continuously displays the running total cost of items from a predefined menu as the user inputs them, stopping on EOF._

- **[Grocery List](week%203/grocery/grocery.py)** - _Reads lines of user input until EOF, then counts and prints each unique item, sorted alphabetically, along with its frequency._

- **[Outdated](week%203/outdated/outdated.py)** - _Parses user-provided dates in MM/DD/YYYY or Month DD, YYYY format, validates them, and prints the date in YYYY-MM-DD format._

---

### :arrow_forward: **Week 4 - Libraries**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Emojize](week%204/volume/volume.c)** - _modify the volume of an audio file._

- **[Frank, Ian and Glen's Letters](week%204/filter-less)** - _program that applies filters to BMPs._

- **[Adieu, Adieu](week%204/filter-more)** - _program that applies filters to BMPs._

- **[Guessing Game](week%204/recover)** - _program that recovers JPEGs from a forensic image._

- **[Little Professor](week%204/recover)** - _program that recovers JPEGs from a forensic image._

- **[Bitcoin Price Index](week%204/recover)** - _program that recovers JPEGs from a forensic image._


---

### :arrow_forward: **Week 5 - Unit Tests**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Testing my twittr](week%205/inheritance)** - _simulates the inheritance of blood types for each member of a family._

- **[Back to the Bank](week%205/speller)** - _program that spell-checks a file using a hash table._

- **[Re-requesting a Vanity Plate](week%205/speller)** - _program that spell-checks a file using a hash table._

- **[Refueling](week%205/speller)** - _program that spell-checks a file using a hash table._


---

### :arrow_forward: **Week 6 - File I/O**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


- **[Lines of Code](week%206/hello.py)** - _ print a hello + your name 

- **[Pizza Py](week%206/mario.py)** - _create an adjacent pyramid of blocks._

- **[Scourgify](week%206/cash.py)** - _minimize the number of coins given to a customer when making a change using greedy algorithms._

- **[Readability](week%206/readability.py)** - _computes the approximate grade level needed to comprehend some text._

- **[CS50 P-Shirt](week%206/dna)** -  _program that identifies a person based on their DNA._

---

### :arrow_forward: **Week 7 - Regular Expressions**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[NUMB3RS](week%207/songs)** - _SQL queries that answer questions about a database of songs._

- **[Watch on YouTube](week%207/movies/)** - _SQL queries that answer questions about a database of movies._

- **[ Working 9 to 5](week%207/fiftyville)** - _write SQL queries to solve a mystery._

- **[ Regular, um, Expressions](week%207/fiftyville)** - _write SQL queries to solve a mystery._

- **[Response Validation](week%207/fiftyville)** - _write SQL queries to solve a mystery._

---

### :arrow_forward: **Week 8 - Object-Oriented Programming**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Seasons of Love](week%208/trivia)** - _simple webpage that lets users answer trivia questions._

- **[Cookie Jar](week%208/homepage)** - _simple web application with multiple pages._

- **[ CS50 Shirtificate](week%208/homepage)** - _simple web application with multiple pages._
  
---

### :arrow_forward: **Week 9 - Et Cetera**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Final Project](week%209/birthdays)** - _web application that keeps track of birthdays._

---


<br>

## :books: **Credits**

First of all, a huge thank you to Prof. David J. Malan and the rest of the CS50 staff for giving us this free learning opportunity. I thoroughly recommend the CS50 course for anyone who wants to get into or improve their skills in the Computer Science field.

<br>

If you'd like to know more about CS50, I'll leave a few link down below.

- **[Official Website](https://cs50.harvard.edu/python/)**
- **[CS50 Introduction on YouTube](https://www.youtube.com/watch?v=OvKCESUCWII&t=2s)**
- **[CS50 on edX](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python)**
