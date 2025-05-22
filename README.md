# Minecraft Relative Coordinates Calculator
EN [RU](READMES/README-ru.md) 
## About the project
This project was written by me for myself, when I got tired of calculating relative coordinates for command block.

## Installation

Download the latest version from the [releases page.](https://github.com/OtlichnikTop/minecraft-relative-coordinates-calcualtor/releases)

To access from anywhere in Linux, move the file to `~/.local/bin/`.

## Usage
1. Enter the coordinates of the command block or any coordinates where the command will be executed in the `X`, `Y` and `Z` fields, in the `Координаты исполнителя` section, respectively.
2. Enter the coordinates of the block on which the command will be executed in the `X`, `Y` and `Z` fields, in the `Координаты блока` section, respectively.
3. Click the `Посчитать` button
4. A pop-up window with the relative coordinates for the command block will appear

## Building from source code
### Dependencies
The project requires [Python](https://www.python.org/) 3.10 and above.

Also, you need to install the [PyQt6](https://pypi.org/project/PyQt6/) library
```bash
pip install PyQt6
```
and [Pyinstaller](https://pypi.org/project/pyinstaller/) for "compiling" the code. It is not mandatory, but it's recommended.
```bash
pip install pyinstaller
```
### Installation and compilation
1. Clone the repository
2. Go to the project directory and run the command
```bash
pyinstaller -F -w main.py
```
3. The executable file should be created in `<project directory>/dist/>`

### Possible errors
#### When installing with pip, an error `error: externally-managed-environment` occurs.
To fix the error, run the following commands in the project directory `python -m venv .venv` and `source .venv/bin/activate` and then try to install the libraries again.

