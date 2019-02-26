
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.length_item = 0   # length of ll
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(1)
        O(1) because we have a stored property where we increment each time we create a node, and decrement
        each time we delete a node!
        """
        # count = 0
        # if self.head is None:
        #     return count
        # head = self.head
        # while head is not None:
        #     count += 1
        #     head = head.next
        # return count
        
        return self.length_item

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1)
        O(1) because we only check for 1 value which is at the tail
        """
        new_node = Node(item)
        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node
            self.length_item += 1
        else:
            self.head = new_node
            self.tail = new_node
            self.length_item += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1)
        O(1) because we're just changing the first node in the linked list and not iterating through nodes
        """
        new_node = Node(item)
        head = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length_item += 1
        else:
            new_node.next = head
            self.head = new_node
            self.length_item += 1

    def replace(self, old, new):
        head = self.head
        while head is not None:
            if head.data == old:
                head.data = new
                return True
            else:
                head = head.next
        return 'Item not in linked list: {}'.format(old)


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        head = self.head
        # print("outside")
        # print(head.next) # 'B'
        # print(quality(head.next.data)) # 'B'
        # print("In while loop")
        while head is not None:
            # print(head) ->>> 'B'
            # print(quality(head.data)) ->>> True
            if quality(head.data):
                return head.data
            else:
                head = head.next
        return None


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        node_to_delete = Node(item)
        current = self.head
        previous = None
        while current:
            if current.data == item:
                if previous:
                    if current == self.tail:
                        self.tail = previous
                    previous.next = current.next
                    self.length_item -= 1
                else:
                    if current == self.tail:
                        self.tail = previous
                    self.head = current.next
                    self.length_item -= 1
                return True

            previous = current
            current = current.next


        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

    # find method
    print('\nTesting find:')
    ll = LinkedList(['A', 'B', 'C'])
    print(ll.find(lambda item: item == 'B'))

    # replace method
    print('\nTesting replace:')
    print(ll)
    print(ll.replace('B', 'Replaced'))
    print(ll)


if __name__ == '__main__':
    test_linked_list()
