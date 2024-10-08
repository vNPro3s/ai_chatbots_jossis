---
layout: page
title: Designing AI ChatBots using no-code platforms
subtitle: Basic directions
---
  
# Designing AI ChatBots using no-code platforms

In hands-on sessions related to designing and implementing AI ChatBots using LangChain and OpenAI API, we show one approach to that process. Specifically, we can use other APIs, such as Hugging Face, Anthropic, Google, Meta LLaMA, Mistral, etc.  In essence, that approach and similar approaches (e.g., [RASA](https://rasa.com/)) share one characteristic: some knowledge of Python programming. These days, no-code platforms offer an alternative to coding practices for AI ChatBots and AI assistant development and implementation. There are many options among such platforms as:

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

   - Define Intents: Group possible user inputs into "intents" representing a specific goal, like ordering food or asking for store hours.
   - Train NLU: Provide examples of phrases that users might say for each intent &rarr; the more diverse the training data, the better the bot’s understanding.
   - Entity Recognition: Identify specific entities in user inputs (e.g., dates, product names, locations) and train the bot to recognize and handle them.

### 4. Leverage ChatBot with KnowledgeBase

Define if you need the knowledge base to provide AI with specific domain knowledge related to the problem associated with AI Chatbots. Support for different file types, documents, and URL(s) or whole Sitemaps is available. This way, a sort of RAG (Retrieval Augmented Generation) system can be developed (create responses with AI plus Knowledge Base, or complex AI Sets plus Knowledge Base, and finally intelligently integrate blocks for KB Search). 

### 5. Add Dynamic Content and Integrations

  - Use Variables: Voiceflow allows you to store and reference variables (e.g., user’s name, order details) throughout the conversation to personalize interactions.
  - Integrate APIs: APIs can retrieve or send data dynamically, such as by querying a database, fetching real-time information, or sending forms.
  - Add JS Functions (Low-Code): For more complex logic or integrations, you can add custom JavaScript functions to handle data manipulation, API calls, or more detailed workflows.

### 6. Design for Error Handling and Edge Cases
   - Fallbacks: Always define a fallback for when the bot doesn’t understand the user, such as a “Sorry, I didn’t catch that” message.
   - Context Management: Manage conversation state with context-based flows, ensuring the bot remembers essential details across multiple exchanges.
        - This is a problem in VoiceFlow because limited context management can be achieved with good organization and usage of predefined or user-defined variables and conditions. On the other hand, AI Response blocks can memorize only a short context of the conversation. So, creating a memory block is one way of resolving this problem.


&nbsp;

     > Response AI block with Knowledge Base does not offer context management by default!

### 7. Test and Iterate

   - Test Conversations: Use Voiceflow’s testing tools to simulate interactions and troubleshoot issues such as incorrect intents, broken flows, or variable mismanagement.
   - Gather Feedback: You can deploy your chatbot in a limited capacity and gather feedback to understand user behavior and improve the bot's accuracy and efficiency.
   - Improve Based on Data: Regularly review logs and analytics to optimize conversation flows, improve NLU accuracy, optimize prompt design, and refine responses.

### 8. Deploy

   - Multi-Platform Deployment: Once satisfied, Voiceflow allows you to deploy your chatbot across multiple platforms, including websites, mobile apps, WhatsApp, Discord, Microsoft Teams, etc.
   - Channel-Specific Optimization: Ensure your chatbot is optimized for the platform it will be deployed on (e.g., voice-specific flows for Alexa, text-based flows for Slack or web).

From [official VoiceFlow documentation](https://docs.voiceflow.com/docs/voice-deployment-overview):

{: .box-warning}
**Warning:** Voiceflow does not have a built-in automatic speech recognition (ASR) or speech-to-text (STT) solution. 
Use a third-party ASR or STT platform to transcribe your users' input before passing it to our APIs to retrieve the next set of responses.
     
### 9. Monitor and Optimize

   - Analytics: Continuously monitor chatbot performance via analytics, identifying areas for improvement, user drop-off points, and engagement rates.
   - Continuous Training: Based on real-world usage, continue training the NLU with new examples and add additional edge cases or error-handling mechanisms.
   - Prompt optimization: Continually try to obtain better AI responses by improving prompts. 


{: .box-success}
In our hands-on sessions, steps 8. and 9. will not be covered, and some limited ways of integration will be explained and demonstrated. 

{: .box-error}
Take special care in choosing an AI model. Different models "eat" tokens at different rates, and not all models are available under the free tier.  

{: .box-error}
When changing an AI model, you will need to alter prompts to obtain the desired responses, and sometimes, responses from some models will be very distant from the desired behavior. 

{: .box-warning}
Simplified: The System prompt in the AI Response block is the model's intentional role or provided context for the response. On the other hand, Prompts are most frequently dynamically generated input content based on user interactions or previous messages in the conversation.

VoiceFlow provides well-organized and extensive [documentation](https://docs.voiceflow.com/docs/welcome) accompanied by many video tutorials. 
