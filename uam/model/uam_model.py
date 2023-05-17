"""This file contains the abstract model class"""

from abc import ABC, abstractmethod

import torch


class ModelABC(ABC):
    """This class represents an abstract model"""

    @abstractmethod
    def __call__(self, x):
        """This method preprocesses, runs and postprocesses the input"""

    @abstractmethod
    def preprocess(self, x):
        """This method preprocesses the input"""

    @abstractmethod
    def postprocess(self, x):
        """This method postprocesses the output"""

    @abstractmethod
    def infer(self, x):
        """This method runs the model on the input"""

    @abstractmethod
    def load(self, path):
        """This method loads the model"""


class UAMModel(ModelABC):
    """This class represents the UAM model"""

    def __init__(self, model, preprocessor, postprocessor):
        self.model = model
        self.preprocessor = preprocessor
        self.postprocessor = postprocessor

    def __call__(self, x):
        x = self.preprocess(x)
        x = self.infer(x)
        x = self.postprocess(x)
        return x

    def preprocess(self, x):
        return self.preprocessor(x)

    def postprocess(self, x):
        return self.postprocessor(x)

    @torch.no_grad()
    def infer(self, x):
        return self.model(x)

    def load(self, path):
        self.model.load(path)

    def eval(self):
        self.model.eval()

    def train(self):
        self.model.train()

    def to(self, device):
        self.model.to(device)
