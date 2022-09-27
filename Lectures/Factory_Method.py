from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def create(self):
        pass

    def send_messages(self) -> str:
        product = self.create()
        result = product.sending()
        return result


class SendingMessages(ABC):
    @abstractmethod
    def sending(self) -> str:
        pass


class CreatorPush(Creator):
    def create(self) -> SendingMessages:
        return SendingPushMessages()


class CreatorSMS(Creator):
    def create(self) -> SendingMessages:
        return SendingSMSMessages()


class SendingPushMessages(SendingMessages):
    def sending(self) -> str:
        return "Выполнена Push рассылка"


class SendingSMSMessages(SendingMessages):
    def sending(self) -> str:
        return "Выполнена SMS рассылка"


def client_code(creator: Creator) -> None:
    print(f"Мы ничего не знаем про код создателя, который работает")
    result = creator.send_messages()
    print(f"Результат: {result}")


if __name__ == "__main__":
    print("Приложение выполняет Push рассылки.")
    client_code(CreatorPush())
    print("\n")

    print("Приложение выполняет SMS рассылки")
    client_code(CreatorSMS())