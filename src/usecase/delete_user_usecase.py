from src.usecase.delete_user_response import DeleteUserResponse

class DeleteUserUseCase:
    def __init__(self, repo, output):
        self.repo = repo
        self.output = output

    def execute(self, request):
        deleted = self._delete_user(request.email)
        response = DeleteUserResponse(deleted)
        self.output.present(response)

    def _delete_user(self, email):
        return self.repo.delete_by_email(email)
