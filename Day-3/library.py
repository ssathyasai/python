def add_item(library):
    item1=int(input("Enter the book id"))
    val=input("Enter title of book")
    library[item1]=val

def remove_item(library):
    item=input("Enter the book id to remove:")
    library.pop(item)

def search_item(library):
    item=input("Enter book id to search title")
    print("the title of book id is :",library.getValue(item))

def update(library):
    item=print("Enter the id of the book to change title")
    value=print("Enter the correct tittle to change")
    library[item]=value
    

def display(library):
    item_count=0
    for i in cart:
        item_count+=1
    print("No.of items in the cart are :",item_count)
def sort_items(cart):
    cart.sort()
    print("Items sorted in order")
def clear_items(cart):
    cart.clear()


library={}

while(True):
    print("\n1.Add book\n2.Remove book\n3.Search book\n4.update title of book\n5.Display all the books\n6.count books \n7.check if title exist\n8.Exit")
    choice=int(input("Select any option(1-6):"))
    if(choice==1):
        print("***Adding items***")
        add_item(cart)
    elif(choice==2):
        print("***Remove items***")
        remove_item(cart)
    elif(choice==3):
        print("***Search items***")
        search_item(cart)
    elif(choice==4):
        print("***Display items***")
        display_items(cart)
    elif(choice==5):
        print("***Counting items***")
        no_of_items(cart)
    elif(choice==6):
        print("Sorting cart in alphabatical order")
        break
    elif(choice==7):
        print("Clearing the cart")
        break
    elif(choice==8):
        print("Exiting.")
        break
    else:
        print("Invalid choice")
