# password generator
#### Video Demo:  <[https://youtu.be/j7HHUeYwAGc]() HERE>
#### Description:

## Password Generator: Project Overview

This Python script delivers a **customizable and secure password generator**, designed for ease of use. It interactively guides users to define their password's characteristics, specifically its **length** and the **inclusion of symbols**.

The generator ensures robust input validation:

* **Length:** Users specify a desired password length between 1 and 15 characters. The system actively prompts for valid numerical input within this range, guaranteeing adherence to practical security guidelines.
* **Symbols:** Users decide whether to incorporate special characters. This choice dynamically adjusts the character pool, which includes letters (uppercase and lowercase), digits, and optionally, punctuation.

Utilizing `random.choices()`, the script efficiently generates passwords by selecting characters from the defined pool, allowing for character repetition to enhance randomness. The generated password is then immediately displayed to the user. This streamlined process provides a fast, secure, and user-friendly experience for creating strong passwords. While the current maximum length is 15, this can be easily modified to suit evolving security needs.
