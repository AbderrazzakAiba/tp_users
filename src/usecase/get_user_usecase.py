from src.usecase.get_user_response import GetUserResponse

class GetUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        user = self.repo.find_by_email(request.email)
        if user:
            return GetUserResponse(True, user)
        return GetUserResponse(False, None)
