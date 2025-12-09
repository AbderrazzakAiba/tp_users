from src.usecase.get_user_usecase import GetUserUseCase
from src.usecase.get_user_request import GetUserRequest


class InMemoryUserRepositoryFake:
    def __init__(self):
        self.saved = []

    def save(self, user):
        self.saved.append(user)

    def find_by_email(self, email):
        for u in self.saved:
            if u.email == email:
                return u
        return None


class GetUserPresenterFake:
    def __init__(self):
        self.last_response = None

    def present(self, response):
        self.last_response = response


def test_get_existing_user():
    repo = InMemoryUserRepositoryFake()
    presenter = GetUserPresenterFake()
    usecase = GetUserUseCase(repo, presenter)

    repo.save(type('User', (), {'email': 'alex@example.com', 'name': 'Alex'})())

    request = GetUserRequest('alex@example.com')

    usecase.execute(request)

    assert presenter.last_response.found is True
    assert presenter.last_response.user.email == 'alex@example.com'


def test_get_non_existing_user():
    repo = InMemoryUserRepositoryFake()
    presenter = GetUserPresenterFake()
    usecase = GetUserUseCase(repo, presenter)

    request = GetUserRequest('not_found@example.com')

    usecase.execute(request)

    assert presenter.last_response.found is False
    assert presenter.last_response.user is None
