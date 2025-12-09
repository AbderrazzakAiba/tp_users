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


def make_usecase():
    repo = InMemoryUserRepositoryFake()
    presenter = DeleteUserPresenterFake()
    usecase = DeleteUserUseCase(repo, presenter)
    return usecase, repo, presenter


def make_request(email="alex@example.com"):
    return DeleteUserRequest(email)


def make_user(email="alex@example.com", name="Alex"):
    return type('User', (), {'email': email, 'name': name})()


def test_delete_existing_user():
    usecase, repo, presenter = make_usecase()
    repo.save(make_user())

    usecase.execute(make_request())

    assert presenter.last_response.deleted is True
    assert len(repo.saved) == 0


def test_delete_non_existing_user():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_request("not_found@example.com"))

    assert presenter.last_response.deleted is False
    assert len(repo.saved) == 0
