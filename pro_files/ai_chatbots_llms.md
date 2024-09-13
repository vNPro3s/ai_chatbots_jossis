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

Let us return to LLMs as generative AI systems that can forecast and generate the next most probable word following a sequence of words. We will explain that tokens, not words, are in play. Usefull starting point for taking about tokenization is [Tiktokenizer web app](https://tiktokenizer.vercel.app/), and we will introduce following examples:

```
Ｕｎｉｃｏｄｅ! 🅤🅝🅘🅒🅞🅓🅔‽ 🇺‌🇳‌🇮‌🇨‌🇴‌🇩‌🇪! 😄 The very name strikes fear and awe into the hearts of programmers worldwide. We all know we ought to “support Unicode” in our software (whatever that means—like using wchar_t for all the strings, right?). 

Nito wo oumono ha itto mo ezu・二兎を追う者は一兎をも得ず

```

```python
class Scalar:
    
    def __init__(self, value:float, operands:Set=None, label:str="", operator:str="") -> None:
        
        self.scalar = value
        self.operands = operands
        self.label = label
        self.operator = operator
        
    # defining a string representation of this class
    def __repr__(self) -> str:
        if self.label == "": 
            if self.operands is None:
                represent_as = f"[{self.scalar}]"
            else:
                represent_as = f"[{self.scalar} | {self.operands}]"
        else:
            if self.operands is None:
                represent_as = f"[{self.scalar} | {self.label}]"
            else:
                represent_as = f"[{self.scalar} | {self.label} | {self.operands} | {self.operator}]"    
            
        return represent_as
```


[^1]: Adrian Thompson: ChatGPT for Conversational AI and ChatBots, Packt Publishing, 2024.
