def display_menu():
    print("\n===== To-Do App =====")
    print("l/list: View To-Do List")
    print("a/add. Add Task")
    print("q. Quit")

def list():
    print("id: list")

def add():
    print("add")

def delet():
    print("delete : id")


## Main Funciton -> Entry point for the tool.
def main():
    while True:
        display_menu()
        choice = input("Use python hello.py a/l/q: ")
        if choice == "a":
            add()
        elif choice == "l":
            list()
        elif choice == "q":
            print("Keep finishing your Todo(s)! ♥️")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()