def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i

    return None


def verify(index):
    if index is not None:
        print("target found at index:", index)
    else:
        print("target dos not found ")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = linear_search(numbers, 8)
verify(result)


def binary_search(list, target):
    first = 0
    last = len(list) - 1
    midpoint = (first + last) // 2
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1


result1 = binary_search(numbers, 4)
verify(result1)


def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint]==target:
            return  True
        else:
            if list[midpoint]<target:
                return (recursive_binary_search(list[midpoint+1:],target))
            else:
                return (recursive_binary_search(list[:midpoint],target))

def verify_recursivebinary(function):
    if function is not False:
        print("target found ")
    else:
        print("target dos not found ")

verify_recursivebinary(recursive_binary_search(numbers,12))
#array (python)
new_list=[1,2,3,4]
print(new_list[0])
if 1 in new_list:
    print(True)
    #because it is not fumction we cant return
# for n in new_list:
#     if n==1:
#         print(True)
#         break
from Node import  Node
from Linkedlist import  Linkedlist
list =Linkedlist()
# def list_insert(list,data):
#     new_node=Node(10)
#     new_node.nex_node=list.head
#     if list.head != None:
#         list.head.prev_node=new_node
#     list.head=new_node
#     new_node.prev_node=None

list.list_insert(2)
list.list_insert(3)
list.list_insert(4)
list.list_insert(5)
list.list_delete(2)
list.print()
