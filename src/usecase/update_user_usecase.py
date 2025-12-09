from src.usecase.update_user_response import UpdateUserResponse
from src.usecase.validators import is_valid_name

class UpdateUserUseCase:
    def __init__(self, repo, output):
        self.repo = repo
        self.output = output

    def execute(self, request):
        if not is_valid_name(request.name):
            response = UpdateUserResponse(False)
            self.output.present(response)
            return

        updated = self._update_user(request.email, request.name)
        response = UpdateUserResponse(updated)
        self.output.present(response)

    def _update_user(self, email, name):
        return self.repo.update(email, name)
