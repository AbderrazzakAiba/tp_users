from src.usecase.save_user_usecase import SaveUserUseCase
from src.usecase.save_user_request import SaveUserRequest


class InMemoryUserRepositoryFake:
    def __init__(self):
        self.saved = []

    def save(self, user):
        self.saved.append(user)

    def exists_by_email(self, email) -> bool:
        return any(u.email == email for u in self.saved)


class SaveUserPresenterFake:
    def __init__(self):
        self.last_response = None

    def present(self, response):
        self.last_response = response


def test_saves_user():
    repo = InMemoryUserRepositoryFake()
    presenter = SaveUserPresenterFake()
    usecase = SaveUserUseCase(repo, presenter)

    request = SaveUserRequest("alex@example.com", "Alex")

    usecase.execute(request)

    assert presenter.last_response.success is True
    assert len(repo.saved) == 1


def test_fails_when_email_is_empty():
    repo = InMemoryUserRepositoryFake()
    presenter = SaveUserPresenterFake()
    usecase = SaveUserUseCase(repo, presenter)

    request = SaveUserRequest("", "Alex")

    usecase.execute(request)

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_email_not_valid_format():
    repo = InMemoryUserRepositoryFake()
    presenter = SaveUserPresenterFake()
    usecase = SaveUserUseCase(repo, presenter)

    request = SaveUserRequest("not-email", "Alex")

    usecase.execute(request)

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_is_empty():
    repo = InMemoryUserRepositoryFake()
    presenter = SaveUserPresenterFake()
    usecase = SaveUserUseCase(repo, presenter)

    request = SaveUserRequest("alex@example.com", "")

    usecase.execute(request)

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_is_too_short():
    repo = InMemoryUserRepositoryFake()
    presenter = SaveUserPresenterFake()
    usecase = SaveUserUseCase(repo, presenter)

    request = SaveUserRequest("alex@example.com", "A")

    usecase.execute(request)

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_contains_digits():
    repo = InMemoryUserRepositoryFake()
    presenter = SaveUserPresenterFake()
    usecase = SaveUserUseCase(repo, presenter)

    request = SaveUserRequest("alex@example.com", "Al3x")

    usecase.execute(request)

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_email_already_exists():
    repo = InMemoryUserRepositoryFake()
    presenter = SaveUserPresenterFake()
    usecase = SaveUserUseCase(repo, presenter)

    request1 = SaveUserRequest("alex@example.com", "Alex")
    usecase.execute(request1)

    request2 = SaveUserRequest("alex@example.com", "Alex")
    usecase.execute(request2)

    assert presenter.last_response.success is False
    assert len(repo.saved) == 1
