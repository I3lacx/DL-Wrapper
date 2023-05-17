"""This file reads the data yaml and displays it"""

import os

import yaml


def print_data():
    """
    This function reads the data yaml and displays it

    Returns:
        None
    """
    # current file's directory
    parent_dir = os.path.dirname(__file__)
    with open(os.path.join(parent_dir, "data", "data.yaml"), "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        print(data)
