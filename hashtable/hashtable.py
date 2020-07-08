class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
      self.data = [None] * capacity
      self.capacity = capacity
      self.size = 0  


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # data_bytes = key.encode()
        hash = 5381

        for byte in key:
          hash = (( hash << 5) + hash) + ord(byte)

        return hash & 0xffffffff


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # self.data[index] = value
        # if linkedlist doesn't exist create one with key value
        if(self.data[index] == None):
            self.data[index] = HashTableEntry(key, value)
            self.size +=1
        else:
            #check if item already exists in linked list
            curr = self.data[index]
            while curr.next and curr.key != key:
                curr = curr.next
            if curr.key == key:
                curr.value = value
            #it doesn't exist add it
            else:
                curr.next = HashTableEntry(key, value)
                self.size +=1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2 )


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # self.data[index] = None
        if self.data[index].key == key:
            # First check if it is the only thing in the list
            if self.data[index].next == None:
                # delete the item by turning it to None
                self.data[index] = None
                # shrink size of filled index
                self.size -=1
            # it is not the only one in the list
            else:
                # assign the next item to a temp variable 
                new_head = self.data[index].next
                # disconnect the first item from connecting to next
                self.data[index].next = None
                # make temp variable the first item
                self.data[index] = new_head
                # shrink size of filled index
                self.size -=1
        #node was not first in the list or is none
        else:
            if self.data[index] == None:
                return None
            else:
                curr = self.data[index]
                prev = None
                #search until at end or have found key
                while curr.next != None and curr.key != key:
                    prev = curr
                    curr = curr.next
                # found the key
                # connect previous node to next node skipping current --essentially deleting it
                if curr.key == key:
                    prev.next = curr.next
                    self.size -=1
                    return curr.value
                #didn't find the key
                else:
                    print("key not found")
        # resize if needed
        if self.get_load_factor() < 0.2:
            self.resize(self.capacity // 2)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # Returns None if the key is not found.

        if self.data[index] is None:
            return None

        if self.data[index].key == key:
            return self.data[index].value
        else:
            curr = self.data[index]
            while curr.next != None and curr.key != key:
                curr = curr.next
            if curr.key == key:
                return curr.value
            return curr.value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        curr = self.data

        self.capacity = new_capacity
        self.data = [None] * new_capacity

        for item in curr:
                while item:
                    self.put(item.key, item.value)
                    item = item.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
