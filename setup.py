"""Setup.py file."""

import os

import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


from shortprint.requirements import REQUIREMENTS

setuptools.setup(
    name="shortprint",  # This is the name of the package
    version=os.getenv("RELEASE_NAME", "0.0.2"),  # The initial release version
    author="Marco Boucas",  # Full name of the author
    url="https://github.com/marcoboucas/shortprint",
    description="The module to help you understand your data",
    long_description=long_description,  # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(
        include=["shortprint", "shortprint.*"]
    ),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires=">=3.6",  # Minimum version requirement of the package
    py_modules=["shortprint"],  # Name of the python package
    install_requires=REQUIREMENTS,  # Install other dependencies if any
)
