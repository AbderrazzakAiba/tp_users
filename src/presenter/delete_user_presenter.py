from src.presenter.delete_user_viewmodel import DeleteUserViewModel

class DeleteUserPresenter:
    def __init__(self):
        self.viewmodel = None

    def present(self, response):
        self.viewmodel = DeleteUserViewModel(
            deleted=response.deleted
        )