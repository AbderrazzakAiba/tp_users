from src.usecase.delete_user_response import DeleteUserResponse

class DeleteUserUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        deleted = self._delete_user(request.email)
        return DeleteUserResponse(deleted)

    def _delete_user(self, email):
        return self.repo.delete_by_email(email)
