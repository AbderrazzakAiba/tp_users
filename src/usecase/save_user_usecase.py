from src.domain.user import User
from src.usecase.save_user_response import SaveUserResponse
from src.usecase.validators import is_valid_email, is_valid_name


class SaveUserUseCase:
    def __init__(self, repo, output):
        self.repo = repo
        self.output = output

    def execute(self, request):
        if not self._is_valid_request(request):
            response = SaveUserResponse(False)
            self.output.present(response)
            return

        if self._email_exists(request.email):
            response = SaveUserResponse(False)
            self.output.present(response)
            return

        user = User(request.email, request.name)
        self.repo.save(user)
        response = SaveUserResponse(True)
        self.output.present(response)

    def _is_valid_request(self, request):
        if not is_valid_email(request.email):
            return False

        if not is_valid_name(request.name):
            return False

        return True

    def _email_exists(self, email):
        return self.repo.exists_by_email(email)
