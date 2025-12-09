from src.presenter.update_user_viewmodel import UpdateUserViewModel

class UpdateUserPresenter:
    def __init__(self):
        self.viewmodel = None

    def present(self, response):
        self.viewmodel = UpdateUserViewModel(
            updated=response.updated
        )