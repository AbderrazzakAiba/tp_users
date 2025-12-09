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


class UpdateUserPresenterFake:
    def __init__(self):
        self.last_response = None

    def present(self, response):
        self.last_response = response


def test_update_existing_user():
    repo = InMemoryUserRepositoryFake()
    presenter = UpdateUserPresenterFake()
    usecase = UpdateUserUseCase(repo, presenter)

    repo.save(type('User', (), {'email': 'alex@example.com', 'name': 'Alex'})())

    request = UpdateUserRequest('alex@example.com', 'Alicia')

    usecase.execute(request)

    assert presenter.last_response.updated is True
    assert repo.saved[0].name == 'Alicia'


def test_update_non_existing_user():
    repo = InMemoryUserRepositoryFake()
    presenter = UpdateUserPresenterFake()
    usecase = UpdateUserUseCase(repo, presenter)

    request = UpdateUserRequest('not_found@example.com', 'Someone')

    usecase.execute(request)

    assert presenter.last_response.updated is False
    assert len(repo.saved) == 0


def test_update_user_with_invalid_name():
    repo = InMemoryUserRepositoryFake()
    presenter = UpdateUserPresenterFake()
    repo.save(type('User', (), {'email': 'alex@example.com', 'name': 'Alex'})())

    usecase = UpdateUserUseCase(repo, presenter)

    request = UpdateUserRequest('alex@example.com', 'A')

    usecase.execute(request)

    assert presenter.last_response.updated is False
    assert repo.saved[0].name == 'Alex'
