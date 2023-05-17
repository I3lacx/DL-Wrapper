"""This file contains the simple model class"""

from dataclasses import dataclass

import torch


@dataclass
class SimpleModel:
    """This class represents a simple model"""

    model: torch.nn.Module
    optimizer: torch.optim.Optimizer
    loss_fn: torch.nn.Module = torch.nn.CrossEntropyLoss()
    device: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    train_loader: torch.utils.data.DataLoader = None
    val_loader: torch.utils.data.DataLoader = None

    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        """This method runs the model on the input"""
        return self.model(x)

    def train(self) -> None:
        """This method trains the model"""
        self.model.train()
        for _, (data, target) in enumerate(self.train_loader):
            data, target = data.to(self.device), target.to(self.device)
            self.optimizer.zero_grad()
            output = self.model(data)
            loss = self.loss_fn(output, target)
            loss.backward()
            self.optimizer.step(closure=None)

    def validate(self) -> None:
        """This method validates the model"""
        self.model.eval()
        test_loss = 0.0
        with torch.no_grad():
            for data, target in self.val_loader:
                data, target = data.to(self.device), target.to(self.device)
                output = self.model(data)
                test_loss += self.loss_fn(output, target, reduction="sum").item()

        test_loss /= len(self.val_loader.dataset)

        print(f"\nTest set: Average loss: {test_loss:.4f}\n")

    def save(self, path: str) -> None:
        """This method saves the model"""
        torch.save(self.model.state_dict(), path)
        torch.save(self.optimizer.state_dict(), path + ".optimizer")

    def load(self, path: str) -> None:
        """This method loads the model"""
        self.model.load_state_dict(torch.load(path))
        self.optimizer.load_state_dict(torch.load(path + ".optimizer"))
