---
layout: page
title: Hands-on Python part I
subtitle: Learning by doing in Python
---

# Hands-on Python - part I

Learning through work is our central policy so we can go directly to some examples.

## Example 1
---

Write a Python program that asks the user's age, and based on that information, it returns the year of the user's birth. Also, the program provides information on what year the user will have a specified age.

{: .box-note}
**Note:** Recall how to create a new Jupyter notebook in Visual Studio Code &rarr; we show that in the morning session.

> Jupyter notebooks in Visual Studio are essential due to their resemblance with Google Colab Notebooks.

`Solution:` First, open a new Jupiter Notebook in VSC and name it `solution_1_part1.ipynb`. 

Before writing any program, there is an urgency for a logical and conceptual understanding of a problem.


```python

# solution - 1

from datetime import datetime


years_old = input("How old are you - please provide input: \t")
now_is = datetime.now().year
born_in = now_is - int(years_old)
print("You were born in: ", born_in)
print("You are interested in a year in which you will have some ages - e.g., 93")
old_in_future = input("Please provide ages of interest: \t")
future_year = born_in + int(old_in_future)
print(f'You will be {old_in_future} in the {future_year} year!')

```
The console output:

```
How old are you - please provide input: 	34
You were born in:  1990
You are interested in a year in which you will have some ages - e.g., 93
Please provide ages of interest: 	121
You will be 121 in the 2111 year!

Process finished with exit code 0
```



<div class="alert alert-warning" role = "alert">
<i class="fa fa-cogs" style="font-size:24px; font-weight:bold"> Highlights </i>

&nbsp;

No one knows everything defined in the Python programming language. For that reason, excellent documentation exists that needs to be consulted daily (see Figure 1).  
</div>

&nbsp;



![datetime]

**Figure 2** Datetime module in the Python Standard Library documentation  



## Example 2
---
Alternate the previous problem to ensure continuous user input, which could be repeated until the user decides to exit the program by typing the breaking sequence 'x'.

`Solution:` We must provide the same program sequence until the escaping sequence is entered. In advance, the number of repeats is unknown &Rarr; while loop. Create a new  `solution_1_part1.ipynb`.  

Solution code:

```Python
# solution - 2
from datetime import datetime

while True:
    years_old = input("How old are you - please provide input: \t")
    now_is = datetime.now().year
    born_in = now_is - int(years_old)
    print("You were born in: ", born_in)
    print("You are interested in a year in which you will have some ages - e.g., 93")
    old_in_future = input("Please provide ages of interest: \t")
    future_year = born_in + int(old_in_future)
    print(f'You will be {old_in_future} in the {future_year} year!')
    cont = input("To exit type 'ex' - any other key for new calculations!!!\n")
    if cont.lower() == 'ex':
        break
    else:
        continue
```



Console output:

```
How old are you - please provide input: 	29
You were born in:  1991
You are interested in a year in which you will have some ages - e.g., 93
Please provide ages of interest: 	78
You will be 78 in the 2069 year!
To exit type 'ex' - any other key for new calculations!!!
g
How old are you - please provide input: 	42
You were born in:  1978
You are interested in a year in which you will have some ages - e.g., 93
Please provide ages of interest: 	89
You will be 89 in the 2067 year!
To exit type 'ex' - any other key for new calculations!!!
Ex

Process finished with exit code 0

```

## Example 3
---
Write a Python function that receives two arguments. If only one of them is a string, perform string concatenation, and in a case where both are numbers, perform all four basic arithmetic operations. In all cases, the corresponding output needs to be produced.

`Solution: ` Create a new Python file with the name `solutions_3.py`. Here we have a relatively new moment in the form of the Python function. Python function can be represented as a black box with some inputs and outputs. In many situations, someone else has written a function, while others use it where there is a need for it. Logic of solution can be in the following form:

```

function (a, b):
    verify type:
      concatenation a and b -> string one of them or both
      perform arithmetic operations -> both are numbers
      print all results

```  

Solution code:

