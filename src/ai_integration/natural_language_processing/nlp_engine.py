import spacy

class NLPEngine:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_text(self, text):
        """Process the input text and return the parsed document."""
        doc = self.nlp(text)
        return doc

if __name__ == "__main__":
    nlp_engine = NLPEngine()
    text = "Hello, how can I assist you today?"
    processed_doc = nlp_engine.process_text(text)
    print("Processed Text:", [(token.text, token.pos_) for token in processed_doc])
