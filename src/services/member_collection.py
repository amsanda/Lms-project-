# ADT for managing multiple library members
class MemberCollection:
    """ADT for managing a collection of library members."""

    # Constructor to initialize internal dictionary
    def __init__(self):
        self._members = {}  # Private dict: member_id -> Member object

    # Method to add a new member
    def add_member(self, member):
        if member.member_id in self._members:
            raise ValueError(f"Member {member.member_id} already exists")
        self._members[member.member_id] = member

    # Method to remove a member
    def remove_member(self, member_id):
        member = self._members[member_id]
        if member.get_borrowed_books():
            raise ValueError("Cannot remove member with borrowed books")
        del self._members[member_id]

    # Method to find a member by their ID
    def find_by_id(self, member_id):
        return self._members.get(member_id)

    # Method to find members by partial name match
    def find_by_name(self, name_substring):
        results = []
        for member in self._members.values():
            if name_substring.lower() in member.name.lower():
                results.append(member)
        return results

    # Return all members as a list
    def get_all_members(self):
        return list(self._members.values())

    # Return the count of members
    def count(self):
        return len(self._members)