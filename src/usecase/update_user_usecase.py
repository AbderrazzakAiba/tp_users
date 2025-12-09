from src.usecase.update_user_response import UpdateUserResponse
from src.usecase.validators import is_valid_name

class UpdateUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        if not is_valid_name(request.name):
            return UpdateUserResponse(False)

        updated = self._update_user(request.email, request.name)
        return UpdateUserResponse(updated)

    def _update_user(self, email, name):
        return self.repo.update(email, name)
