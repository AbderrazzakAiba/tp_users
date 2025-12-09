from src.usecase.update_user_usecase import UpdateUserUseCase
from src.usecase.update_user_request import UpdateUserRequest


class InMemoryUserRepositoryFake:
    def __init__(self):
        self.saved = []

    def save(self, user):
        self.saved.append(user)

    def update(self, email, name):
        for user in self.saved:
            if user.email == email:
                user.name = name
                return True
        return False


def test_update_existing_user():
    repo = InMemoryUserRepositoryFake()

    repo.save(type('User', (), {'email': 'alex@example.com', 'name': 'Alex'})())

    usecase = UpdateUserUseCase(repo)

    request = UpdateUserRequest('alex@example.com', 'Alicia')

    response = usecase.execute(request)

    assert response.updated is True
    assert repo.saved[0].name == 'Alicia'

def test_update_non_existing_user():
    repo = InMemoryUserRepositoryFake()
    usecase = UpdateUserUseCase(repo)

    request = UpdateUserRequest('not_found@example.com', 'Someone')

    response = usecase.execute(request)

    assert response.updated is False
    assert len(repo.saved) == 0