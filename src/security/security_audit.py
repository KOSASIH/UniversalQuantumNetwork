class SecurityAudit:
    def __init__(self):
        self.audit_logs = []

    def log_event(self, event):
        """Log a security event."""
        self.audit_logs.append(event)
        print(f"Event logged: {event}")

    def generate_report(self):
        """Generate a security audit report."""
        print("Security Audit Report:")
        for log in self.audit_logs:
            print(f"- {log}")

if __name__ == "__main__":
    audit = SecurityAudit()
    audit.log_event("User  login attempt.")
    audit.log_event("File access by user.")
    audit.generate_report()
