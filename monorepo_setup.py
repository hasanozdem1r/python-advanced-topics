import os
import subprocess
from enum import Enum

ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Commands(Enum):
    INSTALL = "install"
    INIT = "init"


# function to run poetry init command in the current directory
def execute_poetry_init() -> None:
    try:
        print("Running poetry init...")
        subprocess.run(["poetry", "init", "--no-interaction"],
                       check=True,
                       text=True,
                       input="\n")
        print("Poetry initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def execute_poetry_install() -> None:
    try:
        print("Running poetry install...")
        subprocess.run(["poetry", "install"], check=True, text=True, input="\n")
        print("Poetry dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def process_over_directories(root_dir: str, command: Commands) -> None:
    """Iterate through subdirectories recursively"""
    for directory in os.listdir(root_dir):
        if directory[0] != '.' and os.path.isdir(
                directory) and directory != "docs":
            print(directory)
            os.chdir(directory)
            if command == 'init':
                print(f"\nInitializing poetry in directory: {directory}")
                execute_poetry_init()
            elif command == 'install':
                print(f"\nRunning poetry install in directory: {directory}")
                execute_poetry_install()
            os.chdir(root_dir)


if __name__ == "__main__":
    process_over_directories(root_dir=ROOT_DIRECTORY,
                             command=Commands.INIT.value)
    # for directory in os.listdir(ROOT_DIRECTORY):
    #     if directory[0] != '.' and os.path.isdir(directory):
    #         print(directory)
