# Prompt Design

From the topic related to LangChain and AI Chatbots, we observed that the prompt plays a crucial role in the quality of AI chatbots. Also, in this part of the hands-on, we demonstrated the so-called `hallucination` problem of the LLMs with minor changes in prompt template design. To conclude, prompt design is crafting prompts that produce desired, high-quality, reliable LLMs or AI Chatbot results.  

There are some recipes for efficient, prompt design. Contemporary LLMs are trained on reliable and accessible data from the entire Internet. That means their knowledge is broad (but again restricted), and to get a desired answer, one needs to pose well-coined questions (prompts). Here, the known proverb is true:

> It is better to pose a good question than give an excellent answer to a wrong one.
(Anonymous)

When designing a good prompt, have in mind the following:

 - at this stage, the reasoning of LLMs is different than the reasoning of humans (what is evident for humans is not for LLMs)
 - the vagueness of natural language can produce misunderstanding
 - knowledge base of some topics shares the same or similar terminology


{: .box-success}
**Hint** To avoid undesired results, please ensure that model guessing is minimal.

Many companies behind LLMs developed `Prompt Design Cookbooks` or recipes for writing good prompts. We will present some strategies from those cookbooks.

# Strategies for designing prompts

As in any context, the strategy here refers to high-level planning and decision-making to achieve specific results. It provides a broad, overarching framework without diving into the finer details. In contrast, tactics are specific, concrete actions aligned with the strategy, detailing the steps needed to implement the strategic plan effectively.

There are many proposed strategies for designing good prompts, and here, we will focus only on some well-known ones.

## Strategy I. Write clear and specific instructions 

You must be clear about the task and provide essential details or context.

| Starting prompt | Enhanced version|
| Summarize the following text| Summarize the following text in a maximum of one paragraph of 200 words. |
| How can I create a Questionnaire | Create an anonymous general questionnaire about customer product satisfaction in HTML. Provide comments with short explanations of important code parts.|   
| How do I calculate mean and standard deviation in Excel? | I have a column for monthly customer spending named "MNTH_SPENDING." Explain how to calculate in Excel the mean spending shown in cell "AVG" and the corresponding standard deviation in the cell called "STD." |

Let us try this. Open a notebook [prompt_design_1.iynb](../notebooks/propt_design_1.ipynb), and download `helper functions` in [aux_functions.py](../notebooks/helper_funk/aux_functions.py). Put it under the same folder in the helper_funk/info.txtVSC project folder. 


## Tactic I. Use the delimiters 

Use the delimiters to indicate distinct parts of the input. Standard delimiters used in the prompt design:

 - triple quotes """
 - triple backticks ```
 - triple dashes ---
 - angle bracket < >
 - XML tags

```

review = """
I recently purchased the X500 Wireless Headphones from SoundTech Innovations, \
and I am thoroughly impressed. The sound quality is exceptional, and the battery \
life exceeds my expectations. The comfortable fit makes them perfect for long \
listening sessions. Highly recommend these headphones for anyone in need of top-notch audio performance.
"""
```

```
prompt = f""" Analyze the review  in the angle bracket so it \
can be classified as positive, negative, or neutral reviews.

<{review}>
"""
```

## Tactic II. Specify the length of the response

Define the desired length of the produced output from LLMs. Consider the defined length in terms of how many words, sentences, paragraphs, list length, etc., are at the most approximate value to be satisfied. 

```
USER
Summarize the text delimited by triple quotes in about 50 words.

"""insert text here"""
```
```
USER
Summarize the text delimited by triple quotes in 2 paragraphs.

"""insert text here"""
```
```
USER
Summarize the text delimited by triple quotes in 3 bullet points.

"""insert text here"""

```

## Tactic III. Ask for the structured output

Sometimes it is helpful to ask the model to produce output in the desired format &rarr; `JSON`, `HTML`, `list`, or some other appropriate format. In previous examples of user reviews, we my be interested in obtaining structured output with pair key-values (JSON file).

```

review = """
I recently purchased the X500 Wireless Headphones from SoundTech Innovations, \
and I am thoroughly impressed. The sound quality is exceptional, and the battery \
life exceeds my expectations. The comfortable fit makes them perfect for long \
listening sessions. Highly recommend these headphones for anyone in need of top-notch audio performance.
"""
```

```
prompt = f""" Analyze the review  in the angle bracket and provide output in the form \
of JSON file (key: values) with the following keys and values definitions:

product: name of the product (if not known, write unknown)
brand: name of the brand (if not known, write unknown)
review: review summaries (if the review is longer than 300 words, otherwise original review)
opinion: positive, negative or neutral (if not possible to detect, write unable to detect)

<{review}>
"""
```

Tactic IV. Check the conditions

Check if the input contains instructions, and if it does, write the response in the desired structured format, following the steps in the sequence.


```
text_1 = f"""
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
```

```
prompt = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \ 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, \ 
then simply write \"No steps provided.\"

\"\"\"{text_1}\"\"\"
"""
```

## Tactic V. Provide examples

When we design a prompt without giving examples to the model, we are using **zero-shot** prompting. Zero-shot prompting is plain instructions on what the model needs to do using only previous knowledge. It has been used for simple, well-defined tasks that are generally known. 

Typical example

```
Customer review --> find the sentiment of the review.
 
```

Without providing examples of positive, negative, or neutral sentiments, the model will give an output correctly.

We are designing so-called **few-shot** prompts by providing the model with a few examples (usually 1 to 5) of performing a task. In some way, we can consider the few-hot prompting as additional training for the model. The examples help the model understand the format and type of desired output.

In few-shot prompting examples, enables:

 - model to generalized based on the provided input-output relations &rarr; supervised learning
 - some tutorial on how to perform tasks and what the expected format for output
 - model to cope with the more complex tasks

```
SYSTEM
Answer in a consistent style.
USER
Teach me about patience.
ASSISTANT
The river that carves the deepest valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.
USER
Teach me about the ocean.
```

# Strategy II. Give the model time to "think"

The main goal is to structure a prompt in a way that pushes the model to think about a task like humans, considering more aspects of the problem at hand before providing a final answer. 

## Tactic I. Specify the steps required for task completion.

```
input text in English language

SYSTEM -> perform the following actions:

1. Summarize the input text in one sentence
2. Translate the summary in German
3. List each name in German summary
4. Output the JSON object with keys: german_summary, names

Separate your answers with line breaks.
```
## Tactic II. Specify the output format

That is the only formalization of the previous tactic. 

```
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the 
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>
```

## Tactic III. Instruct the model to work out its solution before rushing to a conclusion

Sometimes, we get better results when explicitly instructing the model to reason from first principles before concluding. Suppose, for example, we want a model to evaluate a student’s solution to a math problem. The most obvious way to approach this is to ask the model if the student's solution is correct.

```
SYSTEM
Determine if the student's solution is correct or not.
```
```
USER
Problem Statement: I'm building a solar power installation and I need help working out the financials.
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot
- I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot
What is the total cost for the first year of operations as a function of the number of square feet.

Student's Solution: Let x be the size of the installation in square feet.
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```
```
ASSISTANT
The student's solution is correct.
```

# Iterative prompt development

Even when you know the strategies and corresponding tactics in prompt development, the first solution is frequently unsatisfying. So, the logical path is toward iterative prompt development. 

[img_iterative](../assets/img/iterative.jpg)
**Figure 1** Iterative prompt development (Sorce: DeepLeaarning.AI)





