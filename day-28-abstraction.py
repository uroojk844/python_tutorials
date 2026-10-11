from typing import Literal


class Bank:
    def __init__(self, name: str, ifsc: str) -> None:
        self.__name = name
        self.__ifsc = ifsc

    def getName(self):
        return self.__name

    def getIfsc(self):
        return self.__ifsc

    def details(self):
        print(f"Bank: {self.__name}")
        print(f"IFSC: {self.__ifsc}")


class Account(Bank):
    def __init__(
        self, bankname: str, ifsc: str, type: Literal["saving", "current"], name: str
    ) -> None:
        super().__init__(bankname, ifsc)
        self.type = type
        self.name = name
        self.__balance = 0

    def __str__(self) -> str:
        return f"""
Bank: {self.getName()}
IFSC: {self.getIfsc()}
Name: {self.name}
Balance: {self.__balance}
"""


a1 = Account("ICICI", "ICI012345", "saving", "CompileRoot")
print(a1)
