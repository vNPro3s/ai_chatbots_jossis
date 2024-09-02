import openai

def get_completion(prompt:str, client, model:str="gpt-4o", temperature:float=0.0) -> str:
    messages = [
        { "role": "user", "content": prompt }
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature= temperature # this is degree of randomness of the model output
    )
    
    return response.choices[0].message.content


def get_completion_from_messages(messages:list, client, model:str="gpt-4o", temperature:float=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature= temperature # this is degree of randomness of the model output
    )
    #     print(str(response.choices[0].message))
    return response.choices[0].message.content
