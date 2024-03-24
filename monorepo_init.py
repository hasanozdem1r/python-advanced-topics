import os
import subprocess


# Function to run poetry init command in the current directory
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


# Function to iterate through subdirectories recursively
def process_directories(root_dir):
    for directory in os.listdir(root_dir):
        if directory[0] != '.' and os.path.isdir(directory):
            print(directory)
            os.chdir(directory)
            print(f"\nInitializing poetry in directory: {directory}")
            run_poetry_init()
            os.chdir(root_dir)


# Starting point
if __name__ == "__main__":
    root_directory = "/d/works/python/python_advanced_topics"
    process_directories(root_directory)
