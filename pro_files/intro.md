---
layout: page
title: Python data types, built-in functions, and flow control
subtitle: Python tutorial - part I
---

# Python programming fundamentals



As the old proverb says:

> "Tell me, and I'll forget; show me, and I may remember; involve me, and I'll understand."

So, there is no better way to start this relatively short introduction to the Python programming language than with examples. Our motivation is straightforward: Many of NLP's contemporary methods are supported by Python solutions.

```python

# this is a simple comment in Python
# comments are not executed
# usually they clarify code or emphasize something important
# hashtag sign are preceding comment text

print("This is a message from python!")

```

If we run this in Python, simple output would be produced:

```
This is a message from python!
```

## Functions

Here, **print** can be noticed, which is an embedded Python function. As its name suggests, the print function directly outputs the argument message to the screen or other standard output device. We will discuss functions in more depth, but for now, they can be realized as specialized workers for a particular job (see Figure 1).


![function_1]

**Figure 1** Function transforms inputs into the desired output    




Indeed, the desired output is an ideal scenario, and many details need to be satisfied to get that outcome. In this particular case **function name** is `print`, and the argument is the message `"This is a message from python!"`.  Therefore, every function has a specific signature:

```
function_name(par_1, par_2, par_3)
```

The **function name** points toward the appropriate action produced by it, followed by brackets containing zero or more **parameters**. Concrete values of parameters passed to the function some authors call **arguments**. So, for the print function in this example, parameter is a string, and an argument is a concrete message `"This is a message from python!"`

<div class="alert alert-warning" role = "alert">
<i class="fa fa-cogs" style="font-size:24px; font-weight:bold"> Highlights </i>

&nbsp;

Built-in functions are documented in <a href="https://docs.python.org/3/library/">The Python Standard Library</a>, and that reference is an inevitable part of consulting in the everyday work of any programmer.
</div>


In functions, parameters can be any regular type. By regular type, we mean generic types, data structures, and adequately user-defined types. Let's look at basic data types; others will be explained throughout the semester.

## Basic data types in Python

 - Integers
 - Floating-point numbers
 - Complex numbers
 - Strings
 - Boolean  

 Why are basic data types essential? The answer is simple: the computer needs to know how to save a particular type in memory. The type also defines allowed operations or, more straightforwardly, data manipulation.

### Strings

 We will introduce the notion of a variable here. The variable is a reference to the memory location for storing data.

```python

msg = "This is also a message!"
print(msg)

Output:

This is also a message!

```

Printing with format method.

```python

name = "Sara"
city = "Zadar"

print("{} lives in {}.".format(name, city))

Output:

Sara lives in Zadar.

```

Printing using f-Strings.

```python

author = "Roger Penrose"
title = "The Emperor's New Mind"
year = 1989

print(f"{author} wrote scientific classic {title} in the {year}.")

```

This example we can notice that the variable year is not declared within quotes. That implies it is a number, precisely an integer number.

```python

print(type(year))

Output:
<class 'int'>

```

The `print` function represents it with an equivalent string of adequate digits. Python has a mechanism for similar, visible data transformation.

```python

var = input("Please enter some year:\n")
print(f"User enter type -> {type(var)}.")
var = int(var) # type casting
print(f"After casting type is -> {type(var)}.")
print("You have entered {}".format(var))

Output:

Please enter some year:
>? 1987
User enter type -> <class 'str'>.
After casting type is -> <class 'int'>.
You have entered 1987

```

The first line introduces Python's built-in function `input`. It asks the user for standard input (from the keyboard) and interprets it as a string. The special character `\n` can be noticed at the end of the input message. Special characters tell the interpreter what to do but do not produce any visible character or sequence on standard output. Special characters have special [meaning](https://www.w3schools.com/python/gloss_python_escape_characters.asp), and on many occasions, they are known under the name `escape characters`.

As mentioned, data types define allowed operations on them. The following example presents that for the string type.

```python

snt_1 = "First sentence..."
snt_2 = "Second one..."

print(snt_1 + " " + snt_2)
print(snt_1 * 3)

Output:

First sentence... Second one...

First sentence...First sentence...First sentence...

```  

Plus, the operator in strings defines the so-called **concatenation** operation.

### Integer and floating point data type

