from abc import ABC, abstractmethod


class Abstract_Adressbook(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def add_phone(self, phone):
        pass

    @abstractmethod
    def del_phone(self, phone):
        pass

    @abstractmethod
    def edit_phone(self, phone, new_phone):
        pass

    @abstractmethod
    def add_email(self, email):
        pass

    @abstractmethod
    def del_email(self, email):
        pass

    @abstractmethod
    def days_to_birthday(self, birthday):
        pass


class Abstract_Notebook(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def hyphenation_string(self, text):
        pass
