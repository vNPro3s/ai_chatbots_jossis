---
layout: page
title: AI ChatBots and LLMs
subtitle: Fundamentals of AI Chatbots and LLMs
---

# AI ChatBots and LLMs

There are many definitions, but we will start with the following:

"An AI chatbot is an intelligent system composed of natural language processing components, machine learning, and knowledge base integration that enables dynamic, context-aware, and human-like conversations. It can understand, process, and generate human language, adapt to different interaction scenarios, and perform specific tasks such as answering queries, providing recommendations, or automating services."

In this course, we focus specifically on text-to-text AI ChatBots while recognizing the multimodal capabilities of contemporary ChatBots, such as those that can handle text, voice, and images.

The field of ChatBots dates back to the 1960s, and since then, huge advancements have been detected, especially in the last decade. Figure 1 depicts a timeline with some notable contributions in that field.

![timeline_catbots](../assets/img/timeline_chatbots.jpg)

**Figure 1** Timeline with the origin of different chatbots (Source: Chakraborty, C. et al.,  Overview of Chatbots with special emphasis on artificial intelligence-enabled ChatGPT in medical science, Frontiers in Artificial Intelligence, Volume: 6-2023)

The first chatbots were restricted to performing only a limited pre-programmed response. So-called `rule-based chatbots` follow predefined rules in answering prepared questions, similar to the FAQs section. They are designed to respond to those questions, provide limited information, or guide users through specific tasks. Their minimal capabilities do not offer any flexibility, which often leads to blind street scenarios, frequently producing user dissatisfaction. 

On the other hand, AI Chatbots, or sometimes Conversational AI-driven Chatbots, refer to sophisticated technological solutions that enable computers (machines in general) to converse with humans or other machines using natural language. Advancements in various fields, such as NLP, ML, DL, database, and dialog management, led to the rapid development of AI chatbots that solved most of the shortcomings of rule-based chatbots and offered higher flexibility. The core features of conversational AI ChatBots are[^1]:

  - Understanding of Context: NLU systems comprehend the broader context of a conversation, processing words about the surrounding text or dialogue. 

  - Semantic Understanding: These systems grasp the meaning of words, including synonyms, slang, dialects, and jargon, often through entity recognition, allowing for a more nuanced understanding of user input.

  - Handling of Ambiguity: NLU systems can interpret vague or ambiguous expressions using contextual clues, inferring the most likely meaning based on the previous conversation.

  - Intent Recognition: NLU identifies the underlying intent of a user’s words, understanding what the user wants to accomplish, not just the literal meaning of the input.

  - Entity Recognition: The system identifies and categorizes specific named entities (like persons, locations, dates) within the text, enabling more precise interpretation.

  - Slot Filling: Extracts relevant information from user input (based on entity recognition) and places it into predefined slots for later use, such as booking a hotel or making an appointment.

  - Sentiment Analysis: NLU systems assess the emotional tone of a user’s input, determining whether they are happy, frustrated, or upset and adjusting the response accordingly.

  - Conversation Management: NLU systems track the history and flow of a conversation, managing interruptions, topic changes, and follow-up questions to create smoother, human-like interactions.

  - Multilingual Capability: Advanced NLU systems can understand and respond in multiple languages, enabling global communication and customer service.

  - Integration with External Systems: NLU systems can connect to external databases, CRMs, or APIs, allowing real-time data retrieval for more personalized and relevant responses.

AI Chatbots are utilized in various sectors, such as customer service, language translation, education, healthcare, banking, insurance, retail, and human resources. Most modern AI ChatBots are built around large language models (LLMs), and this course is interested in such systems. 

## Large Language Models (LLMs)

When Vaswani et al. published their paper "Attention is All You Need" in 2017, they never imagined the powerful impact of the proposed `Transformer` architecture. Firstly, their focus was only on machine translation, but transformer architecture with derivatives soon showed tremendous potential in many other tasks. It revolutionized natural language processing (NLP) because it can process text data efficiently, capture long-range dependencies in sentences, and work in parallel across sequences. This architecture uses self-attention and positional encoding to analyze relationships between words in a sentence, allowing it to understand context better than previous models. More broadly speaking, LLMs are part of generative AI systems. 

{: .box-note}
Generative AI refers to deep learning models that generate text, computer code, 3D simulations, images, audio, or video based on a large amount of representative training data.

Examples:

 - ChatGPT (text 	&#8614; text) [...](https://chat.openai.com/) &rarr; [openai.com](https://openai.com/)
 - Gemini (text 	&#8614; text) [...](https://gemini.google.com/app)
 - DALL·E 2 (text &#8614; image)
 - DALL·E 3 (text &#8614; image) `under chatGPT Plus`
 - Midjourney (text &#8614; image) [...](https://www.midjourney.com/)
 - SORA (text &#8614; video)[...](https://openai.com/sora)

 We can reach the DALL·E 3 model by using [bing &rarr; copilot](https://www.bing.com/new)

**Remark:** Many listed models are multimodal, and basic differences between unimodal and multimodal models are shown in figure 2.

![uniVsMulti](https://onedrive.live.com/embed?resid=C39637E73EC828A%2169367&authkey=%21AJI48uyXHWC8hgA&width=681&height=362) 

**Figure 2** Unimodal vs Multimodalk Generative AI systems (Source: Cao, Y., Li, S., Liu, Y., Yan, Z., Dai, Y., Yu, P. S., & Sun, L. (2023). A comprehensive survey of ai-generated content (aigc): A history of generative ai from gan to chatgpt. arXiv preprint arXiv:2303.04226.)

Let us return to LLMs as generative AI systems that can forecast and generate the next most probable word following a sequence of words. We will explain that tokens, not words, are in play. A useful starting point for talking about tokenization is [Tiktokenizer web app](https://tiktokenizer.vercel.app/).

Figure 3 shows text in the app, while Figures 4 and 5 depict tokenization with a GPT2 tokenizer. 

![tiktokenizer_text](../assets/img/tiktokenizer_text.jpg)

**Figure 3** Input examples in GPT2 tokenizer

![tokens_text](../assets/img/tokens__text_1.jpg)

**Figure 4** Tokenization with GPT2 tokenizer of the textual part of the input 

![python_tokend](../assets/img/python_tokens.jpg)

**Figure 5** Tokenization of the input Python code using GPT2 tokenizer

Figure 6 shows that the token for the unique character `🅝` consists of three-byte values. The numerical part represents byte-coded values from the Byte Pair-encoding algorithm applied to UTF-8 byte-coded points of tokens. That algorithm is used for token representation compression. 

![token](../assets/img/unicode_token.jpg)

**Figure 6** Byte values for the Unicode character `🅝`

For further clarification, let's isolate just a short part of the text and print all code-point values of characters: 

```python
text = "Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪!"
print(f"Length of isolated part of the text: {len(text)}")
code_points = [ord(char) for char in text]
print(f"Code points:\n{code_points}")
```
Output would be:

```
Length of isolated part of the text: 32
Code points:
[65333, 65358, 65353, 65347, 65359, 65348, 65349, 33, 32, 127332, 127325, 127320, 127314, 127326, 127315, 127316, 8253, 32, 127482, 8204, 127475, 8204, 127470, 8204, 127464, 8204, 127476, 8204, 127465, 8204, 127466, 33]
```

Now, encode that in utf-8 as bytes:

```python
tokens_utf8 = list(text.encode('utf-8'))
print(f"Length of isolated part of the text encoded with utf-8: {len(tokens_utf8)}")
print(f"Byte representation of tokens encoded with utf-8:\n{tokens_utf8}")
```

Output:

```
Length of isolated part of the text encoded with utf-8: 102
Byte representation of tokens encoded with utf-8:
[239, 188, 181, 239, 189, 142, 239, 189, 137, 239, 189, 131, 239, 189, 143, 239, 189, 132, 239, 189, 133, 33, 32, 240, 159, 133, 164, 240, 159, 133, 157, 240, 159, 133, 152, 240, 159, 133, 146, 240, 159, 133, 158, 240, 159, 133, 147, 240, 159, 133, 148, 226, 128, 189, 32, 240, 159, 135, 186, 226, 128, 140, 240, 159, 135, 179, 226, 128, 140, 240, 159, 135, 174, 226, 128, 140, 240, 159, 135, 168, 226, 128, 140, 240, 159, 135, 180, 226, 128, 140, 240, 159, 135, 169, 226, 128, 140, 240, 159, 135, 170, 33]
```

We see that the length of encoded code points is larger than the number of code points. The reason is simple &rarr; simple characters e.g., `a` are encoded with one byte, while "complex characters", like `🅤` are encoded with up to 4 bytes. That is why we need to employ some compression &rarr; `Byte pair encoding algorithm`. In that process, many individual tokens are merged (analyze the output of Tiktokenizer for our examples, and that becomes obvious).  We will change the tokenizer to GPT-4o (Figure 7).

![tokenizer_gpt-4o](../assets/img/tokenizer_gpt-4o.jpg)

**Figure 7** Tokenization of the same examples with GPT-4o tokenizer

First, we can notice the number of total tokens and &rarr with the GPT2 tokenizer, it was 585, and with GPT-4o, it was 317. Close inspection shows that significant compression is because of the improvement in block code tokenization in gpt-4o tokenizer (Figure 8):

|                                                        |                                                                 |
|:------------------------------------------------------:|:---------------------------------------------------------------:|
| ![python_tokens_gpt2](../assets/img/python_tokens.jpg) | ![python_tokens_gpt-4o](../assets/img/python_tokens_gpt-4o.jpg) |
|                             (a)                        |                           (b)                                   |


**Figure 8** GPT2 tokenizer (a) has more fragmented tokenization of Python block codes compared to GPT-4o tokenizer (b)

The fragmentation of block codes in the GPT2 tokenizer is one of the main reasons GPT2 performed poorly in coding tasks compared to GPT-4o and other LLMs. As shown in the above examples, `tokenization` parses input text into meaningful constituent parts called `tokens`. Tokenization is the first step in presenting textual data to the computer for further processing. Besides efficient tokenization, we need a so-called `embedding` layer that consists of all tokens called `vocabulary`. Simplified, the embedding layer can be seen as a table with vocabulary tokens as rows and columns as components of multidimensional vector space. Vector space dimensionality, or embedding dimensionality, is hyper-parameter (e.g., 12288). The embedding layer is usually trained with LLM, so it starts with random values and ends with a meaningful representation of tokens in multidimensional space learned from the training dataset &rarr; for each token, there is a row in the embedding table that is a representation of the token in multidimensional vector space with numerical components.    




[^1]: Adrian Thompson: ChatGPT for Conversational AI and ChatBots, Packt Publishing, 2024.
