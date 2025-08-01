import argparse
import os
import shutil
from pathlib import Path

#"/Users/garrettlambert/Code Projects/CLI Folder/FileTesting.txt"


    
def copyFile(filePath):
    
    newFile = Path("NewFile.txt")
    newFile.touch()
    shutil.copyfile(filePath, newFile)


def main():

    

    try:
        userInput = input("Please enter filePath: ")
        filePath = Path(userInput)
        contents = filePath.read_text()
        
        if filePath.exists():
            if "Hello" in contents:
                filePath.write_text("Hello wrong")
        else: 
            print("File Path does not exist")
            filePath.touch()

    except FileExistsError as e:
        print(f"Error: {e}")
        userInput = input("Please enter filePath")
        filePath = Path(userInput)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        userInput = input("Please enter filePath")
        filePath = Path(userInput)
    except Exception as e:
        print(f"Error: {e}")
    
    copyFile(filePath)

if __name__ == "__main__":
    main()

 


