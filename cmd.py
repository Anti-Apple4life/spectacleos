import os
import start
name=start.name


value=True # Repeats command line infinitely
while (value):
        cmdLine=input(name+" "+os.getcwd()+'> ')
        if cmdLine == "fuzzver":
                vvCmd=open("version-gui.txt", "r")
                print(vvCmd.read())
        if cmdLine == "dirn":
                print(os.getcwd())
        if cmdLine == "dir":
                print(os.listdir())
        if cmdLine == "chdir":
                chPath=input("Path> ")
                os.chdir(chPath)
        if cmdLine == "fe":
                feName=input("What to name file? Or if file already exists, type name here. Current working directory is "+os.getcwd()+".> ")
                feOption=input("Append or overWrite? a/w> ");
                f = open(feName, feOption)
                fText=input("FuzzEdit:Enter text, press enter> ")
                f.write(fText)
                print("Reading file.")
                f = open(feName, "r")
                print(f.read())
                print("🔔 This file is located in "+os.getcwd()+".")
        if cmdLine == "help":
                help=open("help.txt", "r")
                print(help.read())
        if cmdLine == "exit":
                exit()
        if cmdLine == "echo":
                echoI=input("echo> ")
                print(echoI)
        if cmdLine == "makef":
                makeFi=input("makef> ")
                os.mkdir(makeFi)
                print("🔔 This folder is located in "+os.getcwd()+"/exit"+makeFi+".")