Integers and floating point data types can be explained in the same section due to their standard features. Let us see one example:

```python

num_1 = 100
num_2 = 3

print(num_1 + num_2)

Output:

103

```

Some slightly modified cases:

```python

num_1 = input("Enter one integer:\t")
num_2 = input("Enter another integer:\t")
print(num_1 + num_2)

Output:

Enter one integer:	>? 100
Enter another integer:	>? 3
1003

```

Some strange things happened here. Can you guess why? The answer is straightforward: input produces string types. So, we need to convert strings into equivalent representatives. That operation has a unique name in programming: typecasting.

```python

num_1 = input("Enter one integer:\t")
num_2 = input("Enter another integer:\t")
print(num_1 + num_2)

num_1 = int(num_1)
num_2 = int(num_2)
print("After typecasting -> ", num_1 + num_2)

Output:

Enter one integer:	>? 100
Enter another integer:	>? 3
1003
After typecasting ->  103

```

Examples of division, nth power, and multiplication can be illustrated with some examples:

```python

n1 = 10
n2 = 3
res = n1/n2
print("Division = ", res)

res = n1**n2
print("Nth power: ", res)

res = n1 * n2
print("Multiplication -> ", res)

# floor division
res = n1//n2
print("Floor division - sometimes called integer division -> ", res)

# modulo operator
res = n1 % n2
print("Division remainder -> ", res)

Output:

Division =  3.3333333333333335
Nth power:  1000
Multiplication ->  30
Floor division - sometimes called integer division ->  3
Division remainder ->  1

```

### Boolean data type

The boolean data type has only two values &rarr; True and False. This data type is mainly related to comparison operators `>, <, >=, <=, ==, !=`. Let us imagine that the user has entered two values &Rarr; val1 and val2. We want to test their relationship.

```python

val1 = 1000
val2 = 45

# greater than
print(val1 > val2)
# less than
print(val1 < val2)
# equal to
print(val1 == val2)
# not equal to
print(val1 != val2)
# greater than or equal to
print(val1 >= val2)
# less than or equal to
print(val1 <= val2)

Output:

True
False
False
True
True
False

```
The Boolean data type is often connected to so-called if statements or any conditional statements. Conditional statements are part of the program control flow.

## Program control flow
Some programmers are working for a company that produces different robots. One robot type needs to have movement ability in the real world - the programmer's team needs to solve the problem of crossing the street in pedestrian crossing spots. Rules for that problem are:

```
If semaphore is in red then STOP
If semaphore is in green then GO
```

It can be assumed that the semaphore is fully operational and defined by two states for pedestrian movement regulation. Now, the logic is:

```
if a semaphore is in red, then STOP
else GO
```

The conclusion is very simple: The program needs to have a mechanism that mimics this real-world logic. Generally, programming mechanisms that define or demand different ways of program execution are program control flow mechanisms.  

###If statements - conditionals

The simplest form is `if-then` with the following logic:

`IF condition is satisfied THEN execute one or more commands.`

Generic implementation in Python is:

```python
if <logical expression>:
  commands
```

This generic form can be presented with the flow diagram in Figure 2:


![if-then]

**Figure 2** Flow diagram for IF-THEN


IF-THEN is simple to understand &rarr; branching point consists of the logical condition test, and if that test is true, then a block of commands 2 will be executed. After that, the following commands block 3 is executed. Otherwise, when the test is false only block 3 is executed.  

***Example:*** What will be output for inputs x = 1, 14, 10 in the following code:


```python

x = int(input("Enter positive integer:\t"))
if(x >= 10):
  print("Number -> ", x, " is greater or equal to 10!")
  print("This part will be printed only when logical if condition is satisfied!")
print("This will be always executed...")

```   

More often, if-else statements are in use. A code block after the ELSE part will always be executed in that mechanism, as depicted in Figure 3.



![if-else]

**Figure 3** Flow diagram for IF-ELSE


***Example:*** Create a Python program that checks if the user input string starts with a letter `p`. If the condition is a true print message, "Starts with p!", otherwise print "Starts with some other letter different of p!".

```python

letter = "p"
strin = input("Enter some arbitrary string:\t")
# strip whitespaces and transform it into the lower case
strin = strin.strip()
strin = strin.lower()
if strin.startswith(letter):
  print("Input string starts with -> ", letter, "!")
else:
  print ("Starts with some other letter!")

```

