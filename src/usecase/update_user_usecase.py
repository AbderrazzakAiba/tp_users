from src.usecase.update_user_response import UpdateUserResponse

class UpdateUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        updated = self.repo.update(request.email, request.name)
        return UpdateUserResponse(updated)