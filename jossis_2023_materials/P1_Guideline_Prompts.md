# Guidelines

## Principle 1: Write clear and specific instructions 

### Tactic 1: Use delimiters to clearly indicate distinct parts of the input

text='''
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.'''

Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```


### Tactic 2: Ask for a structured output

Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.


### Tactic 3: Ask the model to check whether conditions are satisfied

#### Prompt 1

text ="""
Making a cup of tea is easy! First, you need to get some \
water boiling. While that's happening, \
grab a cup and put a tea bag in it. Once the water is \
hot enough, just pour it over the tea bag. \
Let it sit for a bit so the tea can steep. After a \
few minutes, take out the tea bag. If you \
like, you can add some sugar or milk to taste. \
And that's it! You've got yourself a delicious \
cup of tea to enjoy.
"""
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"

"""{text_1}"""


#### Prompt 2

text="""
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \
walk in the park. The flowers are blooming, and the \
trees are swaying gently in the breeze. People \
are out and about, enjoying the lovely weather. \
Some are having picnics, while others are playing \
games or simply relaxing on the grass. It's a \
perfect day to spend time outdoors and appreciate the \
beauty of nature.
"""
You will be provided with text delimited by triple quotes.
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \
then simply write \"No steps provided.\"

"""{text_1}"""

### Tactic 4: Few shot prompting

Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.


## Principle 2: Give the model time to “think”

### Tactic 1: Specify the steps required to complete a task

text="""
In a charming village, siblings Jack and Jill set out on \
a quest to fetch water from a hilltop \
well. As they climbed, singing joyfully, misfortune \
struck—Jack tripped on a stone and tumbled \
down the hill, with Jill following suit. \
Though slightly battered, the pair returned home to \
comforting embraces. Despite the mishap, \
their adventurous spirits remained undimmed, and they \
continued exploring with delight.
"""
Perform the following actions:
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into German.
3 - List each name in the German summary.
4 - Output a json object that contains the following \
keys: german_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```

##### Ask for output in a specified format

Your task is to perform the following actions:
1 - Summarize the following text delimited by
  <> with 1 sentence.
2 - Translate the summary into German.
3 - List each name in the German summary.
4 - Output a json object that contains the
  following keys: german_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in German summary>
Output JSON: <json with summary and num_names>

Text: <{text}>

### Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion


Determine if the student's solution is correct or not.

Question:
I'm building a solar power installation and I need help \
working out the financials.
- Land costs €100 / square meter
- I can buy solar panels for €250 / square meter
- I negotiated a contract for maintenance that will cost \
me a flat €100k per year, and an additional €10 / square \
meter
What is the total cost for the first year of operations \
as a function of the number of square meter.

Student's Solution:
Let x be the size of the installation in square meter.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000

#### **Note** that the student's solution is actually not correct.
#### We can fix this by instructing the model to work out its own solution first.

Your task is to determine if the student's solution \
is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem.
- Then compare your solution to the student's solution \
and evaluate if the student's solution is correct or not.
Don't decide if the student's solution is correct until
you have done the problem yourself.

Use the following format:
Question:
```
question here
```
Student's solution:
```
student's solution here
```
Actual solution:
```
steps to work out the solution and your solution here
```
Is the student's solution the same as actual solution \
just calculated:
```
yes or no
```
Student grade:
```
correct or incorrect
```

Question:
```
I'm building a solar power installation and I need help \
working out the financials.
- Land costs €100 / square meter
- I can buy solar panels for €250 / square meter
- I negotiated a contract for maintenance that will cost \
me a flat €100k per year, and an additional €10 / square \
meter
What is the total cost for the first year of operations \
as a function of the number of square meter.
```
Student's solution:
```
Let x be the size of the installation in square meter.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```
Actual solution:






