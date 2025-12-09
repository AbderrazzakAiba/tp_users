from src.usecase.get_user_request import GetUserRequest

class GetUserController:
    def __init__(self, usecase, presenter):
        self.usecase = usecase
        self.presenter = presenter

    def get(self, email):
        request = GetUserRequest(email)
        self.usecase.execute(request)
        return self.presenter.viewmodel
