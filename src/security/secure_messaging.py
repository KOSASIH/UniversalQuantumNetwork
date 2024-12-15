class SecureMessaging:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, message):
        """Send a secure message."""
        secure_message = f"From: {sender}\nTo: {receiver}\nMessage: {message}"
        self.messages.append(secure_message)
        print("Message sent securely.")

    def display_messages(self):
        """Display all sent messages."""
        print("Sent Messages:")
        for msg in self.messages:
            print(msg)

if __name__ == "__main__":
    messaging = SecureMessaging()
    messaging.send_message("Alice", "Bob", "Hello, Bob! This is a secure message.")
    messaging.display_messages()
