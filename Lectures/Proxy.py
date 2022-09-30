from abc import ABC, abstractmethod


class Request(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class RealRequest(Request):
    def request(self) -> None:
        print("RealRequest: Handling request.")


class Proxy(Request):
    def __init__(self, real_request) -> None:
        self._real_request = real_request

    def request(self) -> None:
        self._real_request.request()

        
        self.log_access()

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")


def client_code(subject) -> None:
    subject.request()



if __name__ == "__main__":
    proxy = Proxy(RealRequest())
    client_code(proxy)