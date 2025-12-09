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


def make_usecase():
    repo = InMemoryUserRepositoryFake()
    presenter = SaveUserPresenterFake()
    usecase = SaveUserUseCase(repo, presenter)
    return usecase, repo, presenter


def make_user(email="alex@example.com", name="Alex"):
    return SaveUserRequest(email, name)


def test_saves_user():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_user())

    assert presenter.last_response.success is True
    assert len(repo.saved) == 1


def test_fails_when_email_is_empty():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_user(email=""))

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_email_not_valid_format():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_user(email="not-email"))

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_is_empty():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_user(name=""))

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_is_too_short():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_user(name="A"))

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_contains_digits():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_user(name="Al3x"))

    assert presenter.last_response.success is False
    assert len(repo.saved) == 0


def test_fails_when_email_already_exists():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_user())
    usecase.execute(make_user())

    assert presenter.last_response.success is False
    assert len(repo.saved) == 1
