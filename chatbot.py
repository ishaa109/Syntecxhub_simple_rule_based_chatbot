import datetime

# Knowledge Base
knowledge_base = {
    "what is cybersecurity": "Cybersecurity is the practice of protecting systems, networks, and data from cyber threats.",
    "what is python": "Python is a high-level programming language used for web development, AI, automation, and more.",
    "what is ai": "Artificial Intelligence enables machines to simulate human intelligence."
}

# Conversation Log
chat_history = []

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting Intent
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"

    # Help Intent
    elif "help" in user_input:
        return "I can answer basic questions about Cybersecurity, Python, and AI."

    # Small Talk Intent
    elif "how are you" in user_input:
        return "I am doing great. Thanks for asking!"

    elif "your name" in user_input:
        return "I am a Rule-Based Chatbot."

    # Knowledge Base Search
    elif user_input in knowledge_base:
        return knowledge_base[user_input]

    # Exit
    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that question."

print("=== Rule-Based Chatbot ===")
print("Type 'bye' to exit.")

while True:
    user = input("You: ")

    response = chatbot_response(user)
    print("Bot:", response)

    timestamp = datetime.datetime.now()
    chat_history.append(f"{timestamp} | User: {user} | Bot: {response}")

    if user.lower() == "bye":
        break

# Save Conversation History
with open("chat_history.txt", "w") as file:
    for entry in chat_history:
        file.write(entry + "\n")

print("Conversation saved to chat_history.txt")