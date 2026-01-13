from datetime import datetime

responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "hey": "Hey! How can I help you?",
    "how are you": "I am fine. How about you?",
    "what is your name": "My name is ChatBot.",
    "who are you": "I am a text based chatbot.",
    "what can you do": "I can answer simple questions.",
    "time": lambda: datetime.now().strftime("%H:%M:%S"),
    "date": lambda: datetime.now().strftime("%d-%m-%Y"),
    "thank you": "You are welcome!",
    "thanks": "Glad to help!",
    "bye": "Goodbye! Have a nice day.",
    "exit": "Chat ended."
}

conversation_log = []
last_response = ""

print("ChatBot: Hello! Type 'exit' to stop.")

while True:
    user_input = input("You: ").lower()
    response = "Sorry, I don't understand your question."

    for key in responses:
        if key in user_input:
            if callable(responses[key]):
                response = responses[key]()
            else:
                response = responses[key]
            break

    if response == last_response:
        response = "You already asked that. Please ask something else."

    print("ChatBot:", response)

    conversation_log.append({
        "user": user_input,
        "bot": response,
        "time": datetime.now().strftime("%H:%M:%S")
    })

    last_response = response

    if user_input in ["bye", "exit"]:
        break

print("\nConversation Log:")
for chat in conversation_log:
    print(chat)