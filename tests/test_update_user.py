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


def make_usecase():
    repo = InMemoryUserRepositoryFake()
    presenter = UpdateUserPresenterFake()
    usecase = UpdateUserUseCase(repo, presenter)
    return usecase, repo, presenter


def make_request(email="alex@example.com", name="Alex Updated"):
    return UpdateUserRequest(email, name)


def make_user(email="alex@example.com", name="Alex"):
    return type('User', (), {'email': email, 'name': name})()


def test_update_existing_user():
    usecase, repo, presenter = make_usecase()
    repo.save(make_user())

    usecase.execute(make_request(name="Alicia"))

    assert presenter.last_response.updated is True
    assert repo.saved[0].name == "Alicia"


def test_update_non_existing_user():
    usecase, repo, presenter = make_usecase()

    usecase.execute(make_request(email="not_found@example.com", name="Someone"))

    assert presenter.last_response.updated is False
    assert len(repo.saved) == 0


def test_update_user_with_invalid_name():
    usecase, repo, presenter = make_usecase()
    repo.save(make_user())

    usecase.execute(make_request(name="A"))

    assert presenter.last_response.updated is False
    assert repo.saved[0].name == "Alex"
