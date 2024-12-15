class KnowledgeGraph:
    def __init__(self):
        self.graph = {}

    def add_relationship(self, subject, predicate, obj):
        """Add a relationship to the knowledge graph."""
        if subject not in self.graph:
            self.graph[subject] = {}
        if predicate not in self.graph[subject]:
            self.graph[subject][predicate] = []
        self.graph[subject][predicate].append(obj)

    def query_relationship(self, subject, predicate):
        """Query relationships from the knowledge graph."""
        return self.graph.get(subject, {}).get(predicate, [])

if __name__ == "__main__":
    knowledge_graph = KnowledgeGraph()
    knowledge_graph.add_relationship("Alice", "knows", "Bob")
    relationships = knowledge_graph.query_relationship("Alice", "knows")
    print("Relationships:", relationships)
