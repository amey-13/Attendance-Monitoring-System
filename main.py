import os  # accessing the os functions
import Capture_Image
import train_image
import recognize


# creating the title bar function

def title_bar():
    os.system('cls')  # for windows

    print("\t***** Face Recognition Attendance System *****")

# creating the user main menu function

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Capture Faces")
    print("[2] Train Images")
    print("[3] Recognize & Attendance")
    print("[4] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                CaptureFaces()
                break
            elif choice == 2:
                Trainimages()
                break
            elif choice == 3:
                RecognizeFaces()
                break
            elif choice == 4:
                print("Quit")
                break
            else:
                print("Invalid Choice. Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-3\n Try Again")
    exit


# calling the take image function form capture_image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()


# calling the train images from train_image.py file

def Trainimages():
    train_image.TrainImages()
    key = input("Enter any key to return main menu")
    mainMenu()


# calling the recognize_attendance from recognize.py file

def RecognizeFaces():
    recognize.Recognizefaces()
    key = input("Enter any key to return main menu")
    mainMenu()


# ---------------main driver code------------------
mainMenu()