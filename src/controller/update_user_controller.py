from src.usecase.update_user_request import UpdateUserRequest

class UpdateUserController:
    def __init__(self, usecase, presenter):
        self.usecase = usecase
        self.presenter = presenter

    def update(self, email, name):
        request = UpdateUserRequest(email, name)
        self.usecase.execute(request)
        return self.presenter.viewmodel
