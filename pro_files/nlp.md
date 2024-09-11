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

## 1. Question Answering 

(Jeopardy - won by IBM's Watson in 2011.)

## 2. Information extraction:

`The first lecture meeting for NLP will be on Monday, 9th of October, in P39, from 09.30 AM to 11.00 AM.`

&nbsp;

![img_calendar_entry](../assets/img/calendar_entry.jpg)

## 3. Sentiment Analysis (e.g. Movie Reviews)

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

## 4. Machine translation

 - Google translate
 - Stanford's Phrasal
 - iTranslate
 - Microsoft Translator
 - DeepL Translator

There is a considerable effort in the NLP community to develop efficient and reliable helpers for human translators.

> For AI ChatBots there is sometimes a need to translate user inputs.


## 5. Text Classification

 - Spam detection
 - Classifying web pages
 - Classifying content of web pages
 - Classifying written works

> As pointed out, sentiment analysis is also a text classification task.

The main problem is that textual data can't be directly processed by computers &rarr; it requires some vectorization. The AI ChatBots and LLMs (Large Language Models) section will discuss this issue more deeply. Figures 1 and 3 show this, while Figure 2 depicts the preprocessing phase of text vectorization. 

![raw_text_input](../assets/img/text_classification_1.jpg)

**Figure 1** Raw text can not be processed directly (WEKA)

![filter](../assets/img/string_to_word_vector.jpg)

**Figure 2** Preprocessing raw text using `StringToWordVector` filter in WEKA

![vectorized_training](../assets/img/vectorized_training.jpg)

**Figure 3** Vectorized training data 

The process of text vectorization in a broader sense consists of several phases: tokenization, then N-gram detection according to the TF-IDF measure, stop-words removal, stemming, and lemmatization, which is part of the so-called text normalization process. Case folding is the most straightforward normalization process, and it can also be done. This represents NLP techniques used in various NLP tasks, and we will briefly discuss it later in this section. 

> IMPORTANT: In the context of LLMs, vectorization is used in a slightly different manner  

Now, we want to focus on classification as one of the major tasks in Machine Learning. Machine learning (ML), with the subfield of deep learning (DL), nowadays represents one of the most advanced fields of artificial intelligence (AI). Vastly simplified, the goal of ML and DL is to develop models that can solve some task (e.g., classification) by learning from data rather than algorithmically coding behavior to them (Figure 4).

![ML_DL_simply](../assets/img/Learning_ML_DL.jpg)

**Figure 4** Simplified process of learning from data in ML and DL

The model learns from training data by changing its parameters in a broader sense because some objective function needs to be optimized (usually minimized). The independent test dataset evaluates how well the model has learned the task. The main goal is to get a model that performs well on training and test datasets, measured by some performance measure, or we say that it learned to generalize from data. The main problems that can not be avoided in such a process are `overfitting` or `underfitting.`

Overfitting occurs when the model performs too well on the training dataset but fails somewhat on the test dataset, and it is detectable through performance measures.
Underfitting is the opposite problem when the model underperforms on training and testing datasets no matter how many representative instances we collect for the training and testing phase. 

After we learn some fundamentals of ML and DL, the main fields in AI, we can proceed to a concrete example of text classification, one of the main tasks in NLP. Classification is the task in which a model needs to learn how to place a particular sample into the corresponding group with the known label. Domain experts usually specify the labels and need to have concrete semantic meanings. This type of learning in which input-output pairs are known for all instances in training/test datasets is called `supervised learning`. On the other hand, learning with known only inputs is called `unsupervised learning` (e.g., clustering). 

For demonstration, the text dataset [Tweets Dataset for Detection of Cyber-Trolls](https://www.kaggle.com/datasets/dataturks/dataset-for-detection-of-cybertrolls) from Kaggle is used. There are two classes, `Troll Tweets` and `Non-troll tweets`. We divided the vectorized original dataset in a 70% to 30% ratio for training and testing datasets. Three models were employed: Naive Bayes, KNN (K=3), and Random Forest. 

Results:

|Model|ACC|AUC|F-measure|
| :----- | ----: | ----: | ----------: |
|NB|52.658%|0.663|0.511|
|KNN (K=3)|71.371%|0.840|0.702|
|Random Forest|92.385%|0.962|0.924|

The Random forest model was chosen as the best model according to the evaluation measures in this experiment.



