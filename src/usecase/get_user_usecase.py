from src.usecase.get_user_response import GetUserResponse

class GetUserUseCase:
    def __init__(self, repo, output):
        self.repo = repo
        self.output = output

    def execute(self, request):
        user = self._find_user(request.email)
        if user:
            response = GetUserResponse(True, user)
            self.output.present(response)
            return

        response = GetUserResponse(False, None)
        self.output.present(response)

    def _find_user(self, email):
        return self.repo.find_by_email(email)
