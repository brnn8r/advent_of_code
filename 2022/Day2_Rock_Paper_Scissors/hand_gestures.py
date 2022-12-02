from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass


class HandGesture(ABC):
    pass

    @property
    @abstractmethod
    def value(self):
        pass

    @staticmethod
    @abstractmethod
    def beats(gesture: type):
        pass


@dataclass
class Rock(HandGesture):
    @staticmethod
    def beats(gesture: HandGesture):
        return type(gesture) == Scissors

    @property
    def value(self):
        return 1


@dataclass
class Paper(HandGesture):
    @staticmethod
    def beats(gesture: HandGesture):
        return type(gesture) == Rock

    @property
    def value(self):
        return 2


@dataclass
class Scissors(HandGesture):
    @staticmethod
    def beats(gesture: HandGesture):
        return type(gesture) == Paper

    @property
    def value(self):
        return 3