```Python
def conc_or_arithmetic(a, b):
    if isinstance(a, str) or isinstance(b, str):
        res = str(a) + str(b)
        print("Concatenation: ", res)
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        res = a + b
        print(f'{a} + {b} = ', res)
        res = a - b
        print(f'{a} - {b} = ', res)
        res = a * b
        print(f'{a} * {b} = ', res)
        try:
            res = a/b
            print(f'{a} / {b} = ', res)
        except ZeroDivisionError as zde:
            print(zde)
    else:
        print("Not strings nor numerical values!!!")
    print("<<<<<<<<<<<<<<<<< Finished function call >>>>>>>>>>>>>>>>>>>>>\n")



if __name__ == '__main__':
    # function calls
    conc_or_arithmetic("tamo", 8)
    conc_or_arithmetic(3, 4)
    conc_or_arithmetic(5, 0)
    conc_or_arithmetic("-", complex(2, 3))
    conc_or_arithmetic(complex(0, 3), complex(2, 3))


```

Console output:

```
Concatenation:  tamo8
<<<<<<<<<<<<<<<<< Finished function call >>>>>>>>>>>>>>>>>>>>>

3 + 4 =  7
3 - 4 =  -1
3 * 4 =  12
3 / 4 =  0.75
<<<<<<<<<<<<<<<<< Finished function call >>>>>>>>>>>>>>>>>>>>>

5 + 0 =  5
5 - 0 =  5
5 * 0 =  0
division by zero
<<<<<<<<<<<<<<<<< Finished function call >>>>>>>>>>>>>>>>>>>>>

Concatenation:  -(2+3j)
<<<<<<<<<<<<<<<<< Finished function call >>>>>>>>>>>>>>>>>>>>>

Not strings nor numerical values!!!
<<<<<<<<<<<<<<<<< Finished function call >>>>>>>>>>>>>>>>>>>>>


Process finished with exit code 0

```

In programming languages that support function usage, that concept implies a structured part of programming code that is specialized in some task that depends on defined mechanisms of executions in wanted parts or under some circumstances or by the particular event's appearance. Functions bring some advantages in programming languages:

1. Minimizes errors due to code repetition
2. Maximizes code readability
3. Simplifies code maintaining
4. Provides better upgrade options  


<div class="alert alert-warning" role = "alert">
<i class="fa fa-cogs" style="font-size:24px; font-weight:bold"> Highlights </i>

&nbsp;

In Python, function definitions starts with keyword <b>def</b> followed by function name.  Function names tend to be related to the function task (specialization). Do not use the Croatian diacritics, and for the compound names, use underscores. Every function can have zero or more parameters.   
</div>

From our example can be inferred that the following steps are crucial for functions usage:

1. Proper function definition
2. Function call at appropriate places or under some conditions or after some event

Sometimes, instead of the `function call`, other terms are known as synonyms &rarr; `run function`, `invoke the function`, or `execute the function`.


## Example 4
---

Write a Python function that receives some string and returns query term if it is found in input string and number of its' occurrences. Simplify problem so the query can be only one word.

`Solution:` Create a new Python file with the name `solutions_4.py`. Consider some problem that mimics given requirements.

```
This example represents one input string .
There are a few lines of text
Text can be without punctuations
Searched term can or can not be present
in the input string
We are looking upon word string ...
```   
`string` &rarr; is query

Solution code:

```Python
def find_term(input_string, q_term):
    count = 0
    found = None
    for wrd in input_string.split():
        if wrd == q_term:
            count += 1
            found = wrd
        else:
            continue
    return (found, count)


if __name__ == '__main__':
    str = '''This example represents one input string
            There are a few lines of text
            Text can be without punctuations
            Searched term can or can not be present
            in the input string
            We are looking upon word string ...
    '''
    query = "string"
    (wrd, cnt) = find_term(str, query)
    print("Word in string is {}.".format(wrd))
    print(f"Word {query} occurrence in the input string is {cnt} times.")

```
Console output:

```
Word in string is string.
Word string occurrence in the input string is 3 times.

Process finished with exit code 0

```

<div class="alert alert-success" role = "alert">
<i class="fa fa-bell" style="font-size:24px; font-weight:bold"> Important </i>

&nbsp;

Now we have enough knowledge to consider so-called Regular expressions, which have an essential role in NLP. That will be the topic of our next Exercise.   
</div>



----

[datetime]: https://www.dropbox.com/s/ysbe2tye7p0y312/datetime.JPG?raw=1
[newPyFile]:https://www.dropbox.com/s/rspdd8anjwi1c2g/newPythonFile.jpg?raw=1
