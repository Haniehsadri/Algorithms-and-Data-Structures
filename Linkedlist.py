from Node import Node


class Linkedlist:
    def __init__(self):

        self.head = None

    # def  is_empty(self):
    #   return self.head==None
    # def size(self):
    #     current=self.head
    #     count=0
    #     while current != None:
    #         count+=1
    #         current=current.next_node
    #     return count
    def list_insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        if self.head != None:
            self.head.prev_node = new_node
        self.head = new_node
        new_node.prev_node = None

    def list_search(self,data):
        current=self.head
        while current!=None and current.data!=data:
            current=current.next_node
        return current

    def list_delete (self,data):
        current=self.list_search(data)
        if current.prev_node!=None:
            current.prev_node.next_node=current.next_node
        else:
            self.head=current.next_node
        if current.next_node!=None:
            current.next_node.prev_node=current.prev_node






    def print(self):
        current = self.head
        result = ""
        while current != None:
            if current == self.head:
                result += "[" + str(current.data)
            if current.next_node == None:
                result += str(current.data) + "]"
            if current.next_node != None and current.prev_node != None:
                result += "," + str(current.data) + ","

            current = current.next_node
        print(result)
