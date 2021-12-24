bcolors = {
    "HEADER" : '\033[95m',
    "OKBLUE" : '\033[94m',
    "OKCYAN" : '\033[96m',
    "OKGREEN" : '\033[92m',
    "WARNING" : '\033[93m',
    "FAIL" : '\033[91m',
    "ENDC" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m'
    } 

def printc(str,color,endl="\n"):
    print(bcolors[color]+str+bcolors["ENDC"],end=endl)


if __name__ == "__main__":
    printc("test","WARNING")



