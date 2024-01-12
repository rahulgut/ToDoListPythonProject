import sys

### Variables
main_list = []

### Functions
def help():
    print("------------------------------------")
    print("Hello, I am your best todo list! ♥️")
    print("------------------------------------")
    print("\n")
    print(" You can list add and remove the todo's like:")
    print("     > help(me): Shows the help content for me.")
    print("     > save \"YOUR_TODO\": Saves the todo.")
    print("     > list: Shows all saved todo(s).")
    print("\n")

def list():

def add(argument):

# The first command line argument (index 0) is the script name
# Actual arguments start from index 1
if len(sys.argv) > 1:
    # Print all command line arguments
    print("Command line arguments:", sys.argv[1:])
    if len(sys.argv) == 2 and sys.argv[1] == "help":
        help()
    if sys.argv[1] == "add"
        if len(sys.argv) == 3

        help()

else:
    help()