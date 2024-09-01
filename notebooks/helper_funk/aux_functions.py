import openai

def get_completion(prompt:str, client, model:str="gpt-4o"):
    messages = [
        { "role": "user", "content": prompt }
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0 # this is degree of randomness of the model output
    )
    
    return response.choices[0].message.content
