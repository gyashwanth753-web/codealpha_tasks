def Jarvis(user_input):
    user_input = user_input.lower()

    if user_input == "hi" or user_input == "hello":
        return "Hi! Nice to meet you."
    
    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"
    
    elif user_input == "what is your name":
        return "I am a Jarvis , a simple rule-based chatbot."
    
    elif user_input == "who made you":
        return "I was created by humans."
    
    elif user_input == "help":
        return "You can say: hello, how are you, time, thanks, or bye."
    
    elif user_input == "thanks":
        return "You're welcome!"
    
    elif user_input == "time":
        return "well , this is the good time to chat ."
    
    elif user_input == "bye":
        return "Goodbye! Have a nice day."
    
    else:
        return "Sorry, I don't understand that."

print(" Chatbot started! Type 'bye' to exit.")

while True:
    user = input("You: ")
    response = Jarvis(user)
    print("Bot:", response)

    if user.lower() == "bye":
        break
