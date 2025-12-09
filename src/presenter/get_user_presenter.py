from src.presenter.get_user_viewmodel import GetUserViewModel

class GetUserPresenter:
    def __init__(self):
        self.viewmodel = None

    def present(self, response):
        if response.found and response.user:
            self.viewmodel = GetUserViewModel(
                found=True,
                email=response.user.email,
                name=response.user.name
            )
        else:
            self.viewmodel = GetUserViewModel(found=False)