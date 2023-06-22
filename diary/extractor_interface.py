from abc import ABC, abstractmethod

class IExtractor(ABC):

    @staticmethod
    @abstractmethod
    def verify_today_diary() -> bool:
        pass

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass