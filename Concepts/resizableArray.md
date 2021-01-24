# Resizable Arrays 
### **e.g. Java ArrayList**
&nbsp;

**Definition**

1. An array resizes itself
2. Provide O(1) access time

**Purpose**

In some languages like Python, array are automatically resized. In some languages like Java, arrays have fixed length, the size is defined while it is being created. Thus, we need an array-like data structure that offers dynamic resizing. 

**implementation**

When array size is full, the array doubles in size  
   1. Array is full
   2. New array is created with double the original length (O(1))  
   3. Go through each character, copy and paste original sentence and new sentence to new array (O(n), n = len(orginal+new))  
   4. Return new array

**implementation in Java**

```
ArrayList<string> merge(String[] original, String[] new) {
  ArrayList<string> newSentence = new ArrayList<string>();
  for(String c: original){
    newSentence.add(c)
  }
  for(String c: new){
    newSentence.add(c)
  }
  return newSentence
}
```

**Time Complexity**

  - Insertion: O(1) on average, some worst case might cost O(N)
    - O(N)? Think about a case where array length is 1, and we just entered a new character. This would copy/paste both old and new character, thus O(N)

**Armotization 平摊**

  - Each insertion cost O(1) on average, even though some insertions take O(N) time in the worst case

  - Intuition: 
    - While certain operations for a given algorithm may have a significant cost in resources, other operations may not be as costly.
    - The amortized analysis considers both the costly and less costly operations together over the whole series of operations of the algorithm

  - Application in Resizable Array:
    - Copy old elements to a new address is costly
    - But it does not happen often
    - We can proof the number of insert on input N is [(N/2) + (N/4) + ... 2 + 1], which is less than N
      - 一尺之槌，日取其半，万事不竭
        






