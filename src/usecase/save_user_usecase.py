from src.domain.user import User
from src.usecase.save_user_response import SaveUserResponse
from src.usecase.validators import is_valid_email, is_valid_name


class SaveUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        if not self._is_valid_request(request):
            return SaveUserResponse(False)

        if self._email_exists(request.email):
            return SaveUserResponse(False)

        user = User(request.email, request.name)
        self.repo.save(user)
        return SaveUserResponse(True)

    def _is_valid_request(self, request):
        if not is_valid_email(request.email):
            return False

        if not is_valid_name(request.name):
            return False

        return True

    def _email_exists(self, email):
        if hasattr(self.repo, "exists_by_email"):
            return self.repo.exists_by_email(email)
        return False
