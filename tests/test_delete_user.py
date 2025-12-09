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


class DeleteUserPresenterFake:
    def __init__(self):
        self.last_response = None

    def present(self, response):
        self.last_response = response


def test_delete_existing_user():
    repo = InMemoryUserRepositoryFake()
    presenter = DeleteUserPresenterFake()
    usecase = DeleteUserUseCase(repo, presenter)

    repo.save(type('User', (), {'email': 'alex@example.com', 'name': 'Alex'})())

    request = DeleteUserRequest('alex@example.com')

    usecase.execute(request)

    assert presenter.last_response.deleted is True
    assert len(repo.saved) == 0


def test_delete_non_existing_user():
    repo = InMemoryUserRepositoryFake()
    presenter = DeleteUserPresenterFake()
    usecase = DeleteUserUseCase(repo, presenter)

    request = DeleteUserRequest('not_found@example.com')

    usecase.execute(request)

    assert presenter.last_response.deleted is False
    assert len(repo.saved) == 0
