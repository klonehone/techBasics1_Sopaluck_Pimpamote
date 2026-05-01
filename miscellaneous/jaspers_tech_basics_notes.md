# Class Notes

## 21/4/26 Notes

A **high-level programming language** is close to human speech (eg. Python).  
A **low-level programming language** is closer to computer speech (eg. a = 010001).

### Programming Terminology

1. Statement
   - A statement performs actions (eg. `print("hello") , if x == 1`).
2. Expression
   - Expression → Evaluation → Value (eg. `123 , 1+2+3+4 , n == 3`).
4. Variables
A variable name should begin with a letter, and it can only contain letters, numbers and underscores.
Lowercase and uppercase letters are different characters. `word` , `Word` and `WORD` are three different variables.
It is a common practice in Python to use only lowercase characters in variable names. For multiple words, use an underscore between the words (eg. `family_name`).
     - A piece of memory that stores a value that can be changed (eg. `x = 1`).

`x = 1` is not the same as `x == 1`. == represents a conditional check "if x is equal to one".

### Different Variables

- string `"text"`
- int `394`
- float `3.1415926`
- boolean `True or False` *Must be Uppercase, `false` would be wrong.
- list, tuple, range
- set, dict
- NoneType

A small block of code containing a conditional if-clause:
```
if semester == 2:
   print("Take Tech Basics I)
elif semester == 3:
   print("Take Tech Basics II)
else:
   print("No more Tech Basics!")
```
Keep in mind, the if, elif and else executes whatever is after the colon `:`.

### Python Operators
Operators are used to perform operations on variables and values.
Includes arithmetic operators, assignment operators, comparison operators, logical operators, identity operators etc.

<ins>Arithmetic Operators</ins>  
| Operator | Name | Example |
| --- | --- | --- |
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulus | x % y |
| ** | Exponential | x ** y |
| // | Floor Division | x // y |

<ins>Comparison Operators</ins>  
| Operator | Name | Example |
| --- | --- | --- |
| == | Equal to | a == b |
| != | Not equal to | a != b |
| > | Greater than | a > b |
| >= | Greater than or equal to | a >= b |
| < | Less than | a < b |
| <= | Less than or equal to | a <= b |

<ins>Logical Operators</ins>  
Combine multiple conditions with: `and` , `or` and `not` (eg. `if a > b and a < c`).

<ins>Identity Operators</ins>  
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location (eg. `a is b , a is not b`).  
<sup>*Note it is **not** the same as `a == b`.</sup>

<ins>Truth Table</ins>  
| a | b | a and b | a or b |
| --- | --- | --- | --- |
| False | False | False | False |
| True | False | False | True |
| False | True | False | True | 
| True | True | True | True |

### Code Fixes

Consider the code:  
`result = 14 * 4`  
`print("The result is" + result)`

This results in an error. Corrections follow:  
`print(f"The result is {result}")`  
`print("The result is", result)`

A snippet of working code, determining prices for different ages:  
`age = input("Enter your age:"))`  
`age = int(age)`  
`if age > 0 and age < 110:`  
`    if age > 18:`  
`        print("1 Adult Ticket")`  
`    else:`  
`        print("1 Discount Ticket")`  
`else:`  
`    print("Please enter a valid age!")`  

end of document.
