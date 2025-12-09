from src.usecase.delete_user_response import DeleteUserResponse

class DeleteUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        self.repo.delete_by_email(request.email)
        return DeleteUserResponse(True)
