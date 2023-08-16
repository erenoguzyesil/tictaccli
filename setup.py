from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='tictactoecli_test_J',
    version='1.0.0',
    description='A simple Tic-Tac-Toe game in command-line.',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tictactoe=tictactoecli:play']
    }
)
