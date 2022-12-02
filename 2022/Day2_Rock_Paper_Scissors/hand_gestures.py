from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass


class HandGesture(ABC):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(HandGesture, cls).__new__(cls)
        return cls.instance

    @property
    @abstractmethod
    def value(self):
        pass

    @staticmethod
    @abstractmethod
    def beats():
        pass

    @staticmethod
    @abstractmethod
    def beaten_by():
        pass


@dataclass
class Rock(HandGesture):
    @staticmethod
    def beaten_by():
        return Paper()

    @staticmethod
    def beats():
        return Scissors()

    @property
    def value(self):
        return 1


@dataclass
class Paper(HandGesture):
    @staticmethod
    def beaten_by():
        return Scissors()

    @staticmethod
    def beats():
        return Rock()

    @property
    def value(self):
        return 2


@dataclass
class Scissors(HandGesture):
    @staticmethod
    def beaten_by():
        return Rock()

    @staticmethod
    def beats():
        return Paper()

    @property
    def value(self):
        return 3