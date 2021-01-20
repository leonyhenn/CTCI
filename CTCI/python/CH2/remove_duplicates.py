from linked_list_structure import *

def delete(cur):
  if cur.next and cur.next.next:
    cur.next = cur.next.next 
  else:
    cur.next = None


# v1 - infinite loop
# def remove_duplicates(head):
#   if not head or not head.next:
#     return
#   seen = set()
#   cur = head
#   seen.add(cur)
#   while(cur):
#     if(cur.next):
#       seen.add(cur.next)
#     else:
#       delete(cur)
#     cur = cur.next

# l1 = LinkedList([5,3,4,1,2,3,4])
# print(l1)

# remove_duplicates(l1.head)
# print(l1)

# v2 - tail failed to delete
# def remove_duplicates(head):
#   if not head or not head.next:
#     return
#   seen = set()
#   cur = head
#   seen.add(cur.value)
#   while(cur.next):
#     if(cur.next.value not in seen):
      
#       seen.add(cur.next.value)
#     else:
#       delete(cur)
#     cur = cur.next
#   if(cur.value in seen):
#     delete(cur)

# l1 = LinkedList([5,3,4,1,2,3,4])
# print(l1)
# remove_duplicates(l1.head)
# print(l1)
  
    