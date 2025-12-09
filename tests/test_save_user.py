from src.usecase.save_user_usecase import SaveUserUseCase
from src.usecase.save_user_request import SaveUserRequest


class InMemoryUserRepositoryFake:
    def __init__(self):
        self.saved = []

    def save(self, user):
        self.saved.append(user)

    # added as requested
    def exists_by_email(self, email) -> bool:
        return any(u.email == email for u in self.saved)


def test_saves_user():
    repo = InMemoryUserRepositoryFake()
    usecase = SaveUserUseCase(repo)

    request = SaveUserRequest("alex@example.com", "Alex")

    response = usecase.execute(request)

    assert response.success is True
    assert len(repo.saved) == 1


def test_fails_when_email_is_empty():
    repo = InMemoryUserRepositoryFake()
    usecase = SaveUserUseCase(repo)

    request = SaveUserRequest("", "Alex")

    response = usecase.execute(request)

    assert response.success is False
    assert len(repo.saved) == 0


def test_fails_when_email_not_valid_format():
    repo = InMemoryUserRepositoryFake()
    usecase = SaveUserUseCase(repo)

    request = SaveUserRequest("not-email", "Alex")

    response = usecase.execute(request)

    assert response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_is_empty():
    repo = InMemoryUserRepositoryFake()
    usecase = SaveUserUseCase(repo)

    request = SaveUserRequest("alex@example.com", "")

    response = usecase.execute(request)

    assert response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_is_too_short():
    repo = InMemoryUserRepositoryFake()
    usecase = SaveUserUseCase(repo)

    request = SaveUserRequest("alex@example.com", "A")  # length = 1

    response = usecase.execute(request)

    assert response.success is False
    assert len(repo.saved) == 0


def test_fails_when_name_contains_digits():
    repo = InMemoryUserRepositoryFake()
    usecase = SaveUserUseCase(repo)

    request = SaveUserRequest("alex@example.com", "Al3x")  # contains number

    response = usecase.execute(request)

    assert response.success is False
    assert len(repo.saved) == 0


def test_fails_when_email_already_exists():
    repo = InMemoryUserRepositoryFake()
    usecase = SaveUserUseCase(repo)

    # save user first
    request1 = SaveUserRequest("alex@example.com", "Alex")
    usecase.execute(request1)

    # try to save again
    request2 = SaveUserRequest("alex@example.com", "Alex")
    response = usecase.execute(request2)

    assert response.success is False
    # still only one saved user
    assert len(repo.saved) == 1
