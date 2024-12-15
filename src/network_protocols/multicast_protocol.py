class MulticastProtocol:
    def __init__(self):
        self.groups = {}

    def create_group(self, group_name):
        """Create a multicast group."""
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f"Group '{group_name}' created.")

    def join_group(self, group_name, member):
        """Add a member to a multicast group."""
        if group_name in self.groups:
            self.groups[group_name].append(member)
            print(f"{member} joined group '{group_name}'.")

    def send_message(self, group_name, message):
        """Send a message to all members of a multicast group."""
        if group_name in self.groups:
            for member in self.groups[group_name]:
                print(f"Sending message to {member}: {message}")

if __name__ == "__main__":
    multicast = MulticastProtocol()
    multicast.create_group("Group 1")
    multicast.join_group("Group 1", "Alice")
    multicast.join_group("Group 1", "Bob")
    multicast.send_message("Group 1", "Hello, Group 1!")
