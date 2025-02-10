from Spaceship import Spaceship # from a module import a class


class Node:
    def __init__(self, value): # here the constructor initializes a new node object with data and the pointer .next
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):  # add to the "back", creates node
        new_node = Node(value)
        if (self.length == 0): # if this is the only node, head and tail point to new_node
            self.head = new_node
            self.tail = new_node
        else:                  # if other nodes exist already,
            self.tail.next = new_node # old second to last pointer now is new_node
            self.tail = new_node # new tail is new node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.length == 1:
                self.tail = new_node.next
            self.length += 1
            return

        if index >= self.length:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return

        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def delete_at_index(self, index):
        if self.head is None:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return

        current = self.head
        for i in range(index - 1):
            if current is None or current.next is None:
                raise IndexError("Index out of bounds")
            current = current.next

        if current.next is None:
            raise IndexError("Index out of bounds")

        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        self.length -= 1

    def print_list(self):
        if self.head is None:
            print("List is empty") # Modified to add condition if list is empty
        current_node = self.head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next



# TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.
# TODO : Write function deleteatindex to delete a newnode at any given index. Consider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.

s1 = Spaceship("Voyager", 300)
s2 = Spaceship("Enterprise", 300)
s3 = Spaceship("Atlantis", 300)
s4 = Spaceship("Challenger", 300)
s5 = Spaceship("Artemis", 300)

mylinkedlist = LinkedList(s1)
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.prepend(s4)
mylinkedlist.prepend(s5)
mylinkedlist.print_list()

# Test functions
def test_insert_at_index():
    print("start at with 1 at index 0")
    ll = LinkedList(1)
    ll.print_list()
    print("Insert 3 at End")
    ll.insert_at_index(1, 3)  # Insert at end
    ll.print_list()  # Expected output: 1 2 3
    ll.insert_at_index(1, 2)  # Insert in the middle
    print("Insert 2 in the middle")
    ll.print_list()  # Expected output: 1 2 3

def test_delete_at_index():
    ll = LinkedList(1)
    ll.insert_at_index(1, 2)
    ll.insert_at_index(2, 3)
    print("delete index 1")
    ll.delete_at_index(1)  # Delete middle node
    ll.print_list()  # Expected output: 1 3
    print("delete index 0")
    ll.delete_at_index(0)  # Delete head
    ll.print_list()  # Expected output: 3
    ll.delete_at_index(0)  # Delete last node
    print("delete last index")
    ll.print_list()  # Expected output: list is empty!

# Run tests
print("Insert Test")
test_insert_at_index()
print("Delete Test")
test_delete_at_index()