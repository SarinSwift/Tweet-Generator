# Personal Notes  


## [Linked Lists](https://github.com/SarinSwift/Tweet-Generator/blob/master/linkedlist.py)
 *Feb.18*   
A linked list is formed by linking nodes together. These nodes contain 'data' and 'next'. 

***Append item:*** *Inserting a node at the end of a linked list.*  
Changing the pointer of the current last node of the linkedlist to the new node  
Reassign the tail pointer to the new node  
Runtime: O(1) 

***Prepend item:*** *Inserting a node at the beginning of a linked list.*  
Setting the new node's next to the current head of the linkedlist  
Reassign the head pointer to the new node  
Runtime: O(1) 

***Delete item:*** *Deleting a node from a linked list.*  
Loop through the linked list until we find the node we want to delete  
Locate the prev node of the node which is to be deleted  
Point the next pointer of the prev to the next node of the node to be deleted  
Runtime: O(n) where n is the number of elements because we'll have to find the element first.

***Length of linkedlist:*** *Calculates the length of a linked list.*  
Has a stored property (return self.length_item) where we increment each time we create a node, and decrement each time we delete a node!   
Runtime: O(1)  

***Find quality:*** *Find an item using a matching function.*  
Loop through the linkedlist and checks if an item satisfies a given quality  
Runtime: O(n) where n is the number of elements because we'll have to find the element first.

## [Hash Tables](https://github.com/SarinSwift/Tweet-Generator/blob/master/hashtable.py)
*Feb.20*  
A data structure that powers Python's dictionary feature. Dictionaries allow you to map keys to values.  
```
index = hashNumber % numberOfBuckets   
```

***Set(key and value):*** *Insert or update the given key with its associated value*  
Get the key's hash value, and calculate the index using the modulus operator  
Use the index to get the bucket where the entry should be stored  
Call the find method on the bucket to retreive the entry(Tuple of key and value)  
If we've found the item, replace the old entry with the new entry(Tuple of key and value)  
else, just append the new entry  

***Get(key):*** *Return the value associated with the given key*  
Get the key's hash code and calculate the index  
Use the index to get a bucket  
Call the find method on the bucket to retreive the entry  
If there is a value, return the entry's key  
else, raise KeyError  

***Delete(key):*** *Delete the given key from this hash table*  
Check if the key-value entry exists in the bucket  
If found, delete from the specific bucket associated with the given key  
else, raise KeyError

***Contains(key):*** *Return True if this hash table contains the given key*  
Go to the specific bucket  
Call the find method on the specific bucket and return True if there's a value  

***Find length:*** *Return the number of key-value entries by traversing its buckets*  
Loop through all buckets  
call the length method on each specific bucket, and increment the count    
return the length

***Get a list of all keys:***  
Loop through the linkedlists in the array of buckets  
Loop through the bucket.items() to append the keys to an empty list  
return the list of all keys in the hash table

***Get a list of all values:***  
Loop through the linkedlists in the array of buckets  
Loop through the bucket.items() to append the values to an empty list  
return the list of all values in the hash table 

***Get a list of all entries(key-value pairs):***  
Loop through the linkedlists in the array of buckets  
extend to the empty list with bucket.items()  
return the pairs of key-value entries in each bucket


## [Dictogram](https://github.com/SarinSwift/Tweet-Generator/blob/master/dictogram.py)
*Feb.18*  
***Dictogram*** is a histogram implemented as a subclass of the dict type.  
**types:** Count of distinct words  
**tokens:** Total count of all occurences of words
  
word list: ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']  
dictogram: {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}  
8 tokens, 5 types  
'blue' occurs 1 times  
'fish' occurs 4 times  

## [Listogram](https://github.com/SarinSwift/Tweet-Generator/blob/master/listogram.py) 
*Feb.18*   
***Listogram*** is a histogram implemented as a subclass of the list type.  
  
word list: ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']  
listogram: [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]  
8 tokens, 5 types  
'blue' occurs 1 times  
'fish' occurs 4 times  
