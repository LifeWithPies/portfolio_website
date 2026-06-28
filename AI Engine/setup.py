# Estimated Token Consumption: 500
from setuptools import setup, find_packages

setup(
    name='adk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pytest>=7.0.0',
        'typing-extensions>=4.0.0',
    ],
)