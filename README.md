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

- **[Emojize](week%204/emojize/emojize.py)** - _Replaces emoji aliases in user input with their corresponding emoji characters using the emoji library._

- **[Frank, Ian and Glen's Letters](week%204/figlet/figlet.py)** - Renders user input text in ASCII art using a specified font from command-line arguments or a random font if none is specified._

- **[Adieu, Adieu](week%204/adieu/adieu.py)** - _Greets a list of names provided by the user, formatting the output for one, two, or multiple names with "Adieu, adieu, to..."._

- **[Guessing Game](week%204/game/game.py)** - _Prompts the user for a positive integer level, then generates a random number within that range for the user to guess, providing "Too small!", "Too large!", or "Just right!" feedback._

- **[Little Professor](week%204/professor/professor.py)** - _Administers a 10-problem arithmetic quiz at a user-selected difficulty level, providing up to three attempts per question and displaying the correct answer after failures, then reports the final score._

- **[Bitcoin Price Index](week%204/bitcoin/bitcoin.py)** - _Fetches the current Bitcoin price in USD from an API, then calculates and prints the USD equivalent of a user-provided Bitcoin amount from a command-line argument._


---

### :arrow_forward: **Week 5 - Unit Tests**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Testing my twittr](week%205/test_twttr)** - _Defines a function shorten that removes all vowels from a string, includes a test_shorten function to verify its behavior with various inputs, and a main function to get user input and apply the shorten function._

- **[Back to the Bank](week%205/test_bank)** - _Tests the value function by asserting its output for various string inputs against expected monetary values._

- **[Re-requesting a Vanity Plate](week%205/test_plates)** - _Tests the is_valid function by asserting its return value for various valid and invalid license plate strings according to predefined rules._

- **[Refueling](week%205/test_fuel)** - _Tests convert and gauge functions from the fuel module, verifying convert correctly processes valid fractions and raises appropriate errors for invalid inputs, and gauge accurately formats fuel levels._


---

### :arrow_forward: **Week 6 - File I/O**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


- **[Lines of Code](week%206/lines/lines.py)** - _Takes a single command-line argument that must be a Python file, checks for its existence and .py extension, then prints the number of lines of code in that file, excluding blank lines and comments._
  
- **[Pizza Py](week%206/pizza/pizza.py)** - _Reads a specified CSV file, validates its extension and existence, then formats and prints its content as a grid-style table using the tabulate library._

- **[Scourgify](week%206/scourgify/scourgify.py)** - _Validates two command-line arguments as CSV file paths, then reads the first CSV, processes its 'name' and 'house' columns to split full names into 'first' and 'last', and writes the transformed data to the second CSV with new 'first', 'last', and 'house' headers._

- **[CS50 P-Shirt](week%206/shirt/shirt.py)** -  _Accepts two command-line arguments (input and output image file paths), validates their extensions and existence, then overlays a "shirt.png" image onto the input image after fitting, saving the result to the output file._

---

### :arrow_forward: **Week 7 - Regular Expressions**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[NUMB3RS](week%207/numb3rs)** - _One Python file validates if a string is a valid IPv4 address, checking format, digit content, range (0-255), and absence of leading zeros. A separate test file thoroughly verifies this validation logic with various correct and incorrect IPv4 address formats, including edge cases and expected error handling._

- **[Watch on YouTube](week%207/watch/watch.py)** - _This Python code extracts the YouTube video ID from an HTML iframe embed code using regular expressions and constructs a YouTube URL using the extracted ID._

- **[Working 9 to 5](week%207/working)** - _This set of files includes a Python script that converts time ranges from 12-hour (AM/PM) to 24-hour format, handling various input nuances and validating time components. Additionally, there is a separate test file using pytest that rigorously validates the convert function's behavior, checking for correct conversions, improper input formats, and out-of-range time values._

- **[Regular, um, Expressions](week%207/um)** - _This pair of Python files includes a main script that counts the occurrences of the whole word "um" (case-insensitive) in a user-provided text, and a separate test file using pytest to extensively validate the count function against various inputs, including cases where "um" appears as a whole word, part of other words, or with surrounding punctuation and spaces._

- **[Response Validation](week%207/response/response.py)** - _This script validates a user-provided email address, checking for a single "@" symbol and at least one dot in the domain, then prints "valid" or "invalid" based on these basic structural checks._

---

### :arrow_forward: **Week 8 - Object-Oriented Programming**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Seasons of Love](week%208/seasons)** - _This project consists of two Python files: a main script and a test file. The main script calculates the total minutes lived since a user-provided birth date and converts this number into English words. It robustly handles date input and utilizes the inflect library for number-to-word conversion. The accompanying test file uses pytest to validate the core logic of calculating minutes lived and converting numbers to words, ensuring accuracy and proper formatting for various numerical inputs._

- **[Cookie Jar](week%208/jar)** - _This Python code defines a Jar class that simulates a cookie jar with a fixed capacity, allowing users to deposit and withdraw cookies. It enforces constraints such as non-negative integer values for capacity, deposits, and withdrawals, and prevents exceeding capacity or withdrawing more cookies than available. A separate pytest file thoroughly tests all functionalities of the Jar class, including initialization with valid and invalid capacities, string representation, and the deposit and withdrawal methods, ensuring they handle valid operations and raise ValueError for invalid ones._

- **[CS50 Shirtificate](week%208/shirtificate/shirtificate.py)** - _This Python script uses the FPDF library to generate a PDF "shirtificate" document. It creates a custom PDF class that includes a header with a "CS50 SHIRTIFICATE" title and an embedded "shirtificate.png" image. The script then prompts the user for a name and generates a PDF displaying "[Name] took CS50" on the shirt, saving the output as shirtificate.pdf._
  
---

### :arrow_forward: **Week 9 - Et Cetera**

<br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- **[Final Project](week%209)** - _Password genarator_

---


<br>

## :books: **Credits**

First of all, a huge thank you to Prof. David J. Malan and the rest of the CS50 staff for giving us this free learning opportunity. I thoroughly recommend the CS50 course for anyone who wants to get into or improve their skills in the Computer Science field.

<br>

If you'd like to know more about CS50, I'll leave a few link down below.

- **[Official Website](https://cs50.harvard.edu/python/)**
- **[CS50 Introduction on YouTube](https://www.youtube.com/watch?v=OvKCESUCWII&t=2s)**
- **[CS50 on edX](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python)**
