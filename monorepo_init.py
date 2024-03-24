import os
import subprocess

ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


# function to run poetry init command in the current directory
def run_poetry_init():
    try:
        print("Running poetry init...")
        subprocess.run(["poetry", "init", "--no-interaction"],
                       check=True,
                       text=True,
                       input="\n")
        print("Poetry initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def run_poetry_install():
    try:
        print("Running poetry install...")
        subprocess.run(["poetry", "install"], check=True, text=True, input="\n")
        print("Poetry dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def process_directories(root_dir: str, command: str):
    """Iterate through subdirectories recursively"""
    for directory in os.listdir(root_dir):
        if directory[0] != '.' and os.path.isdir(directory):
            print(directory)
            os.chdir(directory)
            if command == 'init':
                print(f"\nInitializing poetry in directory: {directory}")
                run_poetry_init()
            elif command == 'install':
                print(f"\nRunning poetry install in directory: {directory}")
                run_poetry_install()
            os.chdir(root_dir)


if __name__ == "__main__":
    process_directories(root_dir=ROOT_DIRECTORY, command='install')
