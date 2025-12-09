from src.domain.user import User
from src.usecase.save_user_response import SaveUserResponse

class SaveUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        if not request.email:
            return SaveUserResponse(False)

        # minimal validation for email format
        if "@" not in request.email:
            return SaveUserResponse(False)

        user = User(request.email, request.name)
        self.repo.save(user)
        return SaveUserResponse(True)

