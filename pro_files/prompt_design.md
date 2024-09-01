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

## Tactic I. Write clear and specific instructions 

You must be clear about the task and provide essential details or context.

| Starting prompt | Enhanced version|
| Summarize the following text| Summarize the following text in a maximum of one paragraph of 200 words. |
| How can I create a Questionnaire | Create an anonymous general questionnaire about customer product satisfaction in HTML. Provide comments with short explanations of important code parts.|   
| How do I calculate mean and standard deviation in Excel? | I have a column for monthly customer spending named "MNTH_SPENDING." Explain how to calculate in Excel the mean spending shown in cell "AVG" and the corresponding standard deviation in the cell called "STD." |

Let us try this. Open a notebook [prompt_design_1.iynb](../notebooks/propt_design_1.ipynb), and download `helper functions` in [aux_functions.py](../notebooks/helper_funk/aux_functions.py). Put it under the same folder in the helper_funk/info.txtVSC project folder. 


## Tactic II. Use the delimiters 

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

## Tactic III. Specify the length of the response

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

## Tactic IV. Ask for the structured output

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
