from typing import Protocol

class SaveUserInputPort(Protocol):
    def execute(self, request):
        pass

class GetUserInputPort(Protocol):
    def execute(self, request):
        pass

class DeleteUserInputPort(Protocol):
    def execute(self, request):
        pass

class UpdateUserInputPort(Protocol):
    def execute(self, request):
        pass

class SaveUserOutputPort(Protocol):
    def present(self, response):
        pass

class GetUserOutputPort(Protocol):
    def present(self, response):
        pass

class DeleteUserOutputPort(Protocol):
    def present(self, response):
        pass

class UpdateUserOutputPort(Protocol):
    def present(self, response):
        pass
