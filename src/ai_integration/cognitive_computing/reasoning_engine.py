class ReasoningEngine:
    def __init__(self):
        self.knowledge_base = {}

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.knowledge_base[fact] = True

    def query_fact(self, fact):
        """Query a fact from the knowledge base."""
        return self.knowledge_base.get(fact, False)

if __name__ == "__main__":
    reasoning_engine = ReasoningEngine()
    reasoning_engine.add_fact("The sky is blue.")
    result = reasoning_engine.query_fact("The sky is blue.")
    print("Fact Query Result:", result)
