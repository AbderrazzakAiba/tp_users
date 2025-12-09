class GetUserViewModel:
    def __init__(self, found, email=None, name=None):
        self.found = found
        self.email = email
        self.name = name