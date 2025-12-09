from src.usecase.delete_user_usecase import DeleteUserUseCase
from src.usecase.delete_user_request import DeleteUserRequest


class InMemoryUserRepositoryFake:
    def __init__(self):
        self.saved = []

    def save(self, user):
        self.saved.append(user)

    def delete_by_email(self, email):
        initial_len = len(self.saved)
        self.saved = [u for u in self.saved if u.email != email]
        return len(self.saved) < initial_len


def test_delete_existing_user():
    repo = InMemoryUserRepositoryFake()
    usecase = DeleteUserUseCase(repo)

    repo.save(type('User', (), {'email': 'alex@example.com', 'name': 'Alex'})())

    request = DeleteUserRequest('alex@example.com')

    response = usecase.execute(request)

    assert response.deleted is True
    assert len(repo.saved) == 0


def test_delete_non_existing_user():
    repo = InMemoryUserRepositoryFake()
    usecase = DeleteUserUseCase(repo)

    request = DeleteUserRequest('not_found@example.com')

    response = usecase.execute(request)

    assert response.deleted is False
    assert len(repo.saved) == 0
