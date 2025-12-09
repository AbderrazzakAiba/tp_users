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


def test_get_existing_user():
    repo = InMemoryUserRepositoryFake()
    usecase = GetUserUseCase(repo)

    repo.save(type('User', (), {'email': 'alex@example.com', 'name': 'Alex'})())

    request = GetUserRequest('alex@example.com')

    response = usecase.execute(request)

    assert response.found is True
    assert response.user.email == 'alex@example.com'

def test_get_non_existing_user():
    repo = InMemoryUserRepositoryFake()
    usecase = GetUserUseCase(repo)

    request = GetUserRequest('not_found@example.com')

    response = usecase.execute(request)

    assert response.found is False
    assert response.user is None
