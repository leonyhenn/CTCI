# Hash Table

**Definition**

A data structure that maps key to values for highly efficient lookups

**Purpose**

- **Speed:** Average case O(1) search speed 
  - Can handle large number of entries


**Ways of implementation**  

1. A hash function, a list of linked list
2. A hash function, a dictionary of linked list

**Substitute**

Set

**Operations and its runtime**
- insert:   
  1. *Hashing:* O(1)
  2. *Insert:* 
      - Avg case O(1): Empty slot
      - Worst case O(n): Think of a terrible hash function like *H(parameter) = 1* all data is being hashed into one slot. Therefore each insert would be at the end of the linked list
- search:
  1. *Hashing:* O(1)
  2. *Search:*
      - Avg case O(1): Data is right at the slot
      - Worst case O(n): - Worst case O(n): Think of a terrible hash function like *H(parameter) = 1* all data is being hashed into one slot, and the value you are looking for is at the end of the linked list. Therefore the search would be an O(n) operation

- delete:  
  1. *Hashing:* O(1)
  2. *Search:*
      - Avg case O(1): Data is right at the slot
      - Worst case O(n): - Worst case O(n): Think of a terrible hash function like *H(parameter) = 1* all data is being hashed into one slot, and the value you are looking for is at the end of the linked list. Therefore the delete would be an O(n) operation

**Misc**  

Hash table can be **collision-free** or even **perfect** with correct choice of hash function

[What is the difference between HashSet, HashMap and hash table? How do they behave in a multi-threaded environment?](https://www.quora.com/What-is-the-difference-between-HashSet-HashMap-and-hash-table-How-do-they-behave-in-a-multi-threaded-environment)


