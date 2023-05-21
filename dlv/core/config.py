# ChatGPT?

# Write an abstract config class that can load and save from yaml
# it has a function that validates the configuration
# that pretty prints the configuration


from typing import Annotated

# A config class subscribing to that abstract config class should
# specify all default parameters and document those
from dlv.core.abstract_config import AbstractConfig


class Train(AbstractConfig):
    """Parameters for the World configuration"""

    learning_rate: int = 1
    """ Learning rate docstring """

    training_episodes: int = 1
    """ training episodes docstring """

    use_early_stopping: bool = True
    """ Using early stopping """

    use_lstm: bool = False
    """ Using lstm """

    def __init__(self, params):
        super().__init__(params)
