import random

class Chatbot:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"],
            "farewell": ["Goodbye!", "See you later!", "Take care!"]
        }

    def respond(self, user_input):
        """Generate a response based on user input."""
        if "hello" in user_input.lower():
            return random.choice(self.responses["greeting"])
        elif "bye" in user_input.lower():
            return random.choice(self.responses["farewell"])
        else:
            return "I'm not sure how to respond to that."

if __name__ == "__main__":
    chatbot = Chatbot()
    user_input = "Hello, chatbot!"
    response = chatbot.respond(user_input)
    print("Chatbot Response:", response)
