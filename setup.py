from setuptools import find_packages, setup

setup(
    name="uam",
    version="0.1",
    description="Template for a Python package",
    author="UAM",
    author_email="harisankar.babu@ivi.fraunhofer.de",
    keywords="python",
    license="MIT",
    url="https://gitlab-extern.ivi.fraunhofer.de/uam/template-project",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Researchers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    packages=find_packages(),
    package_data={
        "uam": ["core/data/*.yaml"],
    },
    install_requires=[
        "numpy>=1.23.2",
        "PyYAML",
        "types-PyYAML",
    ],
    extras_require={
        "dev": [
            "pytest",
            "coverage",
            "pylint",
            "mypy",
            "isort",
            "black",
            "tox",
            "sphinx",
            "sphinx_rtd_theme",
        ],
    },
    python_requires=">=3.8",
)
