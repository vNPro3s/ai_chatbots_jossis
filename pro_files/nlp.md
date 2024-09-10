---
layout: page
title: Natural Language Processing
subtitle: Short intro to NLP
---

# Natural Language Processing (NLP)

> Why do we need NLP in AI ChatBots?

The heart of an AI chatbot is its ability to understand and process user inputs, typically in natural language (e.g., English, German, Croatian, etc.). Besides that, Natural Language Processing (NLP) 
have tools for chatbots to interpret, analyze, and generate human language, allowing them to interact with users effectively in a conversational manner.

> Natural Language Processing (NLP) is an interdisciplinary field that deals with different tasks performed by computers based on content derived from human language.

# Computer tasks in NLP

1. Question Answering (Jeopardy - won by IBM's Watson in 2011.)
2. Information extraction:

`The first lecture meeting for NLP will be on Monday, 9th of October, in P39, from 09.30 AM to 11.00 AM.`

&nbsp;

![img_calendar_entry](../assets/img/calendar_entry.jpg)

3. Sentiment Analysis (e.g. Movie Reviews)

![movie_reviews](../assets/img/csv_as_df.jpg)

The original dataset is from Kaggle [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews?resource=download&select=IMDB+Dataset.csv) and we will use it on `hands-on` afternoon session. 

In this NLP task, we usually have a human-generated opinion in text format, which can be classified as positive, negative, or neutral sentiment. Other types of sentiment analysis can encompass a wide range of nuances related to sentiment, but in most cases, the three-class analysis is the most common.

![laptop](../assets/img/laptop.jpg)

Attributes: build quality, battery life, keyboard quality, CPU throttling, thermal profile

![sentiments_laptop](../assets/img/computer_sentiments.jpg)

By scaling attributes with the average rating value, we can obtain a more differentiated overview of each attribute's quality.   

![scaling_att](../assets/img/attributes_sentiment.jpg)

Standard examples of sentiment analysis:

 - Movie reviews &rarr; positive, negative or neutral &Rarr; movie recommendations
 - Product comparisons &rarr; e.g., scaling attributes
 - Public sentiment &rarr; How is consumer confidence - is despair increasing? &Rarr; economy crisis prediction
 - Politics &rarr; what do people think about presidential candidates &Rarr; predicting election results
 - Market analysis &rarr; predicting market trends from customer opinions
   
Sentiment analysis has many other names:

 - **Opinion extraction**
 - **Opinion mining**
 - **Sentiment mining**
 - **Subjectivity analysis**

> In the context of AI ChatBots, in some chat scenarios, it is helpful to give the ChatBot an understanding of the user's emotional state and to learn how to respond appropriately. 

4. Machine translation

 - Google translate
 - Stanford's Phrasal
 - iTranslate
 - Microsoft Translator
 - DeepL Translator

There is a considerable effort in the NLP community to develop efficient and reliable helpers for human translators.

> For AI ChatBots there is sometimes a need to translate user inputs.


5. Text Classification

 - Spam detection
 - Classifying web pages
 - Classifying content of web pages
 - Classifying written works

> As pointed out, sentiment analysis is also a text classification task.

The main problem is that textual data can't be directly processed by computers &rarr; it requires some vectorization. We will discuss this issue more deeply in the AI ChatBots and LLMs (Large Language Models) section. Figures 1 and 3 show this, while Figure 2 depicts the preprocessing phase of text vectorization. 

![raw_text_input](../assets/img/text_classification.jpg)

**Figure 1** Raw text can not be processed directly (WEKA)

![filter](../assets/img/string_to_word_vector.jpg)

**Figure 2** Preprocessing raw text using `StringToWordVector` filter in WEKA

![vectorized_training](../assets/img/vectorized_training.jpg)

**Figure 3** Vectorized training data 

