from itertools import count


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self._head=None

    def is_empty(self):
        return not self._head

    def push(self,data):
        new_node=Node(data)
        new_node.next= self._head
        self._head = new_node

    def append(self,data):
        if self.is_empty():
            self._head=Node(data)
            return
        temp=self._head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)

    def delete_first(self):
        if not self.is_empty():
            self._head=self._head.next

    def delete_after(self,data):
        temp=self._head
        while temp.next:
            if temp.data == data:
                deleted=temp.next
                temp.next=temp.next.next
                return deleted
            temp = temp.next()
        return None

    def find(self,data):
        temp=self._head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next()
        return None

    def length(self):
        temp = self._head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        return count

    def print_list(self):
        temp = self._head
        while temp:
            print(temp.data, "-> ", end="")
            temp = temp.next
        print("|")

    def find_index(self,num):
        temp = self._head
        index = 0
        while temp:
            if index == num:
                return temp
            temp = temp.next
            index+=1
        return None




