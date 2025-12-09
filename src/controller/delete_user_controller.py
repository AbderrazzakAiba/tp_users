from src.usecase.delete_user_request import DeleteUserRequest

class DeleteUserController:
    def __init__(self, usecase, presenter):
        self.usecase = usecase
        self.presenter = presenter

    def delete(self, email):
        request = DeleteUserRequest(email)
        self.usecase.execute(request)
        return self.presenter.viewmodel