In situations where there is a need for more conditions to check if-else, if-else statements are useful (see Figure 4). As shown in Figure 4, when true is the outcome for any logical condition, the corresponding command block is in charge, and the program jumps to the first block after chained conditions. When all conditions are false, the else block is in action.  



![if-elseif]

**Figure 4** Flow diagram for chained IF-ELSEIF-ELSE


***Example:*** For an arbitrary user string check:

1. Equality with the string "This is if-else if-else" &Rarr; output message "Equals!!!" when it is true
2. When the string is not equal, check if it is starting with a low letter &Rarr; output message "Starts with a lower letter!" when it is true
3. When none of the above conditions are satisfied, print the message "Conditions not satisfied!" and output the input string below that message.

```python

target = "This is if-else if-else"
strin = input("Define one string\n")
if strin == target:
  print("Strings are equals!!!")
elif strin[0].islower():
  print("Starts with a lower letter!")
else:
  print("Conditions are not satisfied!")
  print("Input -> ", string)

```

<div class="alert alert-success" role = "alert">
<i class="fa fa-university" style="font-size:24px; font-weight:bold"> Recall </i>

&nbsp;

In the class, we discussed strings as an array of characters. That means they have length, and all letters are indexed starting from index 0 for the first letter.

</div>

Loops are another set of mechanisms for program control flow. In the next section, the basics of loops and while loops are discussed through diagrams and simple examples.

### Loops in Python

There are plenty of occasions when a program needs to repeat the same steps, and loops are a tool to achieve that goal. Principally, `for loops` is the leading choice when the number of repeats is known.

***Example:*** Write all numbers from 1 to 10. Instead of using print function 10 times, for loop solve the problem more efficiently.

```python

for num in range(1, 11):
    print("Num -> ", num)

Output:

Num ->  1
Num ->  2
Num ->  3
Num ->  4
Num ->  5
Num ->  6
Num ->  7
Num ->  8
Num ->  9
Num -> 10

```

<div class="alert alert-info" role = "alert">
<i class="fa fa-bell-o" style="font-size:24px; font-weight:bold"> Remark </i>

&nbsp;

All Built-in types and functions are well documented in Python Standard Library where even experienced programmers search for information.

</div>



![range]

**Figure 5** Part of the documentation for built-in type ranges


***Example*** Print one by one character in arbitrary string entered by user.

```python

inpt = input("Enter a string:\n")
k = 1
for ch in inpt:
  print(k, ": character -> ", ch)
   k += 1 # increment, same as k = k +1
print("Input string length is -> ", len(inpt))
input("<enter> for exit...")

Output:

Enter a string:
User input this string!
1 : character ->  U
2 : character ->  s
3 : character ->  e
4 : character ->  r
5 : character ->   
6 : character ->  i
7 : character ->  n
8 : character ->  p
9 : character ->  u
10 : character ->  t
11 : character ->   
12 : character ->  t
13 : character ->  h
14 : character ->  i
15 : character ->  s
16 : character ->   
17 : character ->  s
18 : character ->  t
19 : character ->  r
20 : character ->  i
21 : character ->  n
22 : character ->  g
23 : character ->  !
Input string length is ->  23
<enter> for exit...

```
The for loop can be conceptualized with the flow diagram in Figure 6.



![forLoop]

**Figure 6** For loop conceptual flow diagram


***Example*** Write program that prints only odd numbers from desired range of numbers.

```python

endRange = 11

for num in range(endRange):
  if num % 2 == 0:
    pass
    print(num, "-> text after passed even number...")
  else:
    print(num, " -> odd number -> ", num)
  print("After if condition... printed in every step of the for loop!")
print("<<<<<<<<<<<<<<<<< All finished!!! >>>>>>>>>>>>>>>>>>>>>")


Output:

0 -> text after passed even number...
After if condition... printed in every step of the for loop!
1  -> odd number ->  1
After if condition... printed in every step of the for loop!
2 -> text after passed even number...
After if condition... printed in every step of the for loop!
3  -> odd number ->  3
After if condition... printed in every step of the for loop!
4 -> text after passed even number...
After if condition... printed in every step of the for loop!
5  -> odd number ->  5
After if condition... printed in every step of the for loop!
6 -> text after passed even number...
After if condition... printed in every step of the for loop!
7  -> odd number ->  7
After if condition... printed in every step of the for loop!
8 -> text after passed even number...
After if condition... printed in every step of the for loop!
9  -> odd number ->  9
After if condition... printed in every step of the for loop!
10 -> text after passed even number...
After if condition... printed in every step of the for loop!
<<<<<<<<<<<<<<<<< All finished!!! >>>>>>>>>>>>>>>>>>>>>

```

