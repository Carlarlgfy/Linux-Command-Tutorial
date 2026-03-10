def tutorial_add_user():
    print("\nUSER CREATION TUTORIAL\n")
    print("This exercise teaches how Linux creates and removes system users.")
    print("User accounts are required when multiple people share a machine or when services run under specific identities.")
    print("Understanding this helps with system administration and security.\n")

    print("STEP 1")
    print("su")
    print("enter the root password to become the root user\n")

    print("STEP 2")
    print("cut -d: -f1 /etc/passwd")
    print("lists all user accounts currently on the system\n")

    print("STEP 3")
    print("useradd -m testuser")
    print("creates a new user and home directory named testuser\n")

    print("STEP 4")
    print("passwd testuser")
    print("sets the password for the new user account\n")

    print("STEP 5")
    print("su testuser")
    print("switches to the new user account to test that the login works\n")

    print("STEP 6")
    print("whoami")
    print("confirms you are now operating as testuser\n")

    print("STEP 7")
    print("exit")
    print("returns you to the previous user account\n")

    print("STEP 8")
    print("userdel -r testuser")
    print("removes the user and their home directory from the system\n")


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

    print("UNDERSTANDING THE OUTPUT OF df -h\n")

    print("COLUMNS IN df -h OUTPUT\n")

    print("Filesystem")
    print("the disk device or virtual filesystem being reported\n")

    print("Size")
    print("the total size of the filesystem\n")

    print("Used")
    print("how much space is currently used\n")

    print("Avail")
    print("how much space is still available\n")

    print("Use%")
    print("percentage of the disk that is currently full\n")

    print("Mounted on")
    print("the directory where that filesystem is attached in the Linux directory tree\n")

    print("udev")
    print("device manager used by the Linux kernel for hardware devices\n")

    print("tmpfs")
    print("temporary filesystem stored in RAM used for temporary files\n")

    print("/dev/sda1")
    print("a partition on the main hard drive or SSD where the operating system is stored\n")

    print("/dev/sda2")
    print("another partition on the same physical drive (may store data or swap)\n")

    print("/dev")
    print("directory that represents hardware devices as files\n")

    print("/")
    print("the root filesystem this is the main top level of the entire Linux system\n")

    print("/home")
    print("where normal user files and personal directories are stored\n")

    print("/boot")
    print("contains files needed for the system to start up the Linux kernel and bootloader\n")

    print("These entries help you understand where disk space is being used on the system.\n")


def tutorial_files():
    print("\nFILE CREATION AND DELETION TUTORIAL\n")
    print("Files are the basic units of data storage in Linux.")
    print("Learning how to create and delete files is essential for scripting, logging, and everyday terminal work.\n")

    print("STEP 1")
    print("touch example.txt")
    print("creates a new empty file named example.txt\n")

    print("STEP 2")
    print("ls")
    print("lists files in the current directory so you can see the file\n")

    print("STEP 3")
    print("rm example.txt")
    print("deletes the file\n")


def tutorial_folders():
    print("\nFOLDER CREATION AND DELETION TUTORIAL\n")
    print("Folders (directories) organize files in Linux.")
    print("System administrators use directories to structure projects, logs, and user environments.\n")

    print("STEP 1")
    print("mkdir testfolder")
    print("creates a new directory named testfolder\n")

    print("STEP 2")
    print("ls")
    print("lists directories and files so you can confirm it exists\n")

    print("STEP 3")
    print("rmdir testfolder")
    print("removes the directory if it is empty\n")


def tutorial_root():
    print("\nROOT ACCESS TUTORIAL\n")
    print("Root is the superuser account in Linux.")
    print("It has full control over the system and can modify system files, users, and services.")
    print("Normal users have limited permissions to prevent accidental or dangerous changes.")
    print("System administration tasks usually require root privileges.\n")

    print("STEP 1")
    print("whoami")
    print("shows which user you are currently logged in as\n")

    print("STEP 2")
    print("su")
    print("switches to the root user (you must enter the root password)\n")

    print("STEP 3")
    print("whoami")
    print("run it again to confirm you are now root\n")

    print("STEP 4")
    print("exit")
    print("leaves the root account and returns to your normal user\n")

    print("STEP 5")
    print("whoami")
    print("confirms you are back to the normal user\n")


def tutorial_usb():
    print("\nUSB FILE TRANSFER TUTORIAL\n")
    print("This tutorial shows how to manually mount a USB drive and copy files from it.")
    print("This method works even if the Linux machine has no internet connection.\n")

    print("STEP 1")
    print("su")
    print("switch to the root user because mounting drives requires administrator privileges\n")

    print("STEP 2")
    print("lsblk")
    print("lists all storage devices so you can identify the USB drive")
    print("look for something like sdb1 which is usually the USB partition\n")

    print("STEP 3")
    print("mkdir -p /mnt/usb")
    print("creates a mount point where the USB drive will appear\n")

    print("STEP 4")
    print("mount /dev/sdb1 /mnt/usb")
    print("mounts the USB drive to the /mnt/usb directory\n")

    print("STEP 5")
    print("ls /mnt/usb")
    print("shows the files stored on the USB drive\n")

    print("STEP 6")
    print("cp /mnt/usb/filename.py /home/charles/python_code/")
    print("copies the file from the USB drive into your python_code directory\n")

    print("STEP 7")
    print("ls /home/charles/python_code")
    print("confirms the file was copied successfully\n")

    print("STEP 8")
    print("umount /mnt/usb")
    print("unmounts the USB drive so it can be safely removed\n")


def main():
    while True:
        print("\nLINUX TERMINAL PRACTICE\n")
        print("1 user creation tutorial")
        print("2 group management tutorial")
        print("3 permissions tutorial")
        print("4 disk usage tutorial")
        print("5 file creation tutorial")
        print("6 folder creation tutorial")
        print("7 root access tutorial")
        print("8 usb file transfer tutorial")
        print("9 exit\n")

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
            tutorial_files()

        elif choice == "6":
            tutorial_folders()

        elif choice == "7":
            tutorial_root()

        elif choice == "8":
            tutorial_usb()

        elif choice == "9":
            break

        else:
            print("invalid selection")


main()