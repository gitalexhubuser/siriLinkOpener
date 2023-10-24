import os

def fix_directory():
    cwd = os.getcwd()
    print("Текущая рабочая директория: ", cwd)

    # new_working_directory = r"E:\YandexDisk\Python\![2023] Jarvis Chat (Bogatov)\Gotham\1.2" # Я
    new_working_directory = r"D:\Gotham(py)\4" # Енотик

    try:
        os.chdir(new_working_directory)
        print("The working directory has been changed!")
        print("WD: %s " % os.getcwd())
    except NotADirectoryError:
        print("You have not chosen a directory.")
    except FileNotFoundError:
        print("The folder was not found. The path is incorrect.")
    except PermissionError:
        print("You do not have access to this folder/file.")