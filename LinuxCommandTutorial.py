

def tutorial_add_user():
    print("\nUSER CREATION TUTORIAL\n")
    print("This exercise teaches how Linux creates and removes system users.")
    print("User accounts are required when multiple people share a machine or when services run under specific identities.")
    print("Understanding this helps with system administration and security.\n")

    print("STEP 1")
    print("adduser testuser")
    print("creates a new user named testuser\n")

    print("STEP 2")
    print("enter full name when prompted")
    print("this is optional account information\n")

    print("STEP 3")
    print("enter password")
    print("this initializes the user login credentials\n")

    print("STEP 4")
    print("re enter password")
    print("confirms the password\n")

    print("STEP 5")
    print("deluser testuser")
    print("removes the user from the system\n")


def tutorial_groups():
    print("\nGROUP MANAGEMENT TUTORIAL\n")
    print("Groups allow multiple users to share permissions.")
    print("They are commonly used in companies so departments can access shared files.\n")

    print("STEP 1")
    print("groupadd devteam")
    print("creates a new group named devteam\n")

    print("STEP 2")
    print("usermod -aG devteam testuser")
    print("adds testuser to the devteam group\n")

    print("STEP 3")
    print("groups testuser")
    print("shows which groups the user belongs to\n")

    print("STEP 4")
    print("groupdel devteam")
    print("deletes the group\n")


def tutorial_permissions():
    print("\nPERMISSIONS TUTORIAL\n")
    print("Linux uses permissions to control who can access files.")
    print("This is important for security and multi user systems.\n")

    print("STEP 1")
    print("mkdir project_folder")
    print("creates a directory\n")

    print("STEP 2")
    print("chmod 770 project_folder")
    print("owner and group can read write execute others have no access\n")

    print("STEP 3")
    print("chown testuser:devteam project_folder")
    print("changes ownership to user testuser and group devteam\n")

    print("STEP 4")
    print("ls -l")
    print("shows permissions and ownership of files\n")


def tutorial_disk():
    print("\nDISK USAGE TUTORIAL\n")
    print("These commands help monitor disk usage and file sizes.")
    print("System administrators use them to understand storage usage.\n")

    print("STEP 1")
    print("df -h")
    print("shows disk usage in human readable format\n")

    print("STEP 2")
    print("du -sh *")
    print("shows folder sizes in the current directory\n")


def main():
    while True:
        print("\nLINUX TERMINAL PRACTICE\n")
        print("1 user creation tutorial")
        print("2 group management tutorial")
        print("3 permissions tutorial")
        print("4 disk usage tutorial")
        print("5 exit\n")

        choice = input("select tutorial: ")

        if choice == "1":
            tutorial_add_user()

        elif choice == "2":
            tutorial_groups()

        elif choice == "3":
            tutorial_permissions()

        elif choice == "4":
            tutorial_disk()

        elif choice == "5":
            break

        else:
            print("invalid selection")


main()