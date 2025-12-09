import numpy as np
import re

chat_data = {
    r"(hi|hello|hey)": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
    r"(how are you)": ["I'm doing great, thanks!", "All good here. How about you?", "Feeling awesome!"],
    r"(what is your name)": ["I'm a simple chatbot.", "You can call me PyBot!", "I'm your Python friend!"],
    r"(bye|goodbye)": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    r"(what are you doing)":["Nothing,what about you?"],
    r"(can you help me)":["yes! I can"],
    r"(some shopping platforms)":["The shopping platforms are Flipcart,Amazon,Myntra,Ajio,Shopsy,Nykaa------etc "],
    r"(most popular)":["Flipcart and Amazon are most popularly used apps"],
    r"(ok)":["any thing else!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    for pattern, responses in chat_data.items():
        if re.search(pattern, user_input):
            return np.random.choice(responses)  # NumPy random selection
    return "I'm not sure I understand you."

print("Enhanced Python Chatbot. Type 'exit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Thankyou for using this chatbot.Have a nice day")
        break
    print("Chatbot:", chatbot_response(user_input))