from src.usecase.save_user_outputport import SaveUserOutputPort
from src.presenter.save_user_viewmodel import SaveUserViewModel

class SaveUserPresenter(SaveUserOutputPort):
    def __init__(self):
        self.viewmodel = None

    def present(self, response):
        self.viewmodel = SaveUserViewModel(
            success=response.success
        )