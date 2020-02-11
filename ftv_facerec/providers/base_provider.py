import abc
import cv2

class BaseProvider(abc.ABC):
    def __init__(self):
        super().__init__()
    
    @abc.abstractmethod
    def train(self, size):
        pass

    @abc.abstractmethod
    def recognize(self, size):
        pass
