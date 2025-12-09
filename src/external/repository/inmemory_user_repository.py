class InMemoryUserRepository:
    def __init__(self):
        self.saved = []

    def save(self, user):
        self.saved.append(user)

    def exists_by_email(self, email):
        return any(u.email == email for u in self.saved)

    def find_by_email(self, email):
        for u in self.saved:
            if u.email == email:
                return u
        return None

    def delete_by_email(self, email):
        initial_len = len(self.saved)
        self.saved = [u for u in self.saved if u.email != email]
        return len(self.saved) < initial_len

    def update(self, email, name):
        for u in self.saved:
            if u.email == email:
                u.name = name
                return True
        return False
