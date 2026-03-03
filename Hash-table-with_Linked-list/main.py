class LinkedList:
    def __init__(self, value=None, key=None):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.max_entries = 50
        self.entries = [LinkedList() for _ in range(self.max_entries)]

    def hash(self, value):
        return value % self.max_entries

    def add_in_map(self, key, value):  # Add element in hash table
        node = self.entries[self.hash(key)]
        while node and node.next:
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next
        node.next = LinkedList(key=key, value=value)

    def get_from_map(self, key):  # Get value by key from hash table
        node = self.entries[self.hash(key)].next
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove_from_map(self,key):  # Remove element by key from hash table
        node = self.entries[self.hash(key)]
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
            node = node.next

    def print_map(self, empty):  # Print elements in hashtable, empty == 0 - print all, empty == 1 - print non-empty
        for i in range(0, self.max_entries):
            node = self.entries[i]
            arr = []
            while node:
                if node.value != None:
                    arr.append(node.value)
                node = node.next
            if empty == 1:
                if len(arr) != 0:
                    print(arr)
            else:
                print(arr)




def main():
    table = HashMap()

    table.add_in_map(10,10)
    table.add_in_map(20,20)
    table.add_in_map(30,30)
    table.add_in_map(25,25)
    table.add_in_map(20, 20)
    table.add_in_map(70, 70)


    a = table.get_from_map(10)
    b = table.get_from_map(27)
    print(a,b)
    table.print_map(empty=1)
    table.remove_from_map(30)

    table.print_map(empty=1)


if __name__ == '__main__':
    main()