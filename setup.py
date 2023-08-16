from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='tictactoecli',
    version='1.0.0',
    description='A simple Tic-Tac-Toe game in command-line.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erenoguzyesil/tictactoecli',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tictactoe=tictactoecli:play']
    }
)
