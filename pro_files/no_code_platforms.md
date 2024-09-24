---
layout: page
title: Designing AI ChatBots using no-code platforms
subtitle: Basic directions
---

# Designing AI ChatBots using no-code platforms

In hands-on sessions related to designing and implementing AI ChatBots using LangChain and OpenAI API, we show one approach to that process. Specifically, we can use other APIs, such as Hugging Face, Anthropic, Google, Meta LLaMA, Mistral, etc.  In essence, that approach and similar approaches (e.g., RASA) share one characteristic: some knowledge of Python programming. These days, no-code platforms offer an alternative to coding practices for AI ChatBots and AI assistant development and implementation. There are many options among such platforms as:

1. [VoiceFlow](https://www.voiceflow.com/)
2. [Botpress](https://botpress.com/)
3. [ChatBot](https://www.chatbot.com/)

> **REMARK:** The listed platforms offer low-code functionality implementation, but the standard methodology for designing ChatBots revolves around using GUI-like elements to build conversational flow. 

One could list many differences among the platforms mentioned, but our focus differs. In hands-on sessions, we will work only with VoiceFlow, an alternative approach for accomplishing the final project related to the listed [Final project requirements](./final_project.md). The primary methodology to design and develop chatbots on Voiceflow is:

### 1. Define the Use Case
Identify the purpose of your chatbot: Is it for customer service, lead generation, or a more conversational assistant? Define the problem that needs to be solved with a chatbot.
Set clear goals: What would you like the chatbot to do (e.g., answering FAQs, booking services, recommending products, canceling subscriptions, providing web-shopping support, etc.)?

### 2. Create the Conversational Flow

Use a visualization tool (e.g., [miro](miro.com) )to create conversational flow on a conceptual level. Understanding the desired conversational behavior of the future AI ChatBot is essential without being overwhelmed by the technological implementation nuances. This will be the fundamental starting point for building conversational flow in `VoiceFlow Workplaces.`   

From the conceptual conversational flowchart created, start building an AI ChatBot using Voiceflow’s drag-and-drop interface to make the conversation structure. Each block represents a conversational element, such as messages, questions, or conditions.
Define user inputs: Voiceflow supports multiple types of user inputs (text, buttons, voice), so decide how users will interact with the bot.
Based on user responses, map out different paths. Add conditions to guide users down other paths or decision trees and employ AI as a response defined by a well-designed prompt. 

### 3. Set Up Intents and Natural Language Understanding (NLU)
Define Intents: Group possible user inputs into "intents" representing a specific goal, like ordering food or asking for store hours.
Train NLU: Provide examples of phrases that users might say for each intent—the more diverse the training data, the better the bot’s understanding.
Entity Recognition: Identify specific entities in user inputs (e.g., dates, product names, locations) and train the bot to recognize and handle them.

### 4. Leverage ChatBot with KnowledgeBase

Define if you need the knowledge base to provide AI with specific domain knowledge related to the problem associated with AI Chatbots. Support for different file types, documents, and URL(s) or whole Sitemaps is available. This way, a sort of RAG (Retrieval Augmented Generation) system can be developed. 

### 4. Add Dynamic Content and Integrations

  - Use Variables: Voiceflow allows you to store and reference variables (e.g., user’s name, order details) throughout the conversation to personalize interactions.
  - Integrate APIs: APIs can retrieve or send data dynamically, such as by querying a database, fetching real-time information, or sending forms.
  - Add JS Functions (Low-Code): For more complex logic or integrations, you can add custom JavaScript functions to handle data manipulation, API calls, or more detailed workflows.