Here we have `pass` statement as null operation placeholder. This statement can be used when no code needs to be executed. If `pass` is replaced with another statement `continue`, totally different outcome is produced.

```python

Output:

1  -> odd number ->  1
After if condition... printed in every step of the for loop!
3  -> odd number ->  3
After if condition... printed in every step of the for loop!
5  -> odd number ->  5
After if condition... printed in every step of the for loop!
7  -> odd number ->  7

```

The message `After if condition... printed in every step of the for loop!` is actually not printed in every step. The reason is simple—the `continue` statement immediately moves to the next step in the for loop.

Other types of loop are also common in Python &rarr; the `while loop.` When a number of looping steps is not known in advance while the loop is the main character. The flow diagram for that loop is shown in Figure 7.



![whileLoop]

**Figure 7** Flow diagram for while loop




<div class="alert alert-danger" role = "alert">
<i class="fa fa-thermometer-full" style="font-size:24px; font-weight:bold"> Warning </i>

&nbsp;

With the while loop, you can easily end up with an infinite looping. Take precautions in looping conditions to ensure it will terminate at some point.

</div>

***Example*** Using the while loop solves a problem for loops where the user string is printed character by character.  

```python

cnt = 0
inpt = input("Enter a string:\n")
while cnt < len(inpt):
  print(cnt, ":", inpt[cnt])
  cnt += 1 # comment this line to get infinite loop
print("<<<<<<<<<<<<<<<< finished >>>>>>>>>>>>>>>>>>")

Output:

Enter a string:
User enter a string!
0 : U
1 : s
2 : e
3 : r
4 :  
5 : e
6 : n
7 : t
8 : e
9 : r
10 :  
11 : a
12 :  
13 : s
14 : t
15 : r
16 : i
17 : n
18 : g
19 : !
<<<<<<<<<<<<<<<< finished >>>>>>>>>>>>>>>>>>

```

***Example*** Write the Python program that asks the user to supply strings until a choice for exit is not entered. The programmer decided to define exit code with a "q" letter.

```python

exitCode = "q"

while True:
  inpt = input("Enter some string...\n")
  print("You have entered: '<-", inpt, "->'")
  print("String length: ", len(inpt))
  cont = input("'q' for exit / any other for continue? -> \t")
  if cont.strip().lower() == exitCode:
    break
  else:
    print("Decision is to continue!")
print("Out from while loop!")
input("<enter> for exit... \t")

```

The while loop condition is always true because the Boolean value True is engaged. The only way to stop looping, in this case, is by `break` statement &Rarr; terminates the nearest enclosing loop, skipping optional else clause if the loop has one.


<div class="alert alert-info" role = "alert">
<i class="fa fa-bell-o" style="font-size:24px; font-weight:bold"> Remark </i>

&nbsp;

Principally, every the for loop can be replaced with an appropriate while loop and vice versa.

</div>


----

[whileLoop]:https://www.dropbox.com/s/9xidg9ur2quber9/WhileLoop.jpg?raw=1
[forLoop]:https://www.dropbox.com/s/21or0n0itk5ache/ForLoop.jpg?raw=1
[range]:https://www.dropbox.com/s/gbe39oasl0o3abl/range_funk.JPG?raw=1
[if-elseif]:https://www.dropbox.com/s/zkgl5ocd7o33vfb/IF-ELSEIF-ELSE.jpg?raw=1
[if-else]:https://www.dropbox.com/s/xx86oqumkhad5rk/Else_IF.jpg?raw=1
[if-then]:https://www.dropbox.com/s/3n82nl4gv1k8gi1/IF_THEN.jpg?raw=1
[function_1]:https://www.dropbox.com/s/kagizsgu5ifijhg/ProgrammingPython_function_1.jpg?raw=1
