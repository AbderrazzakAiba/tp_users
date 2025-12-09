from src.usecase.save_user_usecase import SaveUserUseCase
from src.usecase.save_user_request import SaveUserRequest


class InMemoryUserRepositoryFake:
    def __init__(self):
        self.saved = []

    def save(self, user):
        self.saved.append(user)


def test_saves_user():
    repo = InMemoryUserRepositoryFake()
    usecase = SaveUserUseCase(repo)

    request = SaveUserRequest("alex@example.com", "Alex")

    response = usecase.execute(request)

    assert response.success is True
    assert len(repo.saved) == 1
