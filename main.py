from zipfile import ZipFile
import sys
import os

argv = False


def options():
    print("""
     ZipFile          :   Enter path to zip file.
     pwdList          :   Enter path to dictionary.
     exit             :   Exit from the tool.
     help             :   Show help.
	""")


try:
    if (sys.argv[1] in ['help', '--help', 'h', '-help', '-h']):
        options()
        argv = True
    else:
        pass
except:
    pass

if (argv == True):
    sys.exit()
else:
    pass

os.system("clear")

while (True):
    try:
        exit = False
        action = input("\nZip file > ")
        if (action == "exit"):
            exit = True
            break
        elif (action == "help"):
            options()
        else:
            pass
        try:
            zip = ZipFile(action, "r")
            break
        except:
            if (action == "" or action == "help"):
                pass
            else:
                print("\n\033[0;91m[!] Unable to locate the zip file!\033[0;0m")
    except:
        pass

if (exit == True):
    sys.exit()
else:
    pass

list = input("\nPassword list > ")

try:
    pwds = open(list, "rb")
    counter = open(list, "r")
except:
    print("\n\033[0;91m[!] Unable to locate the password list!\033[0;0m")
    sys.exit()

print("\n")
looper = counter.readline()
flag = 0
while (looper):
    password = pwds.readline()
    try:
        zip.extractall(path="Extract", pwd=password.strip())
        print("\nPassword --> {}".format(password.decode()))
        flag += 1
        break
    except:
        print('Trying --> ' + password.decode())
    looper = counter.readline()

if (flag == 0):
    print("\n[Password not found!]")
else:
    pass

zip.close()
pwds.close()
counter.close()
