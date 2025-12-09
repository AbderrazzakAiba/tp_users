from src.usecase.save_user_request import SaveUserRequest

class SaveUserController:
    def __init__(self, usecase, presenter):
        self.usecase = usecase
        self.presenter = presenter

    def save(self, email, name):
        request = SaveUserRequest(email, name)
        self.usecase.execute(request)
        return self.presenter.viewmodel
