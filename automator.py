import argparse
import os
from pathlib import Path
import shutil
import zipfile
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("user")
password = os.getenv("password")




def sendingEmail(textFile, sender, recipient):
    print("testing if github actions works!!!")

    with open(textFile) as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())

    msg["Subject"] = f"The contents of the {textFile}"
    msg["From"] = sender
    msg["To"] = recipient

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(user, password)
    s.send_message(msg)
    s.quit()




def organizeFiles(path):
    if not os.path.isdir(path):
        print(f"The path: {path} is not a valid directory")
        print("test")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext[1:].lower()  # remove the . and lowercase

            if not ext:
                continue

            folder_path = os.path.join(path, ext)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, filename))

    print(f"Files organized in {path} by file extension.")
    


def compressFiles(path):

    if not os.path.isdir(path):
        print(f"The path {path} is not a valid directory")
        return
    print(f"Compressing folder in path: {path}")
    
    newFileExt = ".zip"
    
    with zipfile.ZipFile(f"{path}{newFileExt}", 'w') as myzip:
        myzip.write(path)
    
        

def renameFiles(path, prefix):
    print(f"Renaming files in {path}, with prefix: {prefix}")

    for folder in os.listdir(path):
        os.rename(path, prefix)


def copyFile(fileName):
    
    newFile = Path("NewFile.txt")
    newFile.touch()
    shutil.copyfile(fileName, newFile)

def printUI():

    parser = argparse.ArgumentParser(
            description= "Automation Dashboard CLI"
        )
    subparsers = parser.add_subparsers(dest = "command", help = "Available commands")

    #organizing
    parserOrganize = subparsers.add_parser("organize", help = "Organize files by type")
    parserOrganize.add_argument("--path", required=True, help= "Path to folder")

    #rename
    parserRename = subparsers.add_parser("rename", help="Batch rename files")
    parserRename.add_argument("--path", required =True, help = "Path to folder")
    parserRename.add_argument("--prefix", required=True, help ="Prefix for file names")

    #compress 
    parserCompress = subparsers.add_parser("compress", help = "compress files")
    parserCompress.add_argument("--path", required = True, help = "compress files")

        #copyfile
    parserCompress = subparsers.add_parser("copy", help = "copy a file")
    parserCompress.add_argument("--fileName", required= True, help = "copy a file")

    parserCompress = subparsers.add_parser("exit", help = "exit console")
    

    parserCompress = subparsers.add_parser("email", help = "send email")
    parserCompress.add_argument("--fileName", required=True)
    parserCompress.add_argument("--fromEmail", required=True)
    parserCompress.add_argument("--toEmail", required=True)

    
    args = parser.parse_args()

    if args.command == "organize":
        organizeFiles(args.path)
    elif args.command == "compress":
        compressFiles(args.path)
    elif args.command == "rename":
        renameFiles(args.path, args.prefix)
    elif args.command == "copy":
        copyFile(args.fileName)
    elif args.command == "email":
            sendingEmail(args.fileName, args.fromEmail, args.toEmail)
    elif args.command == "exit":
        exitCode = True
    else:
        parser.print_help()
    






def main():
    
  
    printUI()


        

        
    
if __name__ == "__main__":
    main()