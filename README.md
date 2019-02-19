## Personal Notes  


**[Linked Lists](https://github.com/SarinSwift/Tweet-Generator/blob/master/linkedlist.py)** 
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


# Tweet-Generator: Text Processing & Probability

## Course Schedule

**Course Dates:** Monday, October 23 – Friday, December 8, 2017 (6 weeks)

**Class Times:** Tuesday & Thursday 2-4pm or 4–6pm (12 class sessions)


| Class |         Date          |                  Topics                  |
|:-----:|:---------------------:|:----------------------------------------:|
|   1   |  Tuesday, October 24  | [Strings & Random Numbers](Class1.md)    |
|   2   | Thursday, October 26  | [Histogram Data Structures](Class2.md)   |
|   3   |  Tuesday, October 31  | [Probability & Sampling](Class3.md)      |
|   4   | Thursday, November 2  | [Flask Web App Development](Class4.md)   |
|   5   |  Tuesday, November 7  | [Application Architecture](Class5.md)    |
|   6   | Thursday, November 9  | [Generating Sentences](Class6.md)        |
|   7   |  Tuesday, November 14 | [Arrays & Linked Lists](Class7.md)       |
|   8   | Thursday, November 16 | [Hash Tables](Class8.md)                 |
|   9   |  Tuesday, November 28 | [Algorithm Analysis](Class9.md)          |
|  10   | Thursday, November 30 | [Higher Order Markov Chains](Class10.md) |
|  11   |  Tuesday, December 5  | [Regular Expressions](Class11.md)        |
|  12   | Thursday, December 7  | Parsing & Tokenization     |
