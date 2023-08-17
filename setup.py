from setuptools import setup, find_packages

long_description = """# tictaccli
A simple command-line Tic-Tac-Toe game played against the computer.

## Usage

Run the command below in Terminal:

```
tictactoe
```
"""

setup(
    name='tictaccli',
    version='1.0.0.1',
    description='A simple Tic-Tac-Toe game in command-line.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='cli game tictactoe commandline',
    url='https://github.com/erenoguzyesil/tictactoecli',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tictactoe=tictactoecli:play']
    }
)
