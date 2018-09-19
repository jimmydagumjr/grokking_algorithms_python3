def binary_search(list, item):
    low = 0 # low starts from 0
    high = len(list) - 1 # high is length of list -1

    while low <= high: # while low is less than or equal to high
        mid = (low + high) # middle element = low 
        guess = list[mid]
        if guess == item: # found element so return it
            return mid
        elif guess > item: # if guess is too high subtract 1 from middle
            high = mid - 1 #and set to new high number
        elif guess < item: # if guess is too low add 1 from middle
            low = mid + 1  #and set to new low number
    return None # if item does not exist return none

def list_input():
    # Make a new list with requested elements
    test_list = [] # start w/ empty list
    print("Type 'q' to quit; enter numbers to append to list")
    while True:
        test_element = input("Add number/element: ")
        if test_element == 'q': # 'q' to exit
            break
        test_list.append(int(test_element)) # append element to list
        
    return test_list # return the list

def which_element():
    # Choose which element to find
    pick_element = int(input("What number are you looking for?"))
    return pick_element

test_list = [1, 3, 5, 7, 9]

print(binary_search(test_list, 3)) # output 1
print(binary_search(test_list, -1)) # output None

test_list = list_input()

list_search = which_element()

print("\nHere is the item's index: ")
print(binary_search(test_list, list_search))

