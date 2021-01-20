from linked_list_structure import *
def remove_head(head):
  head = head.next 

# by value
def remove_middle(head,target):
  temp = head
  while(temp):
    if(temp.next and temp.next.value == target):
      temp.next = temp.next.next 
      break
    temp = temp.next 
  return 

# test
# l1 = LinkedList([1,2,3,4,5])
# print(l1)
# remove_middle(l1.head, 3)
# print(l1)

def remove_tail(head):
  temp = head
  while(temp.next):
    if(not temp.next.next):
      temp.next = None
      break
    temp = temp.next
# test
# l1 = LinkedList([1,2,3,4,5])
# print(l1)
# remove_tail(l1.head)
# print(l1)
