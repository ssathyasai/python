def add_item(cart):
    item=input("Enter item to add into cart:")
    cart.append(item)

def remove_item(cart):
    item=input("Enter item to remove from cart:")
    cart.remove(item)

def search_item(cart):
    item=input("Enter item to Search in cart:")
    for i in cart:
        if(i==item):
            print(item," is available in cart ")

def display_items(cart):
    for i in cart:
        print(i,end=" ")
    print()

def no_of_items(cart):
    item_count=0
    for i in cart:
        item_count+=1
    print("No.of items in the cart are :",item_count)
def sort_items(cart):
    cart.sort()
    print("Items sorted in order")
def clear_items(cart):
    cart.clear()


cart=["apple","bananna"]

while(True):
    print("\n1.Add item\n2.Remove item\n3.Search item\n4.Display items\n5.Count items\n6.sort\n7.clear\n8.Exit")
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
