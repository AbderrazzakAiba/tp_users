from src.domain.user import User
from src.usecase.save_user_response import SaveUserResponse
from src.usecase.validators import is_valid_email


class SaveUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        # email validation now handled in a single helper
        if not is_valid_email(request.email):
            return SaveUserResponse(False)

        user = User(request.email, request.name)
        self.repo.save(user)
        return SaveUserResponse(True)
