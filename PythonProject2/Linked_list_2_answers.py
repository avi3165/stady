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
        if not self.is_empty():
            temp=self._head
            while temp.next:
                if temp.data == data:
                    deleted=temp.next
                    temp.next=temp.next.next
                    return deleted
                temp = temp.next
            return "The value you entered does not exist in the list."
        return "The list is empty."

    def find(self,data):
        temp=self._head
        while temp:
            if temp.data == data:
                return temp
            temp = temp.next
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
                return temp.data
            temp = temp.next
            index+=1
        return None
d1 = LinkedList()
d1.push(10)
d1.append(20)
d1.append(30)
d1.append(40)
# d1.print_list()
# print(d1.is_empty())
# print(d1.length())
# print(d1.find(20))
# print(d1.find(50))
print(d1.delete_after(100))