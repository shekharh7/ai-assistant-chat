import openai

openai.api_key = "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"
messages = []


#Append the message to the conversation history 
def add_message(role, message):
    messages.append({"role": role, "content": message})

def converse_with_chatGPT():
    model_engine = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model_engine, #Open AI model name
        messages=messages, # user query
        max_tokens = 1024, # this is the maximum number of tokens that can be used to provide a response.
        n=1, #number of responses expected from the Chat GPT
        stop=None, 
        temperature=0.5 #making responses deterministic
    )
    # print(response)
    message = response.choices[0].message.content
    return message.strip()

# process user prompt
def process_user_query(prompt):
    user_prompt = (f"{prompt}")
    add_message("user", user_prompt)
    result = converse_with_chatGPT()
    return result

#Request user to provide the query
def user_query():
    while True:
        print("How can I help you")
        prompt = input("Enter :  ")
        response = process_user_query(prompt)
        return response

