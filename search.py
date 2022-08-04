import os
import time
import shutil
import random

startingPath = input("Starting directory: ")
endingPath = input("Ending directory: ")
fileExtension = input("Substring to search for (if you want to add more substrings, divide them by ',', something like '.png,.jpg') (not case sensitive): ").split(",")
foundedFiles = []
fileCounter = 0
copiedFilesCounter = 0

if os.path.isdir(startingPath):
    if os.path.isdir(endingPath): #no and because i wanted to make an error message more specific
        for path, subdirs, files in os.walk(startingPath):
            for name in files:
                for fileExt in fileExtension:
                    if fileExt.lower() in name.lower():
                        fileCounter += 1
                        foundedFiles.append(name)
                        fileCount = len(list(set(foundedFiles)))
                        print(f"{fileCount} files has been found already.")

        fileCounter = int(len(list(set(foundedFiles))))
        if len(fileExtension) == 1:
            print(f"{fileCounter} files found with a substring {fileExtension}.")
        if len(fileExtension) >= 2:
            print(f"{fileCounter} files found with substrings {fileExtension}.")

        print("Copying will start in 3 seconds.")
        time.sleep(3)

        for path, subdirs, files in os.walk(startingPath):
            for name in files:
                for fileExt in fileExtension:
                    if fileExt.lower() in name.lower() and not name in os.listdir(endingPath):
                        try:
                            shutil.copy(path + "/" + name, endingPath)
                            copiedFilesCounter += 1
                            
                            if not copiedFilesCounter > fileCounter: 
                                print(f"{copiedFilesCounter}/{fileCounter} files transfered. Transfered file's name: {name}")
                        except shutil.SameFileError:
                            randomNum = str(random.randint(0, 999999999))
                            shutil.copy(path + "/" + name + randomNum, endingPath)
                            copiedFilesCounter += 1

                            if not copiedFilesCounter > fileCounter: 
                                print(f"{copiedFilesCounter}/{fileCounter} files transfered. Transfered file's name: {name + randomNum}")

        if copiedFilesCounter == 0 and fileCounter != 0:
            print("No files were copied because they were already in the ending folder.")
        if fileCounter == 0:
            print(f"No files were copied because no file's name has the substring {fileExtension} in it.")
        if copiedFilesCounter != fileCounter:
            print(f"Successfully copied {copiedFilesCounter} files!\nNot all files were copied because some were in the directory already.")
        else:
            print(f"Successfully copied {copiedFilesCounter} files!")
    else:
        print(f"Invalid path {endingPath}")
else:
    print(f"Invalid path {startingPath}")
