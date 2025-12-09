from src.external.repository.inmemory_user_repository import InMemoryUserRepository
from src.usecase.save_user_usecase import SaveUserUseCase
from src.presenter.save_user_presenter import SaveUserPresenter
from src.controller.save_user_controller import SaveUserController

repo = InMemoryUserRepository()
presenter = SaveUserPresenter()
usecase = SaveUserUseCase(repo, presenter)
controller = SaveUserController(usecase, presenter)

vm = controller.save("alex@example.com", "Alex")
print(vm.success)
