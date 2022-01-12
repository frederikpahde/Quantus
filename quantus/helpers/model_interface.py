from abc import ABC, abstractmethod


class ModelInterface(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def predict(self, x_input):
        raise NotImplementedError

    @abstractmethod
    def shape_input(self, x):
        raise NotImplementedError

    @abstractmethod
    def get_model(self):
        raise NotImplementedError

    @abstractmethod
    def state_dict(self):
        raise NotImplementedError

    @abstractmethod
    def load_state_dict(self, original_parameters):
        raise NotImplementedError

    @abstractmethod
    def get_layers(self, order):
        raise NotImplementedError
