from menu import *

def main():
    while True:
        try:
            showMenu()
            choice = input("enter choice: ")

            if choice == "1":
                menuAdd()

            elif choice == "2":
                menuUpdate()

            elif choice == "3":
                menuRemove()

            elif choice == "4":
                menuShow()

            elif choice == "5":
                menuAddToQueue()

            elif choice == "6":
                menuComplete()

            elif choice == "7":
                menuUndo()

            elif choice == "8":
                menuHistory()

            elif choice == "9":
                menuShowQueue()

            elif choice == "0":
                print("Goodbye")
                break

            else:
                print("invalid choice")

        except Exception as e:
            print("something went wrong:", e)


main()