class ErrorHandling:
    def __init__(self):
        self.error_log = []

    def log_error(self, error_message):
        """Log an error message."""
        self.error_log.append(error_message)
        print(f"Error logged: {error_message}")

    def handle_error(self, error_type):
        """Handle different types of errors."""
        if error_type == "quantum_loss":
            self.log_error("Quantum state lost during transmission.")
        elif error_type == "measurement_error":
            self.log_error("Measurement error occurred.")
        else:
            self.log_error("Unknown error type.")

if __name__ == "__main__":
    error_handler = ErrorHandling()
    error_handler.handle_error("quantum_loss")
