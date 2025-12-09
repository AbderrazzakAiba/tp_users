from src.usecase.get_user_response import GetUserResponse

class GetUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        user = self._find_user(request.email)
        if user:
            return GetUserResponse(True, user)
        return GetUserResponse(False, None)

    def _find_user(self, email):
        return self.repo.find_by_email(email)
