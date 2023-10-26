
import os
import subprocess

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Enter thename of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)
    
def remove_user():
    confirm = "N"
    while confirm != "Y":
        username =input ("Enter the name of the user to remove: ")
        print("Remove the user:'" + username + "'?(Y/N)")
        confirm = input().upper()
    os.system("sudo userdel -r" + username )
    
def add_user_to_group():
    username = input("Enter the name of the user that you wantto addto agroup: ")
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    print("Enter a list of groups to add the user to")
    print("The list should be separatedby spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output)
    chosenGroups = input("Groups: ")
    output = output.split(" ")
    chosenGroups = chosenGroups.split(" ")
    print("Add To:")
    found = TruegroupString = ""
    for grp in chosenGroups:
        for existingGrp in output:
            if grp == existingGrp:found = True
            print("-Existing Group : " + grp)
            groupString= groupString + grp + ","
        if found == False:
            print("-New Group : " + grp)
            groupString = groupString + grp + ","
        else:found = False



    
new_user()
remove_user()
add_user_to_group()