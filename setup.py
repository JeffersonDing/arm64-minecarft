import sys
import shutil
import os
import json
from print_color import printc


path = sys.argv[1]

def setup():
    if not os.path.isdir(path):
        printc("please input a valid directory as an argument","ERROR")
        print("e.g. python setup.py /Users/admin/Library/Application Support/minecraft")
        exit()

    printc("ARM64 Native Minecraft Setup Script - For Apple Sillicon MacBooks","HEADER")
    if(input("Proceed?(y/n) ") != "y"):
        exit()

    if not os.path.exists(path+"/lwjglnatives"):
        shutil.copytree("./lwjglnatives",path+"/lwjglnatives")
        shutil.copy("./lwjglfat.jar",path+"/libraries/lwjglfat.jar")

def select():
    versions = []
    for i,j in enumerate([ name for name in os.listdir(path+"/versions") if os.path.isdir(os.path.join(path+"/versions", name)) ]):
        versions.append(j)
        printc(str(i)+". ","OKGREEN","")
        print(j)

    ver = int(input("Please select the version to modify:"))

    if(ver > len(versions)):
        printc("Please enter a valid number","ERROR")
        exit()

    if(input(f"Selected {versions[ver]}, proceed?(y/n) ") != "y"):
        exit()

    newpath = path+"/versions/"+versions[ver]+"-arm/"
    shutil.copytree(path+"/versions/"+versions[ver], newpath)

    os.rename(newpath+versions[ver]+".jar",newpath+versions[ver]+"-arm.jar")
    os.rename(newpath+versions[ver]+".json",newpath+versions[ver]+"-arm.json")

    modify(newpath+versions[ver]+"-arm.json",versions[ver]+"-arm")

# Modify JSON

def modify(path,ver):
    jvm_args = ["${natives_directory}/../../libraries/lwjglfat.jar:${classpath}",
      "-Dorg.lwjgl.librarypath=${natives_directory}/../../lwjglnatives/",
      "-Dfml.earlyprogresswindow=false"]
    f = open(path)

    data = json.load(f)
    data["id"] = ver
    data["arguments"]["jvm"].pop()
    data["arguments"]["jvm"].extend(jvm_args)

    new_lib = []
    for item in data["libraries"]:
        if("lwjgl" not in item["downloads"]["artifact"]["url"]):
            new_lib.append(item)
    
    data["libraries"] = new_lib

    with open(path, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    try:
        setup()
        select()
        printc("Successful!","OKGREEN")
    except:
        printc("Error Occured.","ERROR")

