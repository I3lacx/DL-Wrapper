from abc import ABC, abstractmethod


class AbstractConfig(ABC):
    """Template Class, will be used for each class"""

    def __init__(self, params):
        # Only changes default params if specified in params
        self._overwrite_default_parameters(params)
        self._calculate_undefined_settings()
        self._validate()

    def _overwrite_default_parameters(self, new_params):
        """Sets all parameters to the values specified in configs"""

        for key in new_params.keys():
            # Not needed, but makes sure that all parameters are defined above!
            assert hasattr(self, key), f"Setting: {key}, does not exist in {type(self)}!"
            setattr(self, key, new_params[key])

    def load(self, filename):
        pass

    def save(self, filename):
        pass

    def _validate(self):
        pass

    def _calculate_undefined_settings(self):
        pass
