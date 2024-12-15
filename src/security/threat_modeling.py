class ThreatModeling:
    def __init__(self):
        self.threats = []

    def add_threat(self, threat_name, description):
        """Add a threat to the threat model."""
        self.threats.append({'name': threat_name, 'description': description})
        print(f"Threat added: {threat_name}")

    def analyze_threats(self):
        """Analyze and display the threats."""
        print("Threat Analysis Report:")
        for threat in self.threats:
            print(f"- {threat['name']}: {threat['description']}")

if __name__ == "__main__":
    threat_model = ThreatModeling()
    threat_model.add_threat("Eavesdropping", "Unauthorized interception of communication.")
    threat_model.add_threat("Denial of Service", "Attacks aimed at disrupting service availability.")
    threat_model.analyze_threats()
