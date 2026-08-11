intents = {
    "greeting": {
        "hello", "hi", "hey", "salam", "assalam o alaikum"
    },

    "goodbye": {
        "bye", "goodbye", "exit", "quit"
    },

    "name": {
        "what is your name",
        "who are you",
        "tell me your name"
    },

    "how_are_you": {
        "how are you",
        "how are you doing",
        "are you fine"
    },

    "capabilities": {
        "what can you do",
        "help me",
        "what are your features"
    },

    "thanks": {
        "thank you", "thanks", "thankyou"
    },

    "age": {
        "how old are you",
        "what is your age"
    }
}


responses = {
    "greeting": "Hello! How can I help you?",

    "name": "My name is AI Bot. I am a rule-based chatbot.",

    "how_are_you": "I am fine! Thanks for asking.",

    "capabilities": "I can respond to predefined questions and commands.",

    "thanks": "You're welcome! 😊",

    "age": "I don't have an age. I am a computer program.",

    "goodbye": "Goodbye! Have a nice day."
}


print("🤖 AI Bot: Hello! I am your Rule-Based AI Chatbot.")
print("Type 'bye' or 'exit' to stop.\n")


while True:

    user_input = input("You: ")

    user_input = user_input.strip().lower()

    found_intent = False

    for intent, keywords in intents.items():

        if user_input in keywords:

            print("Bot:", responses[intent])

            found_intent = True

            if intent == "goodbye":
                break

            break

    if found_intent and user_input in intents["goodbye"]:
        break

   
    if not found_intent:
        print("Bot: Sorry, I don't understand that.")