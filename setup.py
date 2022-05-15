# Import required functions
from setuptools import setup, find_packages

# pip install -e .           ---->        to install the package

# Call setup function
setup(
    author="Allison Eduardo",
    description="Directory Architecture",
    name="da",
    version="0.1.0",
    packages=find_packages(include=["da", "da.*"])
)
