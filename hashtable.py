
from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.length_of_hashtable = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case run time: O(n2) n for all the ll's,
        and another n for nodes(key-value pairs) within each ll
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case run time: O(n2) n for all the ll's,
        and another n for nodes(key-value pairs) within each ll
        """
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Run time: O(n) n for total number of items in buckets
        To be more specific, O(b*n): b is number of buckets, and n is average number of items in all buckets
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Run time: O(n) because we loop through every bucket in the hash table
        """
        # using length method in the linkedlist class
        # length_hash = 0
        # for bucket in self.buckets:           # O(b) where b is the length of the buckets
        #     length_hash += bucket.length()    #   O(l)
        # return length_hash        # this would be O(bl) --> O(b*(n/b)) --> O(n)

        # incrementing the count when we append and decrementing the count when we delete
        return self.length_of_hashtable

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Run time: O(n) because we call the find method on the bucket at the specified index
        """
        ind = self._bucket_index(key)
        specific_bucket = self.buckets[ind]
        return specific_bucket.find(lambda entry: entry[0] == key) is not None


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Run time: O(n) because we call the find method on the specified index
            where n is the number of key-value entries
        """
        ind = self._bucket_index(key)           # constant time
        specific_bucket = self.buckets[ind]     # constant time
        found_item = specific_bucket.find(lambda entry: entry[0] == key)    # O(l) where l is the bucket's length
        if found_item is not None: # found
            return found_item[1] # found_item = (key, value)
        else:
            raise KeyError('Key not found: {}'.format(key))



    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case O(1) if item is located near the head of list
        Run time: O(n) because we call the find method on the specified index
        Actually O(2n) but is O(n) where n is the length of items in the bucket
        """
        ind = self._bucket_index(key)
        specific_bucket = self.buckets[ind]
        # checking in the linkedlist
        found_item = specific_bucket.find(lambda entry: entry[0] == key)
        if found_item is not None:
            specific_bucket.replace(found_item, (key, value))       # O(n) time
        else:
            specific_bucket.append((key, value))
            self.length_of_hashtable += 1



    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Best case run time: O(1) if the items are near the beginning of the ll
        Worst case run time: O(n) if the items are near the end of the ll
        """
        ind = self._bucket_index(key)
        specific_bucket = self.buckets[ind]         # O(1) Constant time
        found_item = specific_bucket.find(lambda item: item[0] == key)  # O(l) average length of that ll # returns a key-value pair if found
        if found_item is not None:                  # O(1) Constant time
            specific_bucket.delete(found_item)      # O(l) lenght of that ll
            self.length_of_hashtable -= 1
        else:
            raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting values method:')
    print(ht.values())

    print('\nTesting keys method:')
    print(ht.keys())

    print('\nTesting length method:')
    print(ht.length())

    print('\nTesting contains method:')
    print(ht.contains('X'))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
