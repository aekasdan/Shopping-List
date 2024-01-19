#Nova and Alice
#12/10
#Shopping List

#Init
shoppingList = []
#Functions
def addTask():
    task = input("What task would you like to add?: ")
    shoppingList.append(task)
    print(shoppingList)
    editList()
def viewList():
    print(shoppingList)
    editList()
def removeTask():
    task2 = input("Which item would you like to remove?: ")
    shoppingList.remove(task2)
    print(shoppingList)
    editList()
def markComplete():
    ans = input("Select an item from the list to mark as complete: ")
    i = shoppingList.index(ans)
    shoppingList[i] = ans + " :X"
    print(shoppingList)
    editList()
def exitProgram():
    print("Thank you for using this program")
    quit()

def clearList():
    shoppingList.clear()
    print(shoppingList)
    editList()
def sortList():
    shoppingList.sort()
    print(shoppingList)
    editList()
def countItems():
    x = shoppingList.__len__()
    print(x)
    editList()


def editList():
    ans = (input("Would you like to (1) add an item, (2) view your list, (3) mark an item as completed, (4) remove an item, (5) remove all items from the list, (6) sort the list, (7) count the items on the list, or (8) exit the program? "))
    if ans == ("1"):
        addTask()
    elif ans == ("2"):
        viewList()
    elif ans == ("3"):
        markComplete()
    elif ans == ("4"):
        removeTask()
    elif ans == ("5"):
        clearList()
    elif ans == ("6"):
        sortList()
    elif ans == ("7"):
        countItems()
    elif ans == ("8"):
        exitProgram()
    else:
        print("Invalid response, try again")
        editList()

#Main
editList()