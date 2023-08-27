class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.new_node = Node(value)
        self.head = self.new_node
        self.tail = self.new_node
        self.length = 1

    def print_list(self):
        """Print all the nodes value"""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """Add a value to the end of the list"""
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Remove the last item of the list"""
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while (temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """_Add item in the begining of the list_"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """Remove the first item from the list"""
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = 0
            self.tail = None
        return temp

    def get(self, index):
        """Find the corrosponding item based on the given index"""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """Set value of index number"""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Insert value in a specific index position"""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """Remove any item in a specific index"""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """Reverse the list"""
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
    def find_middle_node(self):
        # Initialize two pointers to the head of the list
        slow = self.head
        fast = self.head
        
        # Traverse the list with the fast pointer moving twich speed as the fast as the slow pointer
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.append(5)
# my_linked_list.pop()
# my_linked_list.prepend(1)
# my_linked_list.pop_first()
# my_linked_list.set_value(1, 5)
# my_linked_list.insert(0, 1)
# my_linked_list.remove(0)
# my_linked_list.reverse()
# print(my_linked_list.get(0))
# print(my_linked_list.find_middle_node())
# my_linked_list.print_list()
