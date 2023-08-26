toDoList = ['hello', 'Chicken', 'smelly']
freespaces = []

def menu():
    inUse = True
    print("To Do List")
    print("==========")
    while inUse == True:
        choice = input("What do you want to do? 1)View List 2)Add Item 3)Remove Item 4)Exit Application: ")
        if choice == "1":
            viewItems(toDoList)
        elif choice == "2":
            addItem(toDoList)
        elif choice == "3":
            removeItem(toDoList)  
            emptySpotCheck(toDoList, freespaces)
        elif choice == "4":
            exitApplication(inUse)
        else:
            print("Invalid choice")
            

def viewItems(toDoList):
    print("Your to do list is: ")
    count = 1
    for x in toDoList:
        print(f"{count}) {x}")
        count += 1

def addItem(toDoList):
    inProgress = True
    while inProgress == True:
        listItem = input("What task would you like to add: ")
        toDoList.append(listItem)
        print(toDoList)
        choice = input("Would you like to continue? 1) Yes 2) No ")
        if choice == "2":
            inProgress = False

def removeItem(toDoList):
    viewItems(toDoList)
    i = int(input("What item would you like to remove? "))
    toDoList[i - 1] = None
    print(toDoList)


def exitApplication(inUse):
    inUse = False
    print("===================")
    print("Exiting Application")

def emptySpotCheck(toDolist, freespaces):
    for i in range(len(toDoList)-1):
        if toDoList == None:
            freespaces.append(i)
    print(freespaces)

menu()

