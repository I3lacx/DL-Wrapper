from setuptools import find_packages, setup

setup(
    name="dlv",
    version="0.1",
    description="Deep Learning Vrapper",
    author="I3lacx",
    author_email="MaxOtteAI@gmail.com",
    keywords="python",
    license="MIT",
    url="https://github.com/I3lacx/DL-Wrapper",
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
        "dlv": ["core/data/*.yaml"],
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
